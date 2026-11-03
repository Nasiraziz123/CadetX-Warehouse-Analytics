# Week 4 — Product Analytics

## Overview

Week 4 focuses on analyzing product-level sales performance and historical demand patterns within the CadetX Heavy Supplier, Inventory & Warehouse Analytics project.

The objective was to evaluate product performance using delivered sales data, identify relatively high- and low-performing products, classify products using ABC analysis, and examine demand trends over time.

The analysis was conducted using Python and Pandas.

## Objectives

- Understand and validate the product and sales datasets.
- Evaluate product performance using sales quantity, revenue, and order frequency.
- Identify relatively fast-moving and slow-moving products.
- Perform ABC / Pareto product classification.
- Analyze monthly, annual, and product-level demand trends.
- Develop business findings and recommendations based on the results.

## Datasets Used

| Dataset | Records | Columns | Purpose |
|---|---:|---:|---|
| `products.csv` | 30 | 23 | Product information and attributes |
| `sales_orders_header.csv` | 20,000 | 11 | Order dates, statuses, and order-level information |
| `sales_orders_lines.csv` | 130,402 | 9 | Product-level sales transactions |

## Data Validation

Data quality checks were performed before beginning the analysis.

The following checks were completed:

- Missing-value validation.
- Exact duplicate-row validation.
- Primary-key uniqueness checks.
- Product and sales-order relationship validation.
- Duplicate sales-order line identification.
- Orders without corresponding sales lines.
- Date conversion and validation.

**Validation results:** All checks passed. No missing values, exact duplicate rows, invalid product references, or invalid sales-order references were identified.

## Analysis Performed

### 1. Product Performance Analysis

Evaluated all 30 products using:

- Total quantity sold.
- Total sales revenue.
- Number of distinct orders.
- Average selling price.
- Revenue contribution percentage.

Delivered orders were used as the primary basis for product performance. Cancelled orders were kept separate.

### 2. Fast-Moving and Slow-Moving Product Analysis

Products were compared using total quantity sold and order frequency.

Key results:

- Highest quantity sold: P029 — Pressure Sensor PS-90.
- Highest order frequency: P011 — Hydraulic Cylinder HC-200.
- Lowest quantity sold: P024 — Track Roller TR-60.
- Lowest order frequency: P004 — Track Chain TC-45.

These are relative rankings within the dataset. They do not independently establish dead stock or actual inventory movement status.

### 3. ABC / Pareto Analysis

Products were classified according to their cumulative contribution to total delivered sales revenue.

| Classification | Products | Revenue Contribution |
|---|---:|---:|
| A | 10 | 81.53% |
| B | 7 | 14.07% |
| C | 13 | 4.40% |

Category A products account for the largest share of sales revenue and therefore deserve closer commercial attention.

### 4. Product Demand Trend Analysis

Demand was examined at three levels:

- Monthly demand from January 2019 to December 2024.
- Annual demand and year-over-year changes.
- Individual product demand trends across the six-year period.

Key observations:

- 2020 recorded the highest annual quantity and revenue.
- 2024 recorded the lowest annual quantity and revenue.
- Compared with 2023, 2024 quantity declined by 2.34% and revenue declined by 3.84%.
- 21 products experienced more annual decreases than increases, while 9 experienced more annual increases than decreases.

## Key Business Findings

1. The top two products by revenue, P015 and P014, contributed approximately 35.92% of total delivered sales revenue.
2. The top ten products accounted for approximately 81.54% of total delivered sales revenue.
3. The product with the highest quantity sold was not the product with the highest revenue.
4. ABC analysis identified ten Category A products contributing approximately 81.53% of revenue.
5. Annual demand fluctuated over the six-year period, with 2024 showing a decline compared with 2023.
6. Individual product demand patterns varied, even when overall portfolio demand appeared relatively stable.

## Business Recommendations

- Monitor Category A products closely because of their substantial revenue contribution.
- Consider both quantity sold and order frequency when evaluating product movement.
- Review products showing repeated annual demand declines.
- Monitor products with increasing demand to support appropriate future planning.
- Combine sales performance with inventory availability, stock levels, lead times, and product criticality before making inventory decisions.

## Documentation

Detailed Week 4 documentation is available below:

1. [Product Analytics Report](DOCS/week_4_product_analytics_report.md)
2. [ABC Classification and Demand Trend Analysis Report](DOCS/week_4_feature_engineering_and_demand_analysis_report.md)
3. [Scrum Master Sprint Notes](DOCS/week_4_sprint_notes.md)

## Tools and Technologies

- Python
- Pandas
- CSV datasets
- Git and GitHub

## Deliverables

- Product and sales data validation.
- Product performance analysis.
- Fast-moving and slow-moving product comparisons.
- ABC / Pareto classification.
- Monthly, annual, and product-level demand trend analysis.
- Business findings and recommendations.
- Week 4 analytical documentation.

## Limitations

- Delivered orders were used for the primary analysis; cancelled orders were kept separate.
- Revenue was calculated using `line_total`, excluding GST.
- ABC classification was based on revenue, not margin or operational criticality.
- Fast-moving and slow-moving rankings represent relative sales comparisons.
- Actual dead stock cannot be confirmed without inventory stock levels and stock-age information.
- Historical demand patterns do not establish the causes of changes or guarantee future demand.

## Conclusion

Week 4 provided a detailed assessment of product sales performance and historical demand patterns. The analysis highlighted revenue concentration, differences between product quantity and revenue performance, and variations in demand across products and years.

These findings provide a product-level analytical foundation for the next phase of the project, where inventory-related analysis can be conducted using appropriate stock and inventory information.