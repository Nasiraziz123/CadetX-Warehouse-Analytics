# Week 4 — Scrum Master Sprint Notes

## 1. Sprint Overview

**Project:** Heavy Supplier, Inventory & Warehouse Analytics  
**Programme:** CadetX Virtual Work Experience  
**Phase:** Phase 2 — Core Product, Inventory & Warehouse Analytics  
**Sprint:** Week 4 — Product Analytics  
**Status:** Completed

## 2. Sprint Objective

The objective of Week 4 was to evaluate product-level sales performance and historical demand patterns using the available product and sales datasets.

The sprint focused on understanding product performance, comparing product movement, performing ABC classification, analyzing demand trends, and developing business findings and recommendations.

## 3. Planned Sprint Tasks

The following tasks were included in the Week 4 scope:

1. Understand and validate product and sales datasets.
2. Perform product performance analysis.
3. Identify relatively fast-moving and slow-moving products.
4. Perform ABC / Pareto product classification.
5. Analyze monthly and annual demand trends.
6. Analyze individual product demand patterns.
7. Prepare business findings and recommendations.
8. Organize code, results, and documentation for submission.

## 4. Completed Sprint Tasks

| Task | Description | Status |
|---|---|---|
| Data understanding and validation | Examined dataset structure, missing values, duplicates, keys, relationships, and dates | Completed |
| Product performance analysis | Evaluated quantity sold, revenue, order frequency, and revenue contribution | Completed |
| Fast-moving product analysis | Identified products with relatively higher quantity sold and order frequency | Completed |
| Slow-moving product comparison | Identified products with relatively lower quantity sold and order frequency | Completed |
| ABC / Pareto analysis | Classified products using cumulative revenue contribution | Completed |
| Monthly demand analysis | Examined monthly quantity, revenue, and order patterns | Completed |
| Annual demand analysis | Compared annual performance and year-over-year changes | Completed |
| Product-level demand analysis | Compared annual quantity changes across individual products | Completed |
| Business findings and recommendations | Prepared conclusions and recommendations based on the analysis | Completed |
| Documentation | Prepared detailed Week 4 analytical reports and sprint notes | Completed |

## 5. Key Sprint Outcomes

### 5.1 Data Validation

- Three datasets were used: products, sales orders header, and sales orders lines.
- All performed data quality checks passed.
- No missing values or exact duplicate rows were identified.
- Product and sales-order relationships were validated successfully.

### 5.2 Product Performance

- All 30 products were evaluated.
- P015 Engine Block EB-600 recorded the highest revenue.
- P029 Pressure Sensor PS-90 recorded the highest quantity sold.
- P011 Hydraulic Cylinder HC-200 appeared in the highest number of distinct orders.

### 5.3 Product Movement

- P024 Track Roller TR-60 recorded the lowest quantity sold.
- P004 Track Chain TC-45 recorded the lowest order frequency.
- All 30 products recorded substantial sales activity, so the results were treated as relative rankings rather than evidence of dead stock.

### 5.4 ABC Classification

| Category | Products | Revenue Contribution |
|---|---:|---:|
| A | 10 | 81.53% |
| B | 7 | 14.07% |
| C | 13 | 4.40% |

Category A products accounted for the largest share of delivered sales revenue.

### 5.5 Demand Trend Analysis

- The monthly analysis covered 72 months, from January 2019 to December 2024.
- 2020 recorded the highest annual quantity and revenue.
- 2024 recorded the lowest annual quantity and revenue.
- 21 products experienced more annual decreases than increases in quantity sold.
- 9 products experienced more annual increases than decreases.

## 6. Analytical Decisions

### 6.1 Sales Order Status

The sales data contained both delivered and cancelled orders.

**Decision:** Delivered orders were used for primary product performance and demand analysis. Cancelled orders were kept separate to avoid treating cancelled transactions as completed sales.

### 6.2 Revenue Calculation

Sales line records included values with and without GST.

**Decision:** `line_total` was used as revenue because it excludes GST.

### 6.3 Slow-Moving and Dead Stock Identification

The available sales data allowed products to be ranked by quantity sold and order frequency, but did not provide sufficient evidence to confirm actual dead stock.

**Decision:** The analysis reported relative product rankings and did not label products as dead stock without inventory age and stock-level information.

### 6.4 ABC Classification

The cumulative revenue thresholds required careful handling for products crossing the 80% and 95% boundaries.

**Decision:** Boundary-crossing products were assigned to the category they brought to the threshold, ensuring that every product received a classification.

## 7. Sprint Deliverables

The Week 4 work produced the following deliverables:

- Product and sales data validation results.
- Product performance analysis.
- Fast-moving and slow-moving product comparisons.
- ABC / Pareto classification.
- Monthly demand analysis.
- Annual demand analysis.
- Product-level annual demand comparisons.
- Business findings and recommendations.
- Python-based analytical work.
- Week 4 analytical documentation.

## 8. Sprint Outcome

**Sprint Status: Completed**

The planned Week 4 analytical activities were completed using Python and Pandas.

The analysis provided an overview of product sales performance, revenue concentration, relative product movement, and historical demand patterns.

The detailed findings and limitations were documented to ensure that business recommendations remain supported by the available data.

## 9. Carry-Forward Notes

The following considerations may support subsequent project phases:

- Use actual inventory information when evaluating stock levels and dead stock.
- Consider product criticality and lead times alongside sales performance.
- Use historical demand patterns as an input for future inventory analysis.
- Preserve the completed Week 4 analysis and documentation.

These are carry-forward considerations, not additional Week 4 tasks.

## 10. Conclusion

Week 4 successfully completed the Product Analytics scope of Phase 2.

The sprint established a product-level understanding of sales performance and historical demand behavior. The completed analysis and documentation provide a foundation for the subsequent inventory and warehouse analytics activities.