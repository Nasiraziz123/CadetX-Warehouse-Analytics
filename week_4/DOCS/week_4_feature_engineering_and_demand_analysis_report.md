# Week 4 — ABC Classification and Demand Trend Analysis Report

## 1. Introduction

This report documents the ABC classification and product demand trend analysis completed during Week 4 of the CadetX Heavy Supplier, Inventory & Warehouse Analytics project.

The objective was to understand how product revenue is distributed across the product portfolio and examine historical demand patterns over time.

The analysis was performed using Python and Pandas, using delivered sales transactions from January 2019 to December 2024.

## 2. Analytical Scope

The analysis covered two major areas:

**ABC / Pareto Analysis**
- Calculate each product's contribution to total delivered sales revenue.
- Calculate cumulative revenue contribution.
- Classify products into A, B, and C categories.
- Examine the revenue distribution across the three categories.

**Demand Trend Analysis**
- Analyze monthly demand patterns.
- Compare annual demand and year-over-year changes.
- Examine individual product demand across the six-year period.
- Identify products with more annual increases or decreases in quantity sold.

The analysis used delivered sales only, with `line_total` as revenue, excluding GST.

## 3. ABC / Pareto Analysis

### 3.1 Methodology

ABC analysis was performed using each product's contribution to total delivered sales revenue.

The steps were:

1. Sort products in descending order of total revenue.
2. Calculate each product's percentage contribution to total revenue.
3. Calculate cumulative revenue contribution.
4. Assign ABC categories based on cumulative contribution.

The classification thresholds were:

| Category | Cumulative Revenue Contribution |
|---|---|
| A | Products contributing up to approximately 80% |
| B | Products contributing through approximately 95% |
| C | Remaining products |

For classification, the product that crosses a threshold remains in the category it brings to that threshold. This avoids leaving boundary products unclassified.

### 3.2 ABC Classification Results

| Category | Number of Products | Total Revenue | Revenue Contribution |
|---|---:|---:|---:|
| A | 10 | 18,718,459,400 | 81.53% |
| B | 7 | 3,229,679,500 | 14.07% |
| C | 13 | 1,010,848,530 | 4.40% |
| **Total** | **30** | **22,958,987,430** | **100%** |

### 3.3 Key Observations

- Category A contains 10 products and contributes approximately 81.53% of total delivered revenue.
- Category B contains 7 products and contributes approximately 14.07%.
- Category C contains 13 products and contributes approximately 4.40%.
- A relatively small portion of the product portfolio accounts for the majority of delivered sales revenue.

The product P022 Control Valve CV-75 was included in Category A because it crossed the 80% cumulative revenue threshold.

### 3.4 Business Interpretation

Category A products make the largest contribution to revenue and therefore deserve closer commercial monitoring.

Category B products provide a moderate contribution, while Category C products account for a smaller share of revenue.

However, ABC classification is based on revenue contribution only. A product in Category C may still be operationally important because of its criticality, customer requirements, or machine compatibility.

ABC classification should therefore be considered alongside other product and inventory information before making operational decisions.

## 4. Monthly Demand Trend Analysis

### 4.1 Methodology

Monthly demand was calculated by grouping delivered sales transactions by order month.

The following metrics were aggregated:

- Total quantity sold.
- Total revenue.
- Number of distinct orders.

The analysis covered 72 months, from January 2019 through December 2024.

### 4.2 Monthly Demand Summary

| Metric | Result |
|---|---:|
| Analysis period | January 2019 – December 2024 |
| Number of months | 72 |
| Average monthly quantity sold | 17,151.93 |
| Average monthly revenue | 318,874,800 |
| Average monthly orders | 250.46 |
| Highest monthly quantity | 22,304 |
| Lowest monthly quantity | 14,117 |
| Highest monthly revenue | 407,508,620 |
| Lowest monthly revenue | 258,162,180 |

### 4.3 Highest and Lowest Demand Months

| Metric | Month | Value |
|---|---|---:|
| Highest quantity sold | July 2020 | 22,304 |
| Lowest quantity sold | February 2019 | 14,117 |
| Highest revenue | July 2020 | 407,508,620 |
| Lowest revenue | February 2019 | 258,162,180 |

### 4.4 Interpretation

Monthly demand fluctuated throughout the analysis period.

July 2020 recorded the highest monthly quantity and revenue, while February 2019 recorded the lowest values for both metrics.

These results show that demand was not constant from month to month. However, monthly fluctuations alone do not establish a long-term upward or downward trend.

## 5. Annual Demand Trend Analysis

### 5.1 Methodology

Monthly demand data was aggregated by calendar year to evaluate annual performance.

The following metrics were calculated:

- Total quantity sold.
- Total revenue.
- Total orders.
- Year-over-year growth in quantity.
- Year-over-year growth in revenue.
- Year-over-year growth in orders.

Growth percentages were calculated by comparing each year with the previous year.

### 5.2 Annual Demand Results

| Year | Quantity Sold | Revenue | Orders | Quantity Growth | Revenue Growth | Orders Growth |
|---|---:|---:|---:|---:|---:|---:|
| 2019 | 207,925 | 3,870,016,600 | 3,031 | — | — | — |
| 2020 | 212,007 | 3,917,532,120 | 3,038 | +1.96% | +1.23% | +0.23% |
| 2021 | 208,269 | 3,852,479,620 | 3,038 | -1.76% | -1.66% | 0.00% |
| 2022 | 202,242 | 3,816,288,220 | 2,948 | -2.89% | -0.94% | -2.96% |
| 2023 | 204,638 | 3,824,675,310 | 3,022 | +1.18% | +0.22% | +2.51% |
| 2024 | 199,858 | 3,677,995,560 | 2,956 | -2.34% | -3.84% | -2.18% |

### 5.3 Key Observations

**2020 performance**

2020 recorded the highest annual quantity sold and revenue during the analysis period.

**2021 and 2022 decline**

Quantity and revenue declined in both 2021 and 2022 compared with their respective previous years.

**2023 recovery**

In 2023, quantity increased by 1.18%, revenue increased by 0.22%, and orders increased by 2.51% compared with 2022.

**2024 decline**

In 2024, quantity declined by 2.34%, revenue declined by 3.84%, and orders declined by 2.18% compared with 2023.

2024 recorded the lowest annual quantity and revenue across the six-year period.

### 5.4 Interpretation

Annual results indicate that overall demand fluctuated rather than following a consistent upward trend.

The portfolio experienced modest growth in 2020, declines in 2021 and 2022, a partial recovery in 2023, and another decline in 2024.

The 2024 results indicate weaker performance compared with 2023 and deserve further monitoring.

These historical changes do not, by themselves, explain why demand increased or decreased.

## 6. Product-Level Annual Demand Analysis

### 6.1 Methodology

To understand differences between individual products, delivered sales were grouped by:

- Calendar year.
- Product ID.

For each product and year, the analysis calculated:

- Total quantity sold.
- Total revenue.
- Number of distinct orders.

This produced 180 product-year records, representing 30 products across six years.

All 30 products were represented in every year from 2019 through 2024.

### 6.2 Product Quantity Change: 2019 vs. 2024

The first and final years of the analysis period were compared to identify products with the largest quantity increases and decreases.

**Largest quantity increases**

| Product ID | Product Name | Quantity Change | Percentage Change |
|---|---|---:|---:|
| P006 | Alternator ALT-500 | +918 | +14.73% |
| P024 | Track Roller TR-60 | +407 | +6.53% |
| P014 | Transmission Assembly TA-800 | +354 | +5.50% |
| P029 | Pressure Sensor PS-90 | +363 | +5.11% |
| P016 | Radiator RD-250 | +339 | +5.10% |

**Largest quantity decreases**

| Product ID | Product Name | Quantity Change | Percentage Change |
|---|---|---:|---:|
| P012 | Brake Pad BP-40 | -1,158 | -15.50% |
| P019 | Swing Motor SWM-350 | -1,000 | -14.04% |
| P010 | Turbocharger TB-900 | -938 | -12.69% |
| P005 | Fuel Injector FI-220 | -752 | -10.92% |
| P004 | Track Chain TC-45 | -811 | -10.83% |

### 6.3 Interpretation

Individual products experienced different demand changes between 2019 and 2024.

P006 Alternator ALT-500 recorded the largest quantity increase, while P012 Brake Pad BP-40 recorded the largest decrease.

These comparisons show that overall portfolio performance can hide important differences between individual products.

A first-year versus final-year comparison does not prove that demand continuously increased or decreased throughout the entire period.

## 7. Year-over-Year Product Trend Patterns

### 7.1 Methodology

Product-level annual quantities were arranged by product and year.

Year-over-year percentage changes were calculated for each product.

For every product, the analysis counted:

- Years with increasing quantity.
- Years with decreasing quantity.
- Years with unchanged quantity.

Each product had five year-over-year comparisons across the six-year period.

### 7.2 Results

| Trend Pattern | Number of Products |
|---|---:|
| More annual decreases than increases | 21 |
| More annual increases than decreases | 9 |
| Equal increases and decreases | 0 |
| **Total** | **30** |

### 7.3 Interpretation

- 21 products, representing 70% of the portfolio, experienced more annual decreases than increases.
- 9 products, representing 30% of the portfolio, experienced more annual increases than decreases.
- No products had an equal number of annual increases and decreases.

This comparison describes how frequently annual quantity changed in each direction.

It does not measure the magnitude of those changes or establish a continuous trend. A product may have more years of increasing demand while still recording a lower quantity in 2024 than in 2019.

## 8. Combined Business Findings

The ABC and demand trend analyses produced the following findings:

1. Category A contains 10 products that account for approximately 81.53% of delivered sales revenue.
2. Category C contains 13 products but contributes only approximately 4.40% of delivered revenue.
3. Monthly demand fluctuated throughout the 72-month analysis period.
4. July 2020 recorded the highest monthly quantity and revenue.
5. 2020 was the strongest year for annual quantity and revenue.
6. 2024 recorded the lowest annual quantity and revenue.
7. 21 products experienced more annual decreases than increases in quantity sold.
8. Individual product demand patterns differed from the overall portfolio trend.
9. P006 Alternator ALT-500 recorded the largest quantity increase between 2019 and 2024.
10. P012 Brake Pad BP-40 recorded the largest quantity decrease between 2019 and 2024.

## 9. Business Recommendations

Based on the analysis, the following recommendations are proposed:

### 9.1 Monitor Category A Products

Give closer commercial attention to Category A products because they account for the largest share of delivered revenue.

### 9.2 Review Products with Declining Demand

Monitor products that experienced repeated annual decreases to determine whether the changes continue in subsequent periods.

### 9.3 Monitor Products with Increasing Demand

Review products with increasing demand to understand whether the pattern continues and whether future planning should account for it.

### 9.4 Use Multiple Indicators

Combine revenue contribution, quantity sold, order frequency, and product criticality when evaluating product performance.

### 9.5 Continue Demand Monitoring

Use monthly and annual demand comparisons to identify changes in product performance over time.

### 9.6 Combine Sales and Inventory Information

Before making inventory-related decisions, combine demand analysis with actual stock levels, stock age, lead times, reorder levels, and safety stock information.

## 10. Analysis Limitations

The following limitations apply:

- The analysis used delivered sales transactions only.
- Revenue was calculated using `line_total`, excluding GST.
- ABC classification was based on revenue contribution, not profit or operational criticality.
- Historical demand patterns do not establish the causes of changes.
- First-year versus final-year comparisons do not establish continuous trends.
- The number of annual increases or decreases does not measure the magnitude of demand changes.
- Sales data alone cannot establish actual stock availability, inventory aging, or dead-stock status.
- Historical results should not be treated as guaranteed future demand.

## 11. Conclusion

The ABC classification showed that a relatively small group of products contributes the majority of delivered sales revenue.

Demand trend analysis revealed monthly and annual fluctuations, with 2020 recording the strongest annual performance and 2024 recording the weakest.

Product-level comparisons also showed that demand patterns differ across the portfolio. Some products experienced increases while others experienced repeated declines.

These findings provide a historical view of product revenue concentration and demand behavior. They can support future product and inventory planning when considered alongside actual inventory information and operational requirements.