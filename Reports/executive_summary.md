# Executive Summary — Retail Sales & Profitability Analysis

## Overview
This project analyzes retail sales transaction data (9,994 orders) to identify key drivers of sales and profitability, uncover underperforming segments, and provide data-backed recommendations for improving profit margins.

## Key Findings

**Category Performance**
- Technology leads in both sales (approx. $836K) and profit (approx. $145K).
- Furniture generates strong sales (approx. $742K) but disproportionately low profit (approx. $18K) — a significant margin issue.
- Office Supplies delivers solid profit (approx. $122K) relative to its sales (approx. $719K).

**Sub-Category Risk**
- Certain sub-categories (notably Tables and Bookcases) operate at a net loss, driven by heavy discounting.

**Statistical Validation**
- Sales and Profit show a statistically significant moderate positive correlation (r = 0.4791, p < 0.0001).
- Technology's average profit is significantly higher than Furniture's (t = 7.1232, p < 0.0001).
- No statistically significant difference in average sales across customer segments — Consumer, Corporate, Home Office (F = 0.5952, p = 0.5515).

**Predictive Modeling**
- A linear regression model was built to predict order-level profit from sales, discount, quantity, category, sub-category, region, and segment.
- Result: MAE = 67.69, RMSE = 282.41, R² = -0.6450.
- The negative R² shows profit is not well explained by a linear combination of these features — likely due to a non-linear interaction between discount and sales (high discounts on high-value orders disproportionately erode profit). This is a useful negative result, not a failure: it reinforces that discount policy, not sales volume, is the more actionable lever.

## Business Recommendations
1. **Review discount policy on Furniture**, especially Tables and Bookcases, where heavy discounting is eroding profit despite healthy sales volume.
2. **Continue prioritizing Technology** as the strongest and most reliable profit driver.
3. **Don't over-index marketing spend by customer segment** — segment does not significantly affect sales, so differentiation should focus on category and region instead.
4. **Investigate non-linear modeling** (e.g., Random Forest or Gradient Boosting with sales-discount interaction terms) as a next step to build a more accurate profit-prediction tool.

## Methodology
1. **Data Cleaning** (`01_data_cleaning.ipynb`) — loaded raw data, validated nulls/duplicates/business rules, engineered features (shipping days, profit margin, order year/month).
2. **Exploratory Data Analysis** (`02_eda.ipynb`) — sales/profit breakdowns by category, sub-category, and region; trend and discount analysis.
3. **Statistical Analysis** (`03_statistical_analysis.ipynb`) — Pearson correlation, independent t-test, and one-way ANOVA to validate EDA findings.
4. **Predictive Modeling** (`04_modeling.ipynb`) — linear regression to predict profit; evaluated and honestly reported limitations.

## Tools Used
Python (pandas, numpy, scipy, scikit-learn, matplotlib), Power BI, Tableau Public.
