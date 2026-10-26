# Week 3 — Data Integration, Feature Engineering & Initial KPIs

## Overview

Week 3 focuses on integrating the supply-chain datasets, validating relationships between tables, engineering analytical features, and calculating initial business KPIs for the **Heavy Supplier, Inventory & Warehouse Analytics** project.

This work builds on the data understanding and data quality investigations from the previous weeks. The objective is to establish a reliable analytical foundation without modifying earlier-week documentation or making unsupported assumptions about the data.

## Objectives

- Integrate related datasets using their primary and foreign keys.
- Validate table relationships and investigate join cardinality.
- Reconcile sales order headers with their corresponding order lines.
- Investigate invoice and payment relationships.
- Engineer date-based and business-oriented analytical features.
- Calculate initial sales, customer, cancellation, and inventory KPIs.
- Validate calculations and document limitations that may affect interpretation.

## Week 3 Documentation

The detailed reports are available below.

| Document | Description |
|---|---|
| [Sprint Notes](DOCS/week_3_sprint_notes.md) | Sprint objectives, completed tasks, key findings, decisions, and status. |
| [Data Integration Report](DOCS/week_3_data_integration_report.md) | Key validation, foreign-key checks, join cardinality, financial reconciliation, and invoice-payment relationship findings. |
| [Feature Engineering and KPI Report](DOCS/week_3_feature_engineering_and_kpi_report.md) | Engineered features, initial KPIs, product and customer analysis, cancellation patterns, and quality checks. |

## Initial Findings

The Week 3 analysis established the following baseline:

| Metric | Result |
|---|---:|
| Sales orders | 20,000 |
| Orders marked delivered | 18,033 |
| Orders marked cancelled | 1,967 |
| Delivery-status rate | 90.17% |
| Cancellation rate | 9.84% |
| Sales order lines | 130,402 |
| Products | 30 |
| Customers | 500 |
| Inventory records | 180 |

The delivery-status rate describes the recorded order statuses; it should not be interpreted as a fully validated operational delivery-performance measure.

## Data Integration and Validation

The integration work examined key uniqueness, foreign-key relationships, join cardinality, sales order headers and lines, and invoice-payment relationships.

Key outcomes included:

- Reviewed foreign-key relationships had no unmatched or null child keys.
- Sales order headers reconciled with their order lines.
- Order-line financial calculations reconciled with the corresponding header totals after rounding to two decimal places.
- Invoice-payment joins produced more rows than invoice records, requiring careful interpretation of one-to-many relationships rather than automatically treating the additional rows as duplicates.

See the [Data Integration Report](DOCS/week_3_data_integration_report.md) for detailed results.

## Feature Engineering and KPI Analysis

The analysis introduced date-based sales features and calculated initial metrics covering:

- Order status and cancellation patterns.
- Product quantities and recorded sales values.
- Customer-level cancellation rates.
- Cancellation rates by customer type.
- Inventory stock levels relative to recorded maximum-stock and reorder thresholds.
- Date differences between recorded order and delivery dates.

These metrics provide an initial analytical baseline for subsequent investigation.

## Important Limitations

- Recorded sales totals include cancelled orders. They must **not** be interpreted as completed sales revenue.
- Date differences include cancelled orders and do not independently establish actual delivery performance.
- All 180 reviewed inventory records were above their recorded maximum-stock thresholds. This is a data pattern requiring investigation, not proof of physical overstock.
- Invoice-payment join expansion reflects relationship cardinality and requires further investigation before conclusions are drawn about payment completeness or duplication.
- No unsupported corrections were made merely to force the data to match expected business behavior.

## Week 3 Status

Week 3 documentation covers the sprint, data integration, feature engineering, initial KPIs, validation outcomes, and known limitations.

The next phase should follow the assigned project roadmap and build on these findings. Week 4 work has not been included in this README.

## Project Structure

```text
week_3/
├── README.md
└── DOCS/
    ├── week_3_sprint_notes.md
    ├── week_3_data_integration_report.md
    └── week_3_feature_engineering_and_kpi_report.md
```
