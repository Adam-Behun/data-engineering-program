## Week 2 Homework

Put the dag files as links here


In this homework, we'll prepare data for the next week. We'll need
to put these datasets to our data lake:

* For the lessons, we'll need the Yellow taxi dataset (years 2019 and 2020)
* For the homework, we'll need FHV Data (for-hire vehicles, for 2019 only)

You can find all the URLs on [the dataset page](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)


When you run this for all the data, the temporary files will be saved in Docker and will consume your 
disk space. If it causes problems for you, add another step in your DAG that cleans everything up.
It could be a bash operator that runs this command:

```bash
rm name-of-csv-file.csv name-of-parquet-file.parquet
```

## Question 1: DAG for yellow_taxi and green_taxi (2 points)

Create DAG for uploading the yellow_taxi data into GCS

week-2-data-ingestion\airflow\dags\homework_ingestion_2.0.py


## Question 2: DAG for FHV Data (2 points)

Create DAG for uploading the FHV data into GCS

week-2-data-ingestion\airflow\dags\homework_ingestion_2.0.py


## Question 3: DAG for Zones (2 points)


Create DAG for uploading Zones into CGS:

week-2-data-ingestion\airflow\dags\homework_ingestion_zones.py