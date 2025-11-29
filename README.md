# DCA-Based Bitcoin Market Analysis (2016–2024)

A complete analytical study of how **4-year Dollar-Cost Averaging (DCA)** performs across different Bitcoin market cycles — especially around **halving events**.  
The analysis covers thousands of simulated start dates and evaluates how long-term DCA behaves under different conditions, including investment scaling and market timing.

This project includes:
- A full Jupyter notebook with simulations
- A polished PDF report (LaTeX)
- High-quality insight visuals (PNG)
- Clean and reproducible code

---

## Overview

DCA is a strategy where a fixed amount of money is invested at regular intervals, regardless of price fluctuations.  
This project analyzes:

- How **4-year DCA** performs across multiple BTC cycles  
- How it compares with **1-year DCA**  
- How **investment multipliers** (0.9 → invest earlier, 1.1 → invest later) impact ROI  
- How returns behave relative to **halving cycles**   
- How scaling daily investment (1 USD vs 10 USD) affects results  

The full analysis is available in both **Jupyter notebook** and **PDF report** formats.

---

## Key Findings (Summary)

### **1. Long-term DCA dominates short-term DCA**  
Q1 of 4-year results is higher than Q3 of 1-year results → far more stable and consistently profitable.

### **2. ROI distribution is right-skewed**  
Typical returns are between **50–200%**, but rare outliers can exceed **800%**.

### **3. Investing earlier outperforms investing later**  
A multiplier of **0.9** (more capital earlier) beats **1.1** (more capital later) across all cycles.

### **4. Cycle timing matters**  
Best results come from entering **early in the cycle**, before large expansions.  
Worst results happen when entering **late** or **deep in bear markets**.

### **5. Post-halving peaks are consistent**  
Both 2016 and 2020 cycles peaked **7–8 months after halving**.

### **6. Scaling daily investment preserves the distribution**  
10 USD/day is simply **10×** the returns of 1 USD/day.  
No structural difference → the strategy scales linearly.

---

## Insight Visuals

All charts and insight summaries are available under:

```
/insights/
```

Each PNG file corresponds to a core insight discussed in the PDF report.

---

## Project Structure

```
BTC-DCA-Analysis/
│
├── data/                # Price data + processed simulation outputs
├── notebook/
│   └── Analysis.ipynb   # Full reproducible notebook
│
├── insights/            # Insight PNGs for presentation
│   ├── Insight1.png
│   ├── Insight2.png
│   ├── ...
│
├── reports/
│   └── DCA_Report.pdf   # Final polished LaTeX report
│
├── src/                 # Utility scripts separated from notebook
│
└── README.md            # ← You are here
```

---

## How to Run the Notebook

### **1. Clone the repository**
```bash
git clone https://github.com/sina-hajarzadeh/BTC-DCA-Analysis.git
cd BTC-DCA-Analysis
```

### **2. Install dependencies**
```
pip install -r requirements.txt
```

### **3. Start Jupyter**
```bash
jupyter notebook
```

Open:

```
notebook/Analysis.ipynb
```

---

## Methodology 

For each possible start date between 2016 and 2021:

1. Simulate buying a fixed USD amount of BTC every day for **4 years**  
2. Convert all accumulated BTC back to USD  
3. Compute:
   - Total invested
   - Total BTC acquired
   - Profit
   - ROI%
4. Repeat with:
   - Different daily investment amounts (**0.5 → 100 USD**)
   - Different yearly multipliers (**0.9 → 1.2**)
5. Compare performance across:
   - Halving cycles
   - Bull/bear phases
   - Distribution statistics
   - Variance and IQR behavior

---

## Full Report (PDF)

A polished LaTeX-generated PDF summarizing all insights, figures, and interpretations:

**/reports/DCA_Report.pdf**

---

## Author

**Sina Hajarzadeh**  
 *sina.hajarzadeh@gmail.com*  
 *[LinkedIn profile](https://www.linkedin.com/in/sinahj/)*  
 *[Kaggle profile](https://www.kaggle.com/sinahjarzadeh)*   
 
 

If you find this analysis useful or want to collaborate, feel free to reach out.

---

## ⭐ If you liked this project

You can help by **starring ⭐ the repository** — it really helps visibility and credibility.

---

