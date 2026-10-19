# Week 2 — Data Quality Assessment

## Overview
Week 2 focused on assessing the quality, consistency, and reliability of the CadetX Heavy Supplier, Inventory & Warehouse Analytics datasets. The work covered missing values, repeated identifiers, inventory anomalies, stock-ledger balance checks, and basic relationship validation.

## Scope
The assessment covered 12 primary datasets:

- Customers
- Branches
- Products
- Suppliers
- Inventory master
- Purchase order headers and lines
- Sales order headers and lines
- Stock ledger
- Invoices
- Payments

## Key Findings

1. **Missing values:** Purchase-order headers contained 2,370 missing `received_date` values, all associated with cancelled orders. The stock ledger contained 180 records with missing `previous_balance` and `expected_balance` values.
2. **Repeated invoice identifiers:** 196 invoice IDs were repeated, affecting 393 records.
3. **Repeated payment identifiers:** 201 payment IDs were repeated, affecting 403 records.
4. **Inventory anomaly:** All 180 inventory records had `current_stock` greater than `max_stock`. The cause could not be established from the available documentation.
5. **Stock-ledger inconsistencies:** 54,876 records had the existing mismatch flag set. Further checks confirmed that the expected-balance calculations and mismatch flags were consistent for the examined inbound and outbound movements.

## Validation and Decisions
- Created working copies of the 12 primary datasets in the `cleaned_tables` dictionary.
- Verified that working-copy row counts and missing-value counts matched the original datasets.
- Retained missing values and repeated identifiers when there was insufficient evidence to justify corrections.
- Did not invent replacement identifiers, opening balances, or inventory values.
- No corrected CSV files or reusable cleaning script were exported during this stage.

## Deliverable
The detailed findings, validation checks, and data-handling decisions are documented in [`docs/week_2_data_quality_report.md`](DOCS/week_2_data_quality_report.md).

## Conclusion
Week 2 established a documented baseline of data-quality issues that must be considered during subsequent analysis. Unresolved issues were preserved and flagged rather than silently altered. These findings will guide later validation, analytical assumptions, and business reporting.
