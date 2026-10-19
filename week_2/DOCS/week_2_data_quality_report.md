# Week 2 — Data Quality Assessment Report

## 1. Objective

The objective of Week 2 was to assess the quality and reliability of the CadetX Heavy Supplier, Inventory & Warehouse Analytics datasets before proceeding to deeper analysis. The assessment focused on missing values, exact duplicate rows, identifier uniqueness, relationship integrity, inventory limits, and stock-ledger balance consistency.

## 2. Datasets Assessed

Twelve primary datasets were reviewed.

| Dataset | Rows | Columns |
|---|---:|---:|
| Customers | 500 | 15 |
| Branches | 6 | 13 |
| Products | 30 | 23 |
| Suppliers | 8 | 12 |
| Inventory master | 180 | 9 |
| Purchase order headers | 24,000 | 10 |
| Purchase order lines | 155,495 | 9 |
| Sales order headers | 20,000 | 11 |
| Sales order lines | 130,402 | 9 |
| Stock ledger | 237,230 | 12 |
| Invoices | 18,033 | 10 |
| Payments | 19,257 | 5 |

## 3. Initial Missing-Value and Duplicate Checks

The initial scan found no missing values or exact duplicate rows in customers, branches, products, suppliers, inventory master, purchase order lines, sales order headers, sales order lines, invoices, or payments.

Exceptions were:

- **Purchase order headers:** 2,370 missing cells, all in `received_date`.
- **Stock ledger:** 360 missing cells, comprising 180 missing `previous_balance` values and 180 missing `expected_balance` values.

No exact duplicate rows were found in any of the 12 datasets.

## 4. Purchase Order Header Assessment

The purchase order header dataset contained 2,370 missing `received_date` values. All 2,370 records were associated with cancelled purchase orders.

### Decision
The missing dates were retained. A cancelled order may not have a receipt date, so filling these values without further evidence would introduce unsupported information.

## 5. Stock Ledger Missing Balances

The stock ledger contained 180 rows with missing `previous_balance` and `expected_balance` values.

All 180 rows were verified as the first movement within their respective product-branch histories. No rows with missing balances were found outside these first movements.

### Decision
The missing values were retained because the opening balances could not be established from the available records. They should not be replaced with zero or another assumed value without supporting evidence.

## 6. Invoice Identifier Assessment

The invoice dataset contained 18,033 rows and 17,836 unique invoice IDs.

| Occurrence pattern | Number of IDs |
|---|---:|
| IDs appearing once | 17,640 |
| IDs appearing twice | 195 |
| IDs appearing three times | 1 |

In total, 196 invoice IDs were repeated, affecting 393 records.

All invoice `so_id` values referred to existing sales orders, and each invoice `so_id` was unique. However, repeated invoice IDs created a risk of incorrect joins.

A join between sales order headers and invoices produced 20,000 rows, with 1,967 sales orders missing an invoice ID. All 1,967 were cancelled orders. No delivered order was found without an invoice.

Joining payments to invoices using the repeated invoice IDs increased the result from 19,257 payment records to 19,678 joined rows, creating 421 additional rows through join multiplication. Of the payment records, 417 used repeated invoice IDs across 194 distinct repeated invoice IDs; two repeated invoice IDs had no associated payments.

### Decision
Repeated invoice IDs were retained and flagged for further investigation. They were not automatically replaced because the available evidence did not establish the correct replacement identifiers. Invoice-to-payment reconciliation should be treated cautiously until these collisions are resolved.

## 7. Payment Identifier Assessment

The payment dataset contained 19,257 rows and 19,055 unique payment IDs.

| Occurrence pattern | Number of IDs |
|---|---:|
| IDs appearing once | 18,854 |
| IDs appearing twice | 200 |
| IDs appearing three times | 1 |

In total, 201 payment IDs were repeated, affecting 403 records. No exact duplicate payment rows were identified.

All 201 repeated payment IDs were linked to multiple distinct invoice IDs. For example, `PAY-361416` appeared three times with different invoice, date, amount, and payment-method details.

### Decision
The repeated IDs were retained and flagged. They were not treated as exact duplicate rows, and no replacement IDs were invented.

## 8. Inventory Master Assessment

The inventory master contained 180 records, with no missing values or exact duplicate rows.

Every record had `current_stock` greater than `max_stock`.

| Metric | Result |
|---|---:|
| Records assessed | 180 |
| Records where current stock exceeds maximum stock | 180 |
| Mean current stock | 107,240 |
| Minimum current stock | 88,853 |
| Maximum current stock | 121,013 |
| Mean maximum stock | 321.76 |
| Minimum maximum stock | 131 |
| Median maximum stock | 310.5 |
| Maximum maximum stock | 582 |
| Average current-stock-to-maximum-stock ratio | 385 |
| Minimum ratio | 177 |
| Maximum ratio | 854 |

Additional checks found no records where `opening_stock` exceeded `max_stock`, `reorder_level` or `safety_stock` exceeded `max_stock`, or `opening_stock` exceeded `current_stock`.

The anomaly appeared across all 30 products and all six branches. The available information did not establish whether the issue resulted from data generation, incompatible units, or undocumented field meanings.

### Decision
The values were preserved. No scaling, capping, or replacement was applied because the intended units and business rules had not been verified.

## 9. Stock Ledger Balance Assessment

The stock ledger contained 237,230 records. All movement IDs were unique, and no exact duplicate rows were found.

| Movement type | Records |
|---|---:|
| IN | 127,611 |
| OUT | 107,165 |
| ADJUSTMENT | 2,454 |

The movement reference types were consistent with the observed mapping:

- `IN` movements referenced purchase orders (`PO`).
- `OUT` movements referenced sales orders (`SO`).
- `ADJUSTMENT` movements referenced adjustments (`ADJ`).

Movement quantities were positive, and the foreign-key and date checks performed during the assessment were valid.

The existing mismatch flag identified 54,876 records, approximately 23.1% of the ledger.

### 9.1 Inbound and outbound movements

The ordinary inbound and outbound assessment included 234,611 movements with non-null previous balances.

- For `IN` movements, the expected relationship was previous balance plus movement quantity.
- For `OUT` movements, the expected relationship was previous balance minus movement quantity.

For these checked movements, the existing mismatch flags agreed with whether `running_balance` differed from `expected_balance`. No disagreements were found.

### 9.2 Sequential balance links

There were 237,050 movements after the first movement in each product-branch history. Every checked movement's `previous_balance` matched the preceding movement's `running_balance`.

This supports the continuity of the recorded sequence, but it does not independently establish that every recorded balance is correct.

### 9.3 Adjustment movements

Among 2,439 adjustment records with non-null previous balances:

| Observed balance-change pattern | Records |
|---|---:|
| Balance increased by the movement quantity | 732 |
| Balance decreased by the movement quantity | 757 |
| Other balance change | 948 |
| No balance change | 2 |

All 2,439 records referenced adjustments and had unique adjustment reference IDs. Fifteen adjustment rows had null previous balances; these were among the first movements in their respective product-branch histories.

For adjustments, `expected_balance` appeared to equal `previous_balance`, even when `running_balance` differed. The intended adjustment calculation and mismatch-flag semantics were not documented clearly enough to confirm whether this was correct.

### Decision
No stock-ledger balances were changed. The unresolved adjustment behavior was preserved for further investigation. The original `stock_ledger` dataset remained the source of truth for diagnostic checks; the intermediate `ledger_test` DataFrame was not used as the source for corrections.

## 10. Working Copies and Validation

Working copies of the 12 primary datasets were created in the `cleaned_tables` dictionary.

Validation confirmed:

- All working-copy row counts matched the original row counts.
- All working-copy missing-value counts matched the original missing-value counts.
- No changes to source values were made as part of this preservation step.

These checks confirm structural preservation, not that every business rule or value in the source data is correct.

No corrected CSV exports or reusable cleaning script were produced during this stage.

## 11. Limitations

The assessment identified several issues whose causes could not be confirmed from the available data and documentation:

- The meaning and units of the inventory stock fields.
- The reason for repeated invoice and payment identifiers.
- The intended rules for calculating adjustment balances and mismatch flags.
- The correctness of historical opening balances where the ledger begins without a prior recorded movement.

These issues require additional documentation or confirmation before reliable corrections can be made.

## 12. Conclusion

Week 2 established a data-quality baseline across the 12 primary datasets. The assessment identified missing receipt dates associated with cancelled purchase orders, first-movement balance gaps, repeated invoice and payment identifiers, a widespread inventory-limit anomaly, and stock-ledger balance issues.

The approach prioritized traceability: unsupported values were not invented, repeated identifiers were not silently changed, and the original data was preserved. These findings should inform the assumptions and validation requirements of subsequent analysis.
