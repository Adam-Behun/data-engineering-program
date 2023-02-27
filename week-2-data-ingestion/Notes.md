# Workflow Orchestration
Starts as a .csv, ends as a table in the Google Cloud Storage (GCS)

1. wget a .csv from the internet
2. locally change the .csv into parquet file
3. upload this parquet file into Google Cloud Storage (Data Lake on GCP)
4. upload to BQ -- resulting in table of BQ

## Data workflow orchestration

- Luigi
- Apache Airflow
- Prefect

## Airflow
- workflow engine - job scheduler, parallel executions
- Originally by AirBnB
- Using DAG - tree structure that never loops back defining the order of execution
- Using python, python libraries, lost of python with Airflow 

### Components

- Metadata Database
- Scheduler
- Workers
- Webserver
- User Interface
- DAG Directory

### Concepts

- Tasks
  - Functions running
  - Operators connecting to different sources
- Control Flow
  - Order of the tasks
- User Interface

### Considerations
- DAGs must end before they can be executed again
- Does not support streaming data - it's a batch type of data processing
- Careful with jobs external to Airflow
- Find the optimal balance between complexity and workflow requirements
    - understand administration and maintainability of complex data systems at scale