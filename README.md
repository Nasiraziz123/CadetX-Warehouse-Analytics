# Heavy Supplier, Inventory & Warehouse Analytics

**CadetX Virtual Work Experience | Data Analytics & Data Science**

## Project Overview

This project focuses on analyzing supplier, purchasing, inventory, warehouse, and sales operations using real-world-style supply chain datasets provided for the CadetX Virtual Work Experience program.

The objective is to assess data quality, develop reliable analytical datasets, investigate operational performance, identify business insights, and support data-driven decision-making through the project.

The work is organized into weekly sprints, with documentation and deliverables maintained in GitHub throughout the project.

## Project Objectives

- Understand the structure and relationships of the available datasets.
- Assess data quality, completeness, consistency, and reliability.
- Investigate supplier, purchasing, inventory, warehouse, and sales operations.
- Develop meaningful operational KPIs and analytical insights.
- Identify data issues that could affect business reporting.
- Communicate findings through clear documentation and, where appropriate, analytical reports and visualizations.

## Tools and Technologies

- **Python** — data exploration, profiling, and validation.
- **Pandas** — tabular data analysis and data-quality checks.
- **Git and GitHub** — version control, project organization, and documentation.

Additional tools will be documented as they are used during subsequent project stages.

## Dataset Overview

The project includes 12 primary datasets covering:

| Area | Datasets |
|---|---|
| Business entities | Customers, branches, products, suppliers |
| Inventory | Inventory master, stock ledger |
| Purchasing | Purchase order headers, purchase order lines |
| Sales | Sales order headers, sales order lines |
| Financial transactions | Invoices, payments |

The raw datasets are maintained locally in the `Data/` directory and excluded from Git where configured by `.gitignore`.

## Project Progress

The project follows a 12-week sprint structure. This section will be updated as each sprint is completed.

### Week 1 — Project Setup and Data Understanding

**Status: Completed**

- Established the project repository and initial folder structure.
- Explored the available datasets and their structures.
- Reviewed dataset dimensions, columns, data types, missing values, and duplicate records.
- Began documenting the datasets and initial project findings.

**Documentation:** [Week 1 README](week_1/README.md)

### Week 2 — Data Quality Assessment

**Status: Documentation prepared; final Git validation pending**

The second week focused on assessing the reliability of the 12 primary datasets and documenting issues that could affect downstream analysis.

Key findings included:

- **Missing values:** 2,370 missing purchase-order receipt dates, all associated with cancelled orders.
- **Missing stock-ledger balances:** 180 first-movement records with missing previous and expected balances.
- **Repeated identifiers:** 196 repeated invoice IDs and 201 repeated payment IDs, requiring further investigation.
- **Inventory anomaly:** All 180 inventory records had current stock greater than maximum stock.
- **Stock-ledger checks:** 54,876 records carried the existing mismatch flag. Additional checks examined inbound and outbound balance calculations and sequential balance links.

No unsupported corrections were applied. Ambiguous values and repeated identifiers were retained for investigation rather than changed without evidence.

Working copies were validated against the original row counts and missing-value counts. Corrected CSV exports and a reusable cleaning script were not produced during this stage.

**Documentation:**
- [Week 2 README](week_02/README.md)
- [Week 2 Data Quality Assessment Report](week_2/DOCS/week_2_data_quality_report.md)

### Weeks 3–12 — Upcoming Sprints

The remaining weekly sections will be added as the corresponding tasks are completed. Progress, findings, and deliverables will reflect the work actually performed during each sprint.

## Repository Structure

```text
CadetX-Warehouse-Analytics/
├── .gitignore
├── Data/                           # Local raw datasets
├── Src/                            # Shared project scripts
│   └── data_profiling.py
├── week-01/
│   ├── README.md
│   └── docs/
├── week-02/
│   ├── README.md
│   └── docs/
│       └── week_2_data_quality_report.md
└── README.md                       # Main project documentation
```

The structure will evolve as new weekly deliverables are added. The shared `Src/` directory will remain at the project root, and each weekly folder will maintain its own README and supporting documentation.

## Data Handling Principles

- Preserve the original datasets.
- Validate assumptions before correcting questionable values.
- Do not invent missing balances or replacement identifiers without supporting evidence.
- Document unresolved data-quality issues and their potential analytical impact.
- Validate transformations and retain a clear record of analytical decisions.

## Final Deliverables

The repository will progressively contain weekly documentation, analysis scripts, data-quality assessments, validated analytical outputs where appropriate, and business findings.

The final project summary and conclusions will be expanded as the remaining sprints are completed.

---

**Project:** Heavy Supplier, Inventory & Warehouse Analytics  
**Program:** CadetX Virtual Work Experience  
**Duration:** 12 weeks
