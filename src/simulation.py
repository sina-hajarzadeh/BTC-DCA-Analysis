import pandas as pd
from tqdm import tqdm


# Load btc historical data
data = pd.read_csv('data/cleaned.csv')


# -------------------------------------------------------
#      UNIVERSAL DCA SIMULATOR (1-YEAR / 4-YEAR)
# -------------------------------------------------------
def run_dca(start_id, initial_daily_invest_USD, df, total_days, yearly_multiplication=None):
    """
    Simulates a DCA strategy starting from a specific row (start_id).

    Parameters
    ----------
    start_id : int
        Index in the dataset representing the first day of investment.
    initial_daily_invest_USD : float
        The daily investment amount in USD (base value for year 0).
    df : DataFrame
        Bitcoin OHLC dataset.
    total_days : int
        Number of days to invest (365 for 1Y, 1460 for 4Y).
    yearly_multiplication : float or None
        If not None, the daily investment for each year is:
            daily = initial_daily_invest_USD * (yearly_multiplication ** year)

    Returns
    -------
    (start_date, end_date, final_USD, payment_USD, profit_USD, owned_BTC)
    """

    # Price and date lookup by Id (fast direct access)
    rate_series = df.set_index('Id')['close']
    date_series = df.set_index('Id')['date']

    payment_USD = 0.0      # Total USD invested
    owned_BTC = 0.0        # Total BTC accumulated

    # Simulate day by day for total_days
    for day_index in range(total_days):

        # Determine which "year" of DCA we are in
        if yearly_multiplication is not None:
            year = day_index // 365
            daily_invest = initial_daily_invest_USD * (yearly_multiplication ** year)
        else:
            daily_invest = initial_daily_invest_USD

        # Identify BTC price for this day
        day_id = start_id + day_index
        rate = rate_series[day_id]

        # Execute purchase
        owned_BTC += daily_invest / rate
        payment_USD += daily_invest

    # Final portfolio value after total_days
    final_USD = owned_BTC * rate
    profit_USD = final_USD - payment_USD

    # Convert numeric IDs back to timestamps
    start_date = date_series[start_id]
    end_date = date_series[start_id + total_days - 1]

    return start_date, end_date, final_USD, payment_USD, profit_USD, owned_BTC


# -------------------------------------------------------
#        CSV APPEND HELPERS (4Y & 1Y RECORDING)
# -------------------------------------------------------
def result_result_4y_to_csv(start_id, initial_daily, yearly_mult, df):
    """
    Executes a single 4-year DCA simulation and appends the results
    to dca4y_result.csv.
    """
    start_date, end_date, final_USD, payment_USD, profit_USD, owned_BTC = \
        run_dca(start_id, initial_daily, df, total_days=365*4, yearly_multiplication=yearly_mult)

    row = pd.DataFrame([{
        "start_date": start_date,
        "end_date": end_date,
        "initial_daily_invest_USD": initial_daily,
        "yearly_multiplication": yearly_mult,
        "final_USD": round(final_USD, 2),
        "payment_USD": round(payment_USD, 2),
        "profit_USD": round(profit_USD, 2),
        "owned_BTC": round(owned_BTC, 10)
    }])

    # Append without header
    row.to_csv("data/dca4y_result.csv", mode='a', header=False, index=False)


def result_result_1y_to_csv(start_id, initial_daily, df):
    """
    Executes a 1-year DCA simulation (no yearly multiplier)
    and appends the output to dca1y_result.csv.
    """
    start_date, end_date, final_USD, payment_USD, profit_USD, owned_BTC = \
        run_dca(start_id, initial_daily, df, total_days=365, yearly_multiplication=None)

    row = pd.DataFrame([{
        "start_date": start_date,
        "end_date": end_date,
        "initial_daily_invest_USD": initial_daily,
        "final_USD": round(final_USD, 2),
        "payment_USD": round(payment_USD, 2),
        "profit_USD": round(profit_USD, 2),
        "owned_BTC": round(owned_BTC, 10)
    }])

    row.to_csv("data/dca1y_result.csv", mode='a', header=False, index=False)


# -------------------------------------------------------
#               INITIALIZE EMPTY OUTPUT FILES
# -------------------------------------------------------
# Create headers for result files (overwrite old content)
pd.DataFrame(columns=[
    "start_date", "end_date",
    "initial_daily_invest_USD", "yearly_multiplication",
    "final_USD", "payment_USD", "profit_USD", "owned_BTC"
]).to_csv("data/dca4y_result.csv", index=False)

pd.DataFrame(columns=[
    "start_date", "end_date",
    "initial_daily_invest_USD",
    "final_USD", "payment_USD", "profit_USD", "owned_BTC"
]).to_csv("data/dca1y_result.csv", index=False)


# -------------------------------------------------------
#               RUN EXPERIMENTS (MAIN LOOP)
# -------------------------------------------------------
initial_values = [0.5, 1, 2, 5, 10, 20, 50, 100]                 # Different base DCA amounts
multipliers = [0.9, 1.0, 1.02, 1.05, 1.10, 1.20]                 # Yearly investment growth factors

# ---- 4-YEAR SIMULATION (full grid search) ----
print("Running 4Y DCA simulations...")
for initial in initial_values:
    for mult in multipliers:
        # Try starting from every possible date where 4 years of data exist
        for start_id in tqdm(range(1, 2148)):
            result_result_4y_to_csv(start_id, initial, mult, data)

# ---- 1-YEAR SIMULATION ----
print("Running 1Y DCA simulations...")
for initial in initial_values:
    # Try every possible starting date where 1 year exists
    for start_id in tqdm(range(1, 3243)):
        result_result_1y_to_csv(start_id, initial, data)


# -------------------------------------------------------
#          LOAD, POSTPROCESS, AND SORT THE RESULTS
# -------------------------------------------------------
# ---- 4Y results ----
result4y = pd.read_csv("data/dca4y_result.csv")
result4y['roi_percent'] = result4y["profit_USD"] / result4y["payment_USD"] * 100
result4y["start_date"] = pd.to_datetime(result4y["start_date"])
result4y["end_date"] = pd.to_datetime(result4y["end_date"])

# Sort by parameters and chronological order
result4y = result4y.sort_values(
    ['initial_daily_invest_USD','yearly_multiplication','start_date'],
    ascending=True
).reset_index(drop=True)

result4y.to_csv("data/dca4y_result.csv") 


# ---- 1Y results ----
result1y = pd.read_csv("data/dca1y_result.csv")
result1y['roi_percent'] = result1y["profit_USD"] / result1y["payment_USD"] * 100
result1y["start_date"] = pd.to_datetime(result1y["start_date"])
result1y["end_date"] = pd.to_datetime(result1y["end_date"])

result1y = result1y.sort_values(
    ['initial_daily_invest_USD','start_date'],
    ascending=True
).reset_index(drop=True)

result1y.to_csv("data/ca1y_result.csv")
