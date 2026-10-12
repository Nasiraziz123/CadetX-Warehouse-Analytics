# Data Quality Log — Week 1

## 1. Project Information

- **Project:** Heavy Supplier, Inventory & Warehouse Analytics
- **Programme:** CadetX Virtual Work Experience
- **Phase:** Week 1 — Data Understanding and Quality Assessment
- **Purpose:** To inspect the available datasets, check data quality, validate key relationships, and document issues requiring further investigation.

## 2. Data Quality Checks Performed

The following checks were performed on the available datasets:

- Table dimensions, column names, and data types
- Missing values and exact duplicate rows
- Uniqueness of primary and composite keys
- Foreign-key relationships between related tables
- Date parsing and basic date logic
- Numeric validation, including negative values and stock thresholds
- Financial calculations and consistency between order, invoice, and payment records
- Preliminary stock-ledger running-balance validation

## 3. Summary of Findings

### 3.1 Checks Passed

- Customer IDs, branch IDs, product IDs, purchase order IDs, sales order IDs, and stock movement IDs were unique in their respective tables.
- Customer, supplier, branch, product, purchase-order, sales-order, and stock-ledger relationship checks found no invalid references in the checks performed.
- Purchase order and sales order line tables had no duplicate combinations of order ID and line number.
- Date conversion checks did not identify invalid dates in the tables examined.
- Purchase-order and sales-order financial totals were internally consistent within a small floating-point tolerance.
- Purchase-order and sales-order line calculations were internally consistent within the tested tolerances.
- No exact duplicate rows or missing values were found in several examined tables. Missing values were present where expected in some business contexts, such as the received date of cancelled purchase orders.

### 3.2 Inventory Master — Current Stock Values

**Finding:** All 180 records had `current_stock` greater than `max_stock`.

This may indicate a data-quality issue, a difference in units or definitions, or a problem in how the values were generated.

**Action required:** Confirm the meaning and units of `current_stock` and `max_stock` using the official field documentation or clarification from the project team. Preserve the original values until the issue is understood.

### 3.3 Invoice Identifiers

**Finding:** The invoice table contained 18,033 rows but only 17,836 unique invoice IDs. Repeated invoice IDs were associated with different sales orders or other record details.

**Potential impact:** Repeated identifiers may cause incorrect joins, duplicated totals, and unreliable payment reconciliation.

**Action required:** Investigate the invoice ID generation and uniqueness rules. Do not delete or combine records without confirming the intended business rules.

### 3.4 Payment Identifiers

**Finding:** The payments table contained 19,257 rows but only 19,055 unique payment IDs. Repeated payment IDs appeared against different invoice IDs or transaction details.

**Potential impact:** Duplicate identifiers may distort payment totals and invoice-to-payment reconciliation.

**Action required:** Confirm whether payment IDs are intended to be unique. Investigate repeated IDs before calculating definitive outstanding balances.

### 3.5 Stock Ledger Running Balances

**Finding:** A preliminary running-balance check identified 54,876 mismatches under the tested transaction-ordering assumption.

**Limitation:** Multiple movements can occur on the same date, and the available fields do not establish a definitive transaction sequence or the direction of adjustments. Therefore, these mismatches are not confirmed errors.

**Action required:** Confirm transaction sequencing, adjustment rules, and the meaning of `running_balance`. Repeat the validation once the business rules are known.

### 3.6 Cancelled Sales Orders and Delivery Dates

**Finding:** All 1,967 cancelled sales orders had delivery dates.

**Action required:** Confirm whether delivery dates on cancelled orders are expected by the business process. Do not classify these records as incorrect without clarification.

### 3.7 Purchase Order Delivery Timing

**Finding:** Among received purchase orders, 3,267 records had a received date later than the expected delivery date.

**Interpretation:** These records may represent late deliveries rather than data-entry errors.

**Action required:** Retain this finding for supplier lead-time and delivery-performance analysis in a later project phase.

## 4. Additional Data Preparation Observations

- Warehouse capacity values in the branches table are stored as text with units, such as square feet.
- Product dimensions are stored as text, for example `40x25x25`.
- Some identifier-like fields, such as postal codes, should be reviewed before deciding on appropriate data types.
- The official field documentation was not available during this assessment, so some field meanings and business rules remain unconfirmed.

These observations are not automatically data-quality errors. Any required transformations should be documented and justified before implementation.

## 5. Data Handling Decisions

- Preserve the original dataset files.
- Do not remove duplicate identifiers or alter stock values without investigating their causes.
- Keep findings separate from confirmed errors.
- Document assumptions and unresolved questions.
- Revalidate affected tables after the relevant business rules are confirmed.

## 6. Week 1 Conclusion

The initial profiling established the structure of the available datasets and identified several relationships and calculation checks that passed. It also highlighted issues requiring clarification, particularly inventory stock values, repeated invoice and payment identifiers, and stock-ledger running balances.

The next phase should focus on completing the initial data dictionary, confirming unresolved business rules, and defining suitable supply-chain and inventory KPIs.