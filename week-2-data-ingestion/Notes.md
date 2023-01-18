Notes for the data lake and data warehouse are in week 1 notes

# Workflow Orchestration

Data pipeline - gets data and then produces data, ingestion scripts from week 1

## Simple data pipeline

1. Download data from the internet
2. Ingest data into PostgreSQL

## Simple data pipeline -- Data Workflow

Starts as a .csv, ends as a table in the cloud storage

1. wget a .csv from the internet
2. locally change the .csv into parquet file
3. upload this parquet file into Google Cloud Storage (Data Lake on GCP)
4. upload to BQ -- resulting in table of BQ

## Parquet files

## DAG - Directed Acyclic Graph

## Data workflow orchestration

- Luigi
- Apache Airflow
- Prefect

## Airflow


localhost 8000 for http server
localhost 8080 for pg and airflow


## Tasks

1. Get airflow to ingest data into GCS
Check out the logs for dags
Google Credentials is not being read by the system - local_to_gcs_task seems like the problem
to run it just go docker-compose up in the the airflow directory, should be 6 services running
watch the videos again and watch later videos too


## Jinja

Learn airflow and the ways we orchestrate data workflows, different services withing airflow