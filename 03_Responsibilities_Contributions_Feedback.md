# Responsibilities, Contributions, and Feedback

## Week 8 Responsibilities

| Member | Responsibility |
|---|---|
| **Gianela Zapata** | Created the shared group repository, granted access to all members and the instructor, and captured the current commit hash for the proposal. Wrote the study group details, project title, target audience, disaster preparedness problem statement, and 2–3 analytical questions (e.g., health facility density relative to population risk). Created the component mapping table (acquisition, validation, cleaning, integration, analysis, visualization, testing, execution) and assigned a primary programmer and reviewer for each stage.|
| **Patrick Raphael Lista** | Wrote the metadata section for Dataset 1 (Health Facility Locations) provider, source URL, coverage, fields, and known limitations. Extracted a representative sample slice (CSV/Excel) of the health facilities dataset and uploaded it to the repository. Coordinated with Patricia Ann Mae Pascual to confirm the common joining column (e.g., Province, Municipality, or Region_Code). Sent the Dataset 1 sample file to Maureen Joi Cruz so coding could begin..|
| **Patricia Ann Mae Pascual** | Found and downloaded a relevant 2nd dataset that paired with health facilities (e.g., PSA Population Data per Municipality/Province or NDRRMC/NOAH Disaster Hazard Risk Data). Wrote the metadata section for Dataset 2 (provider, source URL, coverage, fields, limitations, and integration key). Extracted a sample slice of Dataset 2, uploaded it to the repo, and sent it to Maureen Joi Cruz. Wrote the risk assessment covering all 6 mandatory areas (data access, key mismatches, missing information, privacy, scope, schedule) with fallback strategies. |
| **Maureen Joi Cruz** | Wrote the initial Python script/notebook using Pandas and NumPy to: Load sample files for both datasets. Displayed columns, data types (.dtypes), and array/dataframe shapes (.shape). Reported data quality issues (e.g., missing coordinates, unformatted text, missing population counts). Added code comments explicitly linking dataset variables back to Gianela Zapata's analytical questions.|
| **Audrey Paulynne Olaybar** | Compiled all written sections into 01_Week_8_Proposal.md, formatted headers cleanly, and exported the final 2–3 page PDF. Packaged the final submission ZIP containing the inspection code and both sample data files. Completed 03_Responsibilities_Contributions_Feedback.md, documenting task assignments and contributions for all 5 members.|

These responsibilities reflect the group's assigned tasks for the Week 8 Check-in 1 proposal and programming plan. Responsibilities and contributions will be updated as the project progresses.

## Week 8 Contributions

- The group selected two primary datasets: the Philippines Health Facilities dataset (OpenStreetMap export on HDX, modified May 2026) and the 2024 Census of Population (POPCEN) dataset from the Philippine Statistics Authority (PSA).
- The group defined the spatial scope focusing on the 17 Local Government Units (16 cities and 1 municipality) in the National Capital Region (NCR / Metro Manila) and established three core analytical questions targeting health facility capacity benchmarks, density relative to population, and service specialization distribution
- The group conducted an initial profiling and data quality assessment, identifying key issues such as non-standardized LGU text formatting (e.g., thousands separators and footnote artifacts in PSA data), incomplete capacity/specialty attributes for smaller clinics, and missing geographic coordinates
- The group verified the joining mechanism between both datasets by planning the standardization of the municipal/city keys (addr:city in Dataset 1 mapped to REGION, PROVINCE, AND CITY/MUNICIPALITY in Dataset 2).
- The group structured, formatted, and compiled all written components into the Week 8 check-in proposal and programming plan.

## Peer Review and Collaboration

Each member will review the work of other group members as the project progresses. Reviews, revisions, and collaboration will be recorded in this file.

| Date | Member | Work Reviewed | Reviewer | Comments / Changes |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | To be updated |
| TBD | TBD | TBD | TBD | To be updated |

## Instructor Feedback

| Date | Feedback | Action Taken | Owner | Evidence |
|---|---|---|---|---|
| TBD | Week 8 check-in feedback | To be updated after the check-in | TBD | TBD |

## Future Contributions

The responsibilities listed above are for the Week 8 Check-in 1 proposal and programming plan. As the project continues, the group will record actual coding contributions, peer reviews, revisions, instructor feedback, and other substantive work in this file.



