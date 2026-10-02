# Group 3 - FinalProject

### Members

- Maureen Joi Cruz
- Patrick Raphael Lista
- Audrey Paulynne Olaybar
- Patricia Ann Mae Pascual
- Gianela Zapata

## Project Title

Spatial Equity in Healthcare: Mapping Facility Densities and Specialization Gaps Across NCR

## Project Overview

This project evaluates the distribution, sufficiency, and type of specialization of health facilities across the 17 Local Government Units (LGUs) in the National Capital Region (NCR) relative to local population density and geographic area. The group will utilize two complementary datasets: the Philippines Health Facilities (OpenStreetMap Export) sourced from the Humanitarian Data Exchange (HDX) and the 2024 Census of Population (POPCEN) from the Philippine Statistics Authority (PSA).

The study focuses on assessing public health emergency readiness and identifying critical disparities in healthcare infrastructure across Metro Manila.

### Intended Audience

Urban Planners and Spatial Analysts (MMDA & Local LGUs),  Public Health Officials and Policy Makers (DOH & NCR Regional Office), Emergency Response and Disaster Risk Reduction Managers (MDRRMO & OCD-NCR), Healthcare Investors and Non-Profit Organizations

### Problem

This study aims to evaluate the distribution, sufficiency, and type of specialization of health facilities across the 17 Local Government Units (LGUs) in the National Capital Region (NCR) relative to local population density and geographic area. Specifically, this visualization project seeks to assess healthcare emergency readiness and identify critical infrastructure disparities across Metro Manila by answering the following questions

## Analytical Questions

1. Which NCR cities fall below standard healthcare capacity benchmarks when measuring the number of health facilities per LGU?
2. How does physical health facility density compare to the population number across NCR cities, and which dense LGUs experience the highest operational deficit?
3. To what extent are LGUs in NCR dominated by general/retail health services (pharmacies, general clinics) versus high-priority specialized centers (hospitals, maternity/birthing centers, diagnostic laboratories)?

## Proposed Datasets

### 1. Health Facility Locations

- **Provider:** Humanitarian OpenStreetMap Team (HOT) / OpenStreetMap contributors
- **Dataset:** Philippines Health Facilities (OpenStreetMap Export)
- **Coverage:** National Capital Region (NCR / Metro Manila), 731 records (modified May 2026)
- **Unit:** Count of health facility records and spatial geometry (latitude, longitude coordinates)

### 2. Populations Counts

- **Provider:** Philippine Statistics Authority (PSA) - 2024 Census of Population (POPCEN)
- **Dataset:** 2024 Census of Population Population Counts Declared Official by the President
- **Coverage:** 17 Local Government Units in NCR (2024 Census data)
- **Unit:** Total population headcount

## Dataset Relationship

The two datasets will be linked using municipal/city administrative boundary names as the primary integration key (addr: city in Dataset 1 mapped to REGION, PROVINCE, AND CITY/MUNICIPALITY in Dataset 2).

Initial data inspection addressed administrative boundary nuances, such as filtering for NCR's 17 LGUs and accounting for boundary realignments (e.g., the transfer of 10 EMBO barangays from Makati to Taguig) to ensure precise record matching between the two datasets.

## Group Responsibilities

| Member | Main Responsibility | Peer Reviewer |
|---|---|---|
| Gianela Zapata | Modular Architecture and NumPy Computations | Patricia Ann Mae Pascual |
| Patrick Raphael Lista | Data Acquisition and Automates Reliability | Maureen Joi Cruz |
| Maureen Joi Cruz | Data Cleaning, Profiling an Quality Evidence | Patrick Raphael Lista |
| Patricia Ann Mae Pascual | Data Integration and Analytical Computation | Audrey Paulynne Olaybar |
| Audrey Paulynne Olaybar | Data visualization and Performance Benchmarking | Gianela Zapata |

### Collaboration

Each member will contribute substantive Python code and conduct peer reviews on another member's work. Responsibilities and task assignments may be adjusted as the project progresses based on group workflow and instructor feedback.

## Project Structure

```text
DATA SET 1 & 2/
├── raw/

Notebooks/
├── data-inspections-ncr.py

proposal/
├── Week-8-Checkin-1.pdf
```

## Initial Inspection

he group executed an initial Python inspection of both datasets to analyze shape (.shape), schema (.dtypes), and data quality anomalies—such as missing coordinates, text formatting artifacts, and unpopulated specialization fields. The team also validated municipal join keys across both datasets to ensure seamless data integration.

## Project Status

**Week 8 - Initial Proposal and Programming Plan**

The group has finalized the spatial scope for NCR, completed the initial data profiling, and established three core analytical questions for the Week 8 proposal and programming plan.
