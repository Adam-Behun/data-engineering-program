# Downloads data from https://github.com/DataTalksClub/nyc-tlc-data/releases/download/
# Reads the .csv.gz files for yellow, green, and fhv data
# Changes .csv.gz format into parquet
#   Sets desired data types of all columns 
# Loads data into Google Cloud Storage Bucket used as a Data Lake
# Creates external tables in Big Query used as our Data Warehouse

# next tasks
# format the datasets in GCS from raw into green and yellow, create partition tables in bq


import os
import logging

from datetime import datetime

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage

import pyarrow.csv as pv
import pyarrow.parquet as pq
import pyarrow as pa


PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

table_schema_green = pa.schema(
    [
        ('VendorID',pa.string()),
        ('lpep_pickup_datetime',pa.timestamp('s')),
        ('lpep_dropoff_datetime',pa.timestamp('s')),
        ('store_and_fwd_flag',pa.string()),
        ('RatecodeID',pa.int64()),
        ('PULocationID',pa.int64()),
        ('DOLocationID',pa.int64()),
        ('passenger_count',pa.int64()),
        ('trip_distance',pa.float64()),
        ('fare_amount',pa.float64()),
        ('extra',pa.float64()),
        ('mta_tax',pa.float64()),
        ('tip_amount',pa.float64()),
        ('tolls_amount',pa.float64()),
        ('ehail_fee',pa.float64()),
        ('improvement_surcharge',pa.float64()),
        ('total_amount',pa.float64()),
        ('payment_type',pa.int64()),
        ('trip_type',pa.int64()),
        ('congestion_surcharge',pa.float64()),
    ]
)

table_schema_yellow = pa.schema(
   [
        ('VendorID', pa.string()), 
        ('tpep_pickup_datetime', pa.timestamp('s')), 
        ('tpep_dropoff_datetime', pa.timestamp('s')), 
        ('passenger_count', pa.int64()), 
        ('trip_distance', pa.float64()), 
        ('RatecodeID', pa.string()), 
        ('store_and_fwd_flag', pa.string()), 
        ('PULocationID', pa.int64()), 
        ('DOLocationID', pa.int64()), 
        ('payment_type', pa.int64()), 
        ('fare_amount',pa.float64()), 
        ('extra',pa.float64()), 
        ('mta_tax', pa.float64()), 
        ('tip_amount', pa.float64()), 
        ('tolls_amount', pa.float64()), 
        ('improvement_surcharge', pa.float64()), 
        ('total_amount', pa.float64()), 
        ('congestion_surcharge', pa.float64())]

)

table_schema_fhv = pa.schema(
   [
        ('dispatching_base_num', pa.string()), 
        ('pickup_datetime', pa.timestamp('s')), 
        ('dropOff_datetime', pa.timestamp('s')),
        ('PUlocationID', pa.int64()), 
        ('DOlocationID', pa.int64()),
        ('SR_Flag', pa.int64()),
        ('Affiliated_base_number', pa.string()),]

)

# function needs to set data types before converting into parquet 
# implement this -> https://github.com/sebastian2296/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/web_to_gcs.py
# and this -> https://arrow.apache.org/docs/python/csv.html

def format_to_csv(source_file, destination_file):
    table = pv.read_csv(source_file)    
    table = pv.write_csv(table, destination_file)


def format_to_parquet(src_file, service, dest_file):
    table = pv.read_csv(src_file)    
    
    if service == 'yellow':
            table = table.cast(table_schema_yellow)
    elif service == 'green':
            table = table.cast(table_schema_green)
    elif service == 'fhv':
        table = table.cast(table_schema_fhv)

    pq.write_table(table, dest_file)


def upload_to_gcs(bucket, object_name, local_file):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


default_args = {
    "owner": "airflow",
    #"start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}


def download_parquetize_upload_dag(
    dag,
    url_template,
    local_csv_gz_path_template,
    local_csv_path_template,
    local_parquet_path_template,
    gcs_path_template
):
    with dag:
        download_dataset_task = BashOperator(
            task_id="download_dataset_task",
            bash_command=f"curl -sSLf {url_template} > {local_csv_gz_path_template}"
        )
        
        format_to_csv_task = PythonOperator(
            task_id="format_to_csv_task",
            python_callable=format_to_csv,
            op_kwargs={
                "source_file": local_csv_gz_path_template,
                "destination_file": local_csv_path_template 
            },
        )
        
        format_to_parquet_task = PythonOperator(
            task_id="format_to_parquet_task",
            python_callable=format_to_parquet,
            op_kwargs={
                "src_file": local_csv_path_template,
                "service": "fhv",
                "dest_file": local_parquet_path_template
            },
        )

        local_to_gcs_task = PythonOperator(
            task_id="local_to_gcs_task",
            python_callable=upload_to_gcs,
            op_kwargs={
                "bucket": BUCKET,
                "object_name": gcs_path_template,
                "local_file": local_parquet_path_template,
            },
        )

        rm_task = BashOperator(
            task_id="rm_task",
            bash_command=f"rm {local_csv_gz_path_template} {local_csv_path_template} {local_parquet_path_template}"
        )

        download_dataset_task >> format_to_csv_task >> format_to_parquet_task >> local_to_gcs_task >> rm_task

# Specific for Yellow Taxi data
# Website --> https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-01.csv.gz

URL_PREFIX = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'

YELLOW_TAXI_URL_TEMPLATE = URL_PREFIX + 'yellow' + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv.gz'
YELLOW_TAXI_CSV_GZ_FILE_TEMPLATE = AIRFLOW_HOME + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv.gz'
YELLOW_TAXI_CSV_FILE_TEMPLATE = AIRFLOW_HOME + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv'
YELLOW_TAXI_PARQUET_FILE_TEMPLATE = AIRFLOW_HOME + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
YELLOW_TAXI_GCS_PATH_TEMPLATE = "raw/yellow_tripdata/{{ execution_date.strftime(\'%Y\') }}/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet"


yellow_taxi_data_dag = DAG(
    dag_id="yellow_taxi_data_adam_last_month_done",
    schedule_interval="0 6 2 * *",
    start_date=datetime(2019, 4, 1),
    end_date=datetime(2019, 5, 1),
    default_args=default_args,
    catchup=True,
    max_active_runs=3,
    tags=['dtc-de'],
)

download_parquetize_upload_dag(
    dag=yellow_taxi_data_dag,
    url_template=YELLOW_TAXI_URL_TEMPLATE,
    local_csv_gz_path_template=YELLOW_TAXI_CSV_GZ_FILE_TEMPLATE,
    local_csv_path_template=YELLOW_TAXI_CSV_FILE_TEMPLATE,
    local_parquet_path_template=YELLOW_TAXI_PARQUET_FILE_TEMPLATE,
    gcs_path_template=YELLOW_TAXI_GCS_PATH_TEMPLATE
)

# Specific for Green Taxi data
GREEN_TAXI_URL_TEMPLATE = URL_PREFIX + 'green' + '/green_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv.gz'
GREEN_TAXI_CSV_GZ_FILE_TEMPLATE = AIRFLOW_HOME + '/green_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv.gz'
GREEN_TAXI_CSV_FILE_TEMPLATE = AIRFLOW_HOME + '/green_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv'
GREEN_TAXI_PARQUET_FILE_TEMPLATE = AIRFLOW_HOME + '/green_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
GREEN_TAXI_GCS_PATH_TEMPLATE = "raw/green_tripdata/{{ execution_date.strftime(\'%Y\') }}/green_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet"

green_taxi_data_dag = DAG(
    dag_id="green_taxi_data_adam_final",
    schedule_interval="0 7 2 * *",
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2021, 1, 1),
    default_args=default_args,
    catchup=True,
    max_active_runs=3,
    tags=['dtc-de'],
)

download_parquetize_upload_dag(
    dag=green_taxi_data_dag,
    url_template=GREEN_TAXI_URL_TEMPLATE,
    local_csv_gz_path_template=GREEN_TAXI_CSV_GZ_FILE_TEMPLATE,
    local_csv_path_template=GREEN_TAXI_CSV_FILE_TEMPLATE,
    local_parquet_path_template=GREEN_TAXI_PARQUET_FILE_TEMPLATE,
    gcs_path_template=GREEN_TAXI_GCS_PATH_TEMPLATE
)

# Specific for FHV data
FHV_TAXI_URL_TEMPLATE = URL_PREFIX + 'fhv' + '/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv.gz'
FHV_TAXI_CSV_GZ_FILE_TEMPLATE = AIRFLOW_HOME + '/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv.gz'
FHV_TAXI_CSV_FILE_TEMPLATE = AIRFLOW_HOME + '/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.csv'
FHV_TAXI_PARQUET_FILE_TEMPLATE = AIRFLOW_HOME + '/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
FHV_TAXI_GCS_PATH_TEMPLATE = "raw/fhv_tripdata/{{ execution_date.strftime(\'%Y\') }}/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet"

fhv_taxi_data_dag = DAG(
    dag_id="fhv_taxi_data_adam_final",
    schedule_interval="0 8 2 * *",
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2021, 1, 1),
    default_args=default_args,
    catchup=True,
    max_active_runs=3,
    tags=['dtc-de'],
)

download_parquetize_upload_dag(
    dag=fhv_taxi_data_dag,
    url_template=FHV_TAXI_URL_TEMPLATE,
    local_csv_gz_path_template=FHV_TAXI_CSV_GZ_FILE_TEMPLATE,
    local_csv_path_template=FHV_TAXI_CSV_FILE_TEMPLATE,
    local_parquet_path_template=FHV_TAXI_PARQUET_FILE_TEMPLATE,
    gcs_path_template=FHV_TAXI_GCS_PATH_TEMPLATE
)