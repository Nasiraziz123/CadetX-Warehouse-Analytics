@@ -0,0 +1,69 @@
# Week 1 Sprint Notes

## 1. Sprint Overview

**Project:** Heavy Supplier, Inventory & Warehouse Analytics  
**Programme:** CadetX Virtual Work Experience  
**Sprint:** Week 1 — Project Setup and Data Understanding

### Sprint Objective

Establish the project structure, profile the available datasets, assess initial data quality, identify relationships between tables, and document preliminary findings and questions for further investigation.

## 2. Work Completed

- Created the local project folder structure.
- Developed a Python data-profiling script using pandas.
- Inspected dataset dimensions, column names, data types, missing values, and exact duplicate rows.
- Checked key uniqueness and selected relationships between tables.
- Validated date fields and selected date-related business rules.
- Tested financial calculations in purchase orders, sales orders, and invoices.
- Investigated inventory master stock thresholds.
- Performed preliminary stock-ledger running-balance checks.
- Created an initial data quality log.
- Created an initial data dictionary.
- Uploaded the profiling script and project files to the public GitHub repository.

## 3. Key Findings

1. Several primary identifiers and foreign-key relationships passed the checks performed.
2. Purchase order and sales order financial calculations were internally consistent within the tested tolerances.
3. All 180 inventory master records had current stock greater than maximum stock, requiring investigation.
4. Repeated invoice IDs and payment IDs may affect the reliability of financial reconciliation.
5. The stock-ledger running-balance check produced preliminary mismatches, but transaction sequencing and adjustment rules remain unconfirmed.
6. Some cancelled sales orders contained delivery dates, and some received purchase orders arrived after their expected delivery dates. These findings require business interpretation rather than automatic correction.

## 4. Unresolved Questions

- Why does current stock exceed maximum stock in every inventory master record?
- Are invoice IDs and payment IDs required to be unique?
- What is the correct transaction sequence for stock movements recorded on the same date?
- How should stock adjustments affect running balances?
- Should cancelled sales orders have delivery dates?
- What are the official definitions and units for key fields?
- What business KPIs and questions does CadetX expect the team to prioritize?

## 5. Risks and Limitations

- Official field documentation was unavailable during the initial profiling.
- Some business rules cannot yet be confirmed.
- Repeated invoice and payment identifiers may create misleading results when tables are joined.
- Stock-ledger validation depends on transaction ordering and adjustment rules.
- The findings are preliminary and should be reviewed before any data corrections or final business conclusions.

## 6. Next Steps

1. Confirm the official field definitions and business rules.
2. Investigate the inventory master stock inconsistencies.
3. Investigate repeated invoice and payment identifiers.
4. Confirm stock-ledger sequencing and adjustment logic.
5. Review the data dictionary and data quality log.
6. Define initial supply-chain business questions and KPIs.
7. Update the README with the project overview, setup instructions, and key findings.
8. Review the repository and submit the required Week 1 deliverables through the CadetX platform.

## 7. Sprint Conclusion

Week 1 established the foundation for the project through repository setup, Python-based data profiling, preliminary validation, and documentation. Several relationships and financial calculations passed the checks performed, while a small number of significant issues require clarification before further analysis.

The next phase should focus on confirming business rules, investigating the identified issues, and agreeing on the most relevant inventory, supplier, purchasing, and sales performance measures.