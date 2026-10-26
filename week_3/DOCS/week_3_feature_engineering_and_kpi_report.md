# Week 3 Feature Engineering and KPI Report

## 1. Overview

This report documents the inventory, sales order, product, and customer features developed during Week 3 of the Heavy Supplier, Inventory & Warehouse Analytics project.

The work establishes initial KPI baselines, validates derived features, and records important interpretation limits for future analysis.

## 2. Inventory Feature Engineering

### 2.1 Dataset Overview

The inventory master contains 180 product-branch records covering 30 products across 6 branches.

The product-branch combination was validated as a unique key.

### 2.2 Derived Features

The inventory analysis included:

- `stock_to_max_ratio`: current stock divided by recorded maximum stock.
- `above_max_stock_flag`: indicates whether current stock exceeds recorded maximum stock.
- `below_reorder_level_flag`: indicates whether current stock is below the recorded reorder level.
- `units_above_max`: current stock minus maximum stock.
- `units_above_reorder`: current stock minus reorder level.

The existing stock-to-maximum ratio was validated against its formula.

### 2.3 Initial Inventory KPIs

| KPI | Result |
|---|---:|
| Inventory records | 180 |
| Unique products | 30 |
| Unique branches | 6 |
| Records above recorded maximum stock | 180 (100%) |
| Records below reorder level | 0 (0%) |
| Records at or below reorder level | 0 (0%) |
| Duplicate product-branch combinations | 0 |

### 2.4 Branch-Level Overview

| Branch | Inventory records | Average current stock | Average maximum stock | Records above maximum |
|---|---:|---:|---:|---:|
| AHM001 | 30 | 105,166.40 | 323.00 | 30 |
| CHN001 | 30 | 107,808.17 | 321.40 | 30 |
| DEL001 | 30 | 109,622.33 | 324.80 | 30 |
| HYD001 | 30 | 108,176.37 | 314.57 | 30 |
| KOL001 | 30 | 104,126.83 | 361.53 | 30 |
| PUN001 | 30 | 108,542.10 | 285.23 | 30 |

### 2.5 Interpretation and Limitations

All 180 inventory records have current stock above the recorded maximum stock. The pattern appears across every branch.

The recorded threshold fields are internally consistent: safety stock does not exceed reorder level, and neither reorder level nor safety stock exceeds maximum stock in the reviewed records.

However, the current-stock values are much larger than the recorded thresholds. Because the field definitions, units, and source-generation rules have not been confirmed, this pattern is documented as an unresolved data-quality concern. It is not sufficient evidence by itself to conclude that physical overstock exists.

No unsupported stock corrections were applied.

## 3. Sales Order Feature Engineering

### 3.1 Dataset Overview

The sales order header dataset contains 20,000 records. The sales order line dataset contains 130,402 records.

Derived header features include:

- `delivery_days`: difference between delivery date and order date.
- `order_year`: year extracted from the order date.
- `order_month`: month extracted from the order date.

### 3.2 Delivery Duration

| Measure | Result |
|---|---:|
| Orders analyzed | 20,000 |
| Average recorded delivery duration | 8.06 days |
| Median recorded delivery duration | 8 days |
| Minimum recorded duration | 0 days |
| Maximum recorded duration | 15 days |
| Missing durations | 0 |
| Negative durations | 0 |

The recorded durations were non-negative and complete in the reviewed dataset.

**Limitation:** Cancelled orders also have recorded delivery dates. Their date differences may be placeholders and must not be interpreted as actual completed-delivery performance. The figures above describe recorded date differences across all orders, not verified delivery service levels.

### 3.3 Sales Line Calculation Validation

| Validation | Result |
|---|---|
| Line total = quantity × unit price | No mismatches |
| GST amount = line total × GST rate | No mismatches after rounding |
| Line grand total = line total + GST amount | No mismatches after rounding |

The two recorded GST rates were:

| GST rate | Number of order lines |
|---|---:|
| 18% | 56,676 |
| 28% | 73,726 |

### 3.4 Header-to-Line Reconciliation

Sales order lines were aggregated by order ID and compared with the sales order headers.

| Reconciliation measure | Result |
|---|---:|
| Orders without line items | 0 |
| Order value mismatches | 0 |
| GST amount mismatches | 0 |
| Grand-total mismatches | 0 after rounding to two decimals |

These results indicate that the recorded header totals reconcile with the aggregated line totals under the tested calculations.

## 4. Product-Level Analytics

### 4.1 Features Created

Product-level aggregation produced the following features:

- `total_quantity_sold`
- `total_sales_value`
- `total_gst_amount`
- `total_sales_including_gst`
- `order_line_count`
- `average_line_value`

The product aggregation contains 30 unique products and no missing product IDs.

### 4.2 Initial Product KPIs

| KPI | Result |
|---|---:|
| Products analyzed | 30 |
| Recorded quantity across order lines | 1,368,534 |
| Recorded sales value before GST | 25,447,392,560.00 |
| Recorded GST amount | 6,977,361,995.80 |
| Recorded value including GST | 32,424,754,555.80 |
| Sales order lines | 130,402 |

The product-level quantity and order-line counts reconcile with the source sales lines.

### 4.3 Leading Products by Recorded Quantity

| Product ID | Recorded quantity | Recorded sales value before GST |
|---|---:|---:|
| P029 | 47,066 | 185,910,700.00 |
| P010 | 46,964 | 1,639,043,600.00 |
| P006 | 46,731 | 523,387,200.00 |
| P011 | 46,612 | 1,286,491,200.00 |
| P007 | 46,468 | 67,378,600.00 |

### 4.4 Leading Products by Recorded Sales Value

| Product ID | Recorded sales value before GST | Recorded quantity |
|---|---:|---:|
| P015 | 5,381,418,000.00 | 45,222 |
| P014 | 3,760,422,500.00 | 45,035 |
| P021 | 2,142,016,800.00 | 46,364 |
| P019 | 1,829,645,800.00 | 45,971 |
| P004 | 1,813,885,000.00 | 45,575 |

**Interpretation note:** These aggregates include cancelled orders. They represent recorded order activity, not confirmed completed sales or recognized revenue.

## 5. Customer-Level Analytics

### 5.1 Features Created

Customer analysis included:

- Total order count.
- Aggregated order value, GST, and grand total.
- Delivered and cancelled order counts.
- Total orders per customer.
- Customer-level cancellation rate.

The customer analytics output contains 500 customers with unique customer IDs and no missing values in the reviewed feature set.

### 5.2 Order Status Baseline

| Measure | Result |
|---|---:|
| Customers analyzed | 500 |
| Total orders | 20,000 |
| Delivered orders | 18,033 |
| Cancelled orders | 1,967 |
| Overall cancellation rate | 9.84% |
| Overall delivered-status rate | Approximately 90.17% |

Customer-level order counts and cancellation counts reconcile with the source sales order records.

### 5.3 Customer Cancellation Rate Distribution

| Measure | Result |
|---|---:|
| Mean customer-level cancellation rate | 9.83% |
| Median customer-level cancellation rate | 10.00% |
| Minimum customer-level cancellation rate | 0.00% |
| Maximum customer-level cancellation rate | 25.00% |
| Standard deviation | 4.59 percentage points |

The mean of individual customer cancellation rates differs from the overall order-weighted cancellation rate because customers have different numbers of orders.

### 5.4 Customers with the Highest Recorded Cancellation Rates

| Customer ID | Cancelled orders | Total orders | Cancellation rate |
|---|---:|---:|---:|
| C0137 | 7 | 28 | 25.00% |
| C0135 | 10 | 45 | 22.22% |
| C0388 | 7 | 34 | 20.59% |
| C0036 | 8 | 39 | 20.51% |
| C0202 | 7 | 35 | 20.00% |

These are descriptive results from the recorded order statuses. They do not explain why the orders were cancelled.

### 5.5 Cancellation Rate by Customer Type

| Customer type | Customers | Orders | Cancelled orders | Overall cancellation rate within type |
|---|---:|---:|---:|---:|
| Government | 114 | 4,551 | 476 | 10.46% |
| Fleet Owner | 95 | 3,834 | 377 | 9.83% |
| Corporate | 104 | 4,064 | 392 | 9.65% |
| Retail | 88 | 3,535 | 339 | 9.59% |
| Dealer | 99 | 4,016 | 383 | 9.54% |

The overall cancellation rate across all orders is approximately 9.84%.

The customer-type comparison is descriptive. Further analysis would be required to determine whether the observed differences are meaningful and what factors may explain them.

## 6. Reconciliation and Quality Checks

The following checks were completed on the reviewed analytical outputs:

- Inventory feature output: 180 records.
- Sales order feature output: 20,000 records.
- Product feature output: 30 records.
- Customer cancellation feature output: 500 records.
- Customer analytics output: 500 records.
- No missing values were found in the reviewed feature outputs.
- Key uniqueness checks passed for the reviewed output grains.
- Product quantities and order-line counts reconciled with source sales lines.
- Customer order and cancellation counts reconciled with sales order headers.
- Sales order header totals reconciled with aggregated line totals.

## 7. Analytical Decisions and Limitations

1. No unsupported source-value corrections were made.
2. Recorded monetary totals include cancelled orders and are not presented as completed sales revenue.
3. Recorded delivery-date differences for cancelled orders are not treated as completed-delivery performance.
4. The inventory threshold pattern remains unresolved pending clarification of field definitions and units.
5. Customer cancellation rates describe observed order statuses and do not establish causes.
6. Product and customer rankings are descriptive and depend on the current recorded data.
7. Small unrounded monetary differences were treated as floating-point precision artifacts when rounded comparisons reconciled.

## 8. Conclusion

Week 3 produced validated inventory, sales order, product, and customer features alongside initial KPI baselines.

The financial calculations and sales header-to-line reconciliation passed the tested checks. Product and customer aggregates reconciled with their source records. The analysis also identified an inventory threshold pattern requiring clarification and established important limitations around cancelled orders and recorded monetary totals.

These outputs provide a documented foundation for subsequent supply-chain and business-performance analysis.
