# Week 4 — Product Analytics Report

## 1. Introduction

This report documents the product analytics activities completed during Week 4 of the CadetX Heavy Supplier, Inventory & Warehouse Analytics project.

The purpose of this analysis was to evaluate product-level sales performance, understand the contribution of individual products to total revenue, and compare product movement using sales quantity and order frequency.

The analysis was performed using Python and Pandas.

## 2. Datasets Used

Three datasets were used for the analysis.

| Dataset | Records | Columns | Description |
|---|---:|---:|---|
| `products.csv` | 30 | 23 | Product details, categories, pricing, and inventory-related attributes |
| `sales_orders_header.csv` | 20,000 | 11 | Order-level details, dates, statuses, and financial information |
| `sales_orders_lines.csv` | 130,402 | 9 | Product-level transaction quantities and sales values |

## 3. Data Understanding and Validation

Before performing product analytics, the datasets were examined to understand their structure and verify their data quality.

### 3.1 Data Quality Checks

The following validation checks were performed:

- Dataset dimensions and column inspection.
- Data type examination.
- Missing-value checks.
- Exact duplicate-row checks.
- Primary-key uniqueness checks.
- Product and sales-order relationship validation.
- Duplicate sales-order line validation.
- Identification of orders without corresponding sales lines.
- Date conversion and validation.

### 3.2 Validation Results

| Validation Check | Result |
|---|---|
| Missing values | None found |
| Exact duplicate rows | None found |
| Unique product IDs | 30 |
| Unique sales-order IDs | 20,000 |
| Missing product references in sales lines | 0 |
| Missing sales-order references in sales lines | 0 |
| Duplicate (`so_id`, `line_number`) combinations | 0 |
| Orders without sales lines | 0 |
| Invalid order dates after conversion | 0 |

All performed validation checks passed.

## 4. Analytical Dataset Preparation

The sales-order header dataset was joined with the sales-order lines dataset using `so_id`.

The purpose of this merge was to bring order dates and order statuses into the product-level transaction data.

The merge was validated as a many-to-one relationship.

The resulting analytical dataset was separated into:

- Delivered sales.
- Cancelled sales.

### 4.1 Sales Status Summary

| Metric | Result |
|---|---:|
| Total sales lines | 130,402 |
| Delivered sales lines | 117,656 |
| Cancelled sales lines | 12,746 |
| Delivered orders | 18,033 |
| Cancelled orders | 1,967 |
| Delivered quantity | 1,234,939 |
| Cancelled quantity | 133,595 |
| Delivered sales value | 22,958,987,430 |
| Cancelled sales value | 2,488,405,130 |

### 4.2 Analytical Decisions

The following decisions were applied throughout the analysis:

1. Delivered orders were used as the primary basis for product performance.
2. Cancelled orders were kept separate from delivered sales.
3. `line_total` was used as sales revenue because it excludes GST.
4. Product-level metrics were calculated using the delivered sales dataset.

These decisions ensure that the product performance results reflect completed sales rather than combining delivered and cancelled transactions.

## 5. Product Performance Analysis

Product performance was evaluated across all 30 products.

The following metrics were calculated:

- Total quantity sold.
- Total revenue.
- Number of distinct orders containing each product.
- Average selling price.
- Revenue contribution percentage.

Products were ranked by total revenue to identify the largest contributors to delivered sales.

### 5.1 Top 10 Products by Revenue

| Rank | Product ID | Product Name | Quantity Sold | Revenue | Orders | Revenue Contribution |
|---:|---|---|---:|---:|---:|---:|
| 1 | P015 | Engine Block EB-600 | 40,815 | 4,856,985,000 | 3,411 | 21.16% |
| 2 | P014 | Transmission Assembly TA-800 | 40,574 | 3,387,929,000 | 3,462 | 14.76% |
| 3 | P021 | Boom Cylinder BC-400 | 41,864 | 1,934,116,800 | 3,481 | 8.42% |
| 4 | P019 | Swing Motor SWM-350 | 41,543 | 1,653,411,400 | 3,476 | 7.20% |
| 5 | P004 | Track Chain TC-45 | 40,891 | 1,627,461,800 | 3,392 | 7.09% |
| 6 | P010 | Turbocharger TB-900 | 42,292 | 1,475,990,800 | 3,542 | 6.43% |
| 7 | P011 | Hydraulic Cylinder HC-200 | 42,093 | 1,161,766,800 | 3,595 | 5.06% |
| 8 | P001 | Hydraulic Pump HP-300 | 41,304 | 1,011,948,000 | 3,499 | 4.41% |
| 9 | P030 | Fuel Pump FP-350 | 41,595 | 910,930,500 | 3,509 | 3.97% |
| 10 | P022 | Control Valve CV-75 | 41,297 | 697,919,300 | 3,493 | 3.04% |

### 5.2 Key Observations

**Revenue concentration**

- P015 Engine Block EB-600 was the highest-revenue product, contributing 21.16% of total delivered revenue.
- P014 Transmission Assembly TA-800 ranked second, contributing 14.76%.
- Together, these two products contributed approximately 35.92% of total delivered revenue.
- The top ten products accounted for approximately 81.54% of total delivered revenue.

**Quantity versus revenue**

The highest-revenue product was not the highest-quantity product.

P015 generated the highest revenue, while P010 recorded the highest quantity among the top ten products. This demonstrates that sales quantity and revenue contribution measure different aspects of product performance.

## 6. Fast-Moving and Slow-Moving Product Comparison

Products were compared using two indicators:

1. Total quantity sold.
2. Number of distinct orders containing each product.

These indicators provide a relative view of product movement based on historical delivered sales.

### 6.1 Top 10 Products by Quantity Sold

| Rank | Product ID | Product Name | Quantity Sold | Orders |
|---:|---|---|---:|---:|
| 1 | P029 | Pressure Sensor PS-90 | 42,702 | 3,506 |
| 2 | P010 | Turbocharger TB-900 | 42,292 | 3,542 |
| 3 | P007 | Hydraulic Hose HH-60 | 42,156 | 3,534 |
| 4 | P011 | Hydraulic Cylinder HC-200 | 42,093 | 3,595 |
| 5 | P021 | Boom Cylinder BC-400 | 41,864 | 3,481 |
| 6 | P006 | Alternator ALT-500 | 41,843 | 3,539 |
| 7 | P016 | Radiator RD-250 | 41,770 | 3,544 |
| 8 | P003 | Air Filter AF-120 | 41,712 | 3,554 |
| 9 | P030 | Fuel Pump FP-350 | 41,595 | 3,509 |
| 10 | P012 | Brake Pad BP-40 | 41,549 | 3,517 |

P029 Pressure Sensor PS-90 recorded the highest quantity sold, with 42,702 units.

### 6.2 Bottom 10 Products by Quantity Sold

| Product ID | Product Name | Quantity Sold | Orders |
|---|---|---:|---:|
| P027 | O-Ring Set OR-50 | 40,870 | 3,476 |
| P015 | Engine Block EB-600 | 40,815 | 3,411 |
| P018 | Wheel Rim WR-24 | 40,752 | 3,466 |
| P014 | Transmission Assembly TA-800 | 40,574 | 3,462 |
| P009 | Starter Motor SM-700 | 40,547 | 3,412 |
| P005 | Fuel Injector FI-220 | 40,480 | 3,454 |
| P026 | Grease Cartridge GC-5 | 40,407 | 3,428 |
| P023 | Idler Wheel IW-55 | 40,276 | 3,402 |
| P013 | Seal Kit SK-15 | 39,927 | 3,421 |
| P024 | Track Roller TR-60 | 39,486 | 3,401 |

P024 Track Roller TR-60 recorded the lowest quantity sold, with 39,486 units.

### 6.3 Order Frequency Comparison

Order frequency was also used to compare product movement.

- Highest order frequency: P011 Hydraulic Cylinder HC-200, with 3,595 orders.
- Lowest order frequency: P004 Track Chain TC-45, with 3,392 orders.

The results show that the product with the highest order frequency was not necessarily the product with the highest quantity sold.

### 6.4 Interpretation

The difference between the highest and lowest product quantities was relatively small compared with the overall sales volume.

All 30 products recorded substantial sales activity during the analysis period.

Therefore, these rankings identify relatively higher- and lower-performing products, but they do not establish that any product is genuinely dead stock or has inadequate inventory movement.

Actual dead-stock identification would require additional information, such as current stock levels, inventory age, last movement dates, and stock history.

## 7. Business Findings

The product analytics produced the following findings:

1. Product revenue was concentrated among a relatively small group of products.
2. P015 Engine Block EB-600 was the largest revenue contributor.
3. P029 Pressure Sensor PS-90 recorded the highest quantity sold.
4. P011 Hydraulic Cylinder HC-200 appeared in the highest number of distinct orders.
5. P024 Track Roller TR-60 had the lowest quantity sold among the 30 products.
6. P004 Track Chain TC-45 had the lowest order frequency.
7. Quantity sold, order frequency, and revenue provide different perspectives on product performance.

## 8. Business Recommendations

Based on the findings:

- Monitor high-revenue products closely because changes in their performance can have a substantial effect on total sales.
- Evaluate products using revenue, quantity, and order frequency together rather than relying on one metric.
- Review relatively lower-performing products alongside inventory availability and product criticality before making stock-related decisions.
- Use historical sales performance as one input for future product planning.
- Combine sales information with inventory records before making decisions about dead stock or stock reduction.

## 9. Analysis Limitations

The following limitations should be considered:

- The primary product performance analysis used delivered orders only.
- Revenue was calculated using `line_total`, excluding GST.
- Product movement rankings are relative comparisons within the dataset.
- Sales quantity and order frequency do not directly measure inventory turnover.
- Actual dead stock cannot be confirmed without inventory quantities and stock-age information.
- Revenue contribution does not represent profit contribution.

## 10. Conclusion

Week 4 product analytics evaluated all 30 products using delivered sales data.

The analysis identified leading revenue contributors, compared product quantity and order frequency, and highlighted differences between product sales volume and financial contribution.

The results show that product performance should be evaluated through multiple indicators. They also provide a foundation for further inventory-related analysis, where sales performance can be considered alongside actual stock information and inventory characteristics.