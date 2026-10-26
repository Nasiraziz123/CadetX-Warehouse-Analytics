# Week 3 Sprint Notes — Data Integration, Feature Engineering & Initial KPIs

## 1. Sprint Overview

**Project:** Heavy Supplier, Inventory & Warehouse Analytics  
**Sprint:** Week 3  
**Phase:** Foundation & Exploration  
**Primary focus:** Data integration, relationship validation, feature engineering, reconciliation, and initial KPI baselines.

## 2. Sprint Objectives

- Validate key fields and relationships across the project datasets.
- Assess join cardinality and identify potential row multiplication.
- Engineer inventory, sales, product, and customer analytical features.
- Reconcile sales order headers with sales order lines.
- Calculate initial sales, inventory, product, and customer KPIs.
- Preserve unresolved data-quality concerns rather than applying unsupported corrections.

## 3. Work Completed

### 3.1 Data Integration and Relationship Validation

- Validated primary and composite keys across the main datasets.
- Checked foreign-key relationships and unmatched records.
- Reviewed joins between sales orders, sales order lines, invoices, and payments.
- Identified repeated invoice and payment identifiers.
- Confirmed that one-to-many relationships can increase joined row counts and require careful interpretation.

### 3.2 Inventory Feature Engineering

- Reviewed the 180 product-branch inventory records.
- Validated the existing `stock_to_max_ratio` calculation against `current_stock / max_stock`.
- Created and reviewed stock-threshold indicators and units-above-threshold calculations.
- Confirmed that all 180 records exceed the recorded `max_stock` value.
- Preserved this pattern as an unresolved data-quality concern because the field definitions and units have not been confirmed.

### 3.3 Sales Order Analysis and Reconciliation

- Created sales order features including `delivery_days`, `order_year`, and `order_month`.
- Validated sales line calculations for line value, GST, and grand total.
- Aggregated sales order lines and reconciled them with sales order header totals.
- Confirmed that all 20,000 sales orders have associated sales lines.
- Found no discrepancies in the validated financial calculations after rounding monetary values to two decimal places.

### 3.4 Product Analytics

- Created product-level aggregates for quantity, sales value, GST, total value including GST, order-line count, and average line value.
- Confirmed that the product-level results cover all 30 products.
- Reconciled aggregate quantities and order-line counts against the source sales lines.

### 3.5 Customer Analytics

- Created customer-level order counts and monetary aggregates.
- Calculated delivered and cancelled order counts and customer cancellation rates.
- Integrated cancellation metrics with customer profile information.
- Confirmed that customer-level order and cancellation totals reconcile with the sales order source data.

### 3.6 Initial KPI Baselines

Calculated initial measures for:
- Order volume and order status rates.
- Recorded order value, GST, and grand total.
- Inventory threshold indicators.
- Product quantity and recorded sales value.
- Customer order activity and cancellation rates.

These are initial analytical baselines and may require refinement as later project phases introduce additional business rules.

## 4. Initial Results

| Measure | Initial result |
|---|---:|
| Sales orders | 20,000 |
| Delivered orders | 18,033 |
| Cancelled orders | 1,967 |
| Delivered-status rate | Approximately 90.17% |
| Cancellation rate | Approximately 9.84% |
| Sales order lines | 130,402 |
| Products analyzed | 30 |
| Inventory product-branch records | 180 |
| Customers analyzed | 500 |
| Recorded order value before GST | 25,447,392,560.00 |
| Recorded GST amount | 6,977,361,995.80 |
| Recorded grand total including GST | 32,424,754,555.80 |

**Interpretation note:** The monetary totals include cancelled orders. They represent recorded order activity and must not be interpreted as confirmed completed sales revenue.

## 5. Data Quality and Validation Outcomes

- The reviewed analytical outputs passed the recorded missing-value and key-uniqueness checks.
- Sales line calculations reconciled with their underlying formulas.
- Sales order header totals reconciled with aggregated sales line totals.
- Customer order and cancellation counts reconciled with the source sales orders.
- Repeated invoice and payment identifiers were retained for investigation rather than deleted or replaced.
- The inventory threshold pattern remains unresolved and requires confirmation of source definitions and units.

## 6. Decisions and Limitations

1. No unsupported changes were made to source values.
2. Repeated identifiers were not automatically treated as duplicate transactions.
3. Join row increases were assessed in the context of relationship cardinality.
4. Cancelled orders were not treated as completed sales.
5. Recorded inventory values above `max_stock` were not interpreted as confirmed physical overstock.
6. Delivery dates associated with cancelled orders were not treated as reliable completed-delivery performance.
7. Very small differences in aggregated monetary values were treated as floating-point precision effects when they disappeared after rounding to two decimal places.

## 7. Sprint Status

**Technical analysis:** Core Week 3 integration, feature engineering, reconciliation, and initial KPI calculations completed.

**Documentation:** In progress.

**Next steps:** Complete the Week 3 data integration report, feature engineering and KPI report, and Week 3 README. Perform a final documentation and repository review before preparing the sprint submission.

## 8. Scope Control

Week 1 and Week 2 files remain unchanged. Week 4 work has not started.
