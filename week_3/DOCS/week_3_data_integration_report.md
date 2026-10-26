# Week 3 Data Integration Report

## 1. Overview

This report documents the integration and relationship validation performed for the Heavy Supplier, Inventory & Warehouse Analytics project during Week 3.

The work focused on validating key fields, checking foreign-key relationships, examining join cardinality, identifying repeated identifiers, and reconciling sales order headers with their associated line items.

The objective was to establish reliable integration rules while preserving unresolved data-quality issues for further investigation.

## 2. Key Validation

Primary and composite keys were reviewed across the core datasets.

| Dataset | Key field(s) | Validation outcome |
|---|---|---|
| Customers | `customer_id` | Unique and non-null |
| Branches | `branch_id` | Unique and non-null |
| Products | `product_id` | Unique and non-null |
| Suppliers | `supplier_id` | Unique and non-null |
| Purchase order headers | `po_id` | Unique and non-null |
| Sales order headers | `so_id` | Unique and non-null |
| Inventory master | `product_id`, `branch_id` | Composite key unique |
| Purchase order lines | `po_id`, `line_number` | Composite key unique |
| Sales order lines | `so_id`, `line_number` | Composite key unique |
| Stock ledger | `movement_id` | Unique and non-null |
| Invoices | `invoice_id` | Repeated identifiers found |
| Payments | `payment_id` | Repeated identifiers found |

The invoice and payment identifier findings require careful interpretation. Repeated identifiers were not automatically classified as duplicate transactions because the associated records may contain different business information.

## 3. Relationship Validation

Foreign-key checks were performed across the reviewed relationships, including links between customers, branches, products, purchase orders, sales orders, invoices, payments, and stock movements.

The reviewed checks found no unmatched foreign-key values or null child keys in the relationships tested.

This confirms that the tested child records reference existing parent identifiers. It does not establish that every parent identifier is unique or that every relationship is one-to-one.

## 4. Join Cardinality Analysis

### 4.1 Sales Order Headers to Sales Order Lines

| Measure | Rows |
|---|---:|
| Sales order headers | 20,000 |
| Sales order lines | 130,402 |
| Rows after left join | 130,402 |
| Increase over header count | 110,402 |

The row increase is expected because each sales order may contain multiple line items. The join preserved the line-level grain rather than producing one row per order.

All 20,000 sales orders had associated sales lines.

### 4.2 Sales Order Headers to Invoices

| Measure | Result |
|---|---:|
| Sales order headers | 20,000 |
| Rows after join | 20,000 |
| Orders without invoices | 1,967 |
| Orders without invoices that were cancelled | 1,967 |

The orders without invoices were all cancelled. This pattern is consistent with the observed order statuses, although it does not independently establish the underlying business rule for invoice creation.

### 4.3 Invoices to Payments

| Measure | Rows |
|---|---:|
| Invoice records | 18,033 |
| Payment records | 19,257 |
| Rows after left join | 21,480 |
| Additional rows from join expansion | 3,447 |
| Increase relative to invoice rows | Approximately 19.11% |

The join produced more rows than the invoice table because invoice identifiers and payment relationships were not strictly one-to-one.

Additional validation results:

- Repeated invoice identifiers: 196.
- Extra invoice rows beyond one row per distinct repeated identifier group: 197.
- Repeated payment identifiers: 201.
- Extra payment rows beyond one row per distinct repeated identifier group: 202.
- Invoice identifiers with multiple payment rows: 2,530.
- Matching invoice-payment join rows: 19,678.
- Invoice records without matching payments: 1,802.

The 3,447 additional joined rows must not be described as confirmed duplicate transactions. Join expansion can result from multiple matching records on either side.

## 5. Sales Financial Reconciliation

Sales order line calculations were validated before aggregation.

| Validation | Result |
|---|---|
| `line_total` against quantity × unit price | No mismatches |
| `gst_amount` against line total × GST rate | No mismatches after rounding to two decimals |
| `line_grand_total` against line total + GST | No mismatches after rounding to two decimals |

Sales lines were then aggregated by `so_id` and joined to sales order headers using a one-to-one validation on the aggregated result.

| Reconciliation check | Result |
|---|---|
| Sales orders without lines | 0 |
| Order value mismatches | 0 |
| GST amount mismatches | 0 |
| Grand-total mismatches | 0 after rounding to two decimal places |

Tiny unrounded differences were attributable to floating-point precision rather than substantive financial discrepancies.

## 6. Integration Decisions

The following decisions were applied:

1. Preserve source records while investigating repeated identifiers.
2. Do not delete records solely because an identifier occurs more than once.
3. Use the correct data grain when joining headers, lines, invoices, and payments.
4. Aggregate line-level data to order level before comparing it with order-header totals.
5. Use explicit join validation where the expected relationship supports it.
6. Round financial comparisons to two decimal places to avoid treating floating-point artifacts as meaningful discrepancies.
7. Distinguish referential integrity from uniqueness and business-rule validity.

## 7. Limitations and Follow-up

The following issues remain unresolved:

- The business meaning of repeated invoice and payment identifiers needs confirmation.
- The reason for repeated identifiers cannot be established from key counts alone.
- The invoice-payment relationship should be interpreted using its observed cardinality rather than assumed to be one-to-one.
- No unsupported identifier corrections or transaction deletions were made.

These findings should be retained as data-quality investigation items for future project phases.

## 8. Conclusion

Week 3 integration checks established that the reviewed foreign-key relationships were valid for the tested records and that sales order headers reconciled with their aggregated line items.

The analysis also identified repeated invoice and payment identifiers and demonstrated that invoice-payment joins can expand row counts. These records were preserved, and the findings were documented without assuming that repeated identifiers represent duplicate transactions.

The integration results provide a foundation for subsequent product, inventory, supplier, and business-performance analysis.
