# Data Directory

This folder contains the input data files used for training and applying the dropout prediction model. All files are anonymized or synthetic, and no personally identifiable information (PII) is included.

## File Descriptions

- **2024_example_input.csv**  
  A sample dataset containing the enrollment-time attributes of students from the 2024 cohort. This file simulates the format and structure used for prospective predictions in production.

- **program_change_map.csv**  
  A mapping table used to identify and recode students who changed academic programs during their first year. This is used to adjust the dropout labels accordingly.

- **dropout_status.csv**  
  A binary label file indicating whether each student in the training set dropped out (1) or persisted (0). This label is derived from institutional tracking data.

- **area_code_location_map.csv**  
  A utility table that translates telephone area codes (LADA) into geographic regions. This feature is used to infer students' commuting zones or states of origin.

## Notes

- All data files here are required for the full pipeline to run successfully.
- If you use your own institutional data, make sure to match the expected column names and formats as defined in the preprocessing scripts.
