# Heavy Supplier, Inventory & Warehouse Analytics

**CadetX Virtual Work Experience — Data Analytics & Data Science**

## Project Overview

This project explores supply-chain operations using data related to suppliers, products, inventory, warehouses, purchasing, sales, invoices, and payments.

The objective is to understand the available data, assess data quality, identify relationships between tables, and establish a foundation for future operational and business analysis.

## Week 1 Objectives

- Understand the available datasets and their structures.
- Profile tables using Python and pandas.
- Check missing values, duplicate records, key uniqueness, and relationships.
- Validate selected dates, stock thresholds, and financial calculations.
- Document findings, assumptions, and unresolved questions.
- Identify potential business questions and KPIs for subsequent analysis.

## Repository Structure

```text
CadetX-Warehouse-Analytics/
├── Data/                       # Raw data; excluded from Git
├── Docs/
│   ├── data_quality_log.md
│   ├── initial_data_dictionary.md
│   └── week_1_sprint_notes.md
├── Src/
│   └── data_profiling.py
├── .gitignore
└── README.md
```

## Tools and Technologies

- Python
- pandas
- Git and GitHub
- Markdown documentation

## Initial Findings

- Several identifier and foreign-key checks passed.
- Purchase order and sales order financial calculations were consistent within the tested tolerances.
- All 180 inventory master records had current stock greater than maximum stock, requiring further investigation.
- Repeated invoice IDs and payment IDs may affect payment reconciliation.
- Preliminary stock-ledger running-balance mismatches require further investigation into transaction sequencing and adjustment rules.
- Some delivery-date observations require clarification of the relevant business rules.

These are preliminary findings, not confirmed explanations of the underlying issues.

## Documentation

- [Data Quality Log](Docs/data_quality_log.md)
- [Initial Data Dictionary](Docs/initial_data_dictionary.md)
- [Week 1 Sprint Notes](Docs/week_1_sprint_notes.md)

## Running the Profiling Script

1. Install Python if it is not already installed.
2. Install pandas:

   ```bash
   python -m pip install pandas
   ```

3. Download or clone this repository.
4. Obtain the project datasets through the authorized CadetX source and place the CSV files in the local `Data/` directory.
5. Run the profiling script from the project root:

   ```bash
   python Src/data_profiling.py
   ```

The script's required input files and execution assumptions should be checked against its actual implementation before running it in a new environment.

## Data Handling

The raw `Data/` directory is excluded from Git through `.gitignore`. The repository therefore does not contain the raw CSV files. Access the dataset through the authorized project source and follow CadetX's data-sharing requirements.

## Current Status

**Week 1:** Initial profiling and documentation completed locally. Findings and unresolved data-quality questions have been recorded for follow-up.

## Next Steps

- Confirm field definitions and business rules.
- Investigate the identified stock and identifier issues.
- Define initial supply-chain business questions and KPIs.
- Continue the project according to the CadetX sprint roadmap.