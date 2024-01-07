# NYC Taxi Fare and Tip Prediction Analysis

## Project Overview

In this project, I used supervised machine learning to transform raw data from the New York City Taxi and Limousine Commission into predictive insights. My goal was to predict taxi fares and tips, enhancing taxi service efficiency.

<p align="center">
<img src="taxi.jpg" alt="Yellow Taxi - New York City" height="300"/> 
</p>

## Data Pipeline Architecture

<p align="center">
<img src="de-program-architecture.png" alt="Data Pipeline Architecture" height="300"/> 
</p>

The data journey started with the extraction of raw records from the [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), which were then ingested, processed, and analyzed through a data pipeline. Python, Airflow, and Apache Spark made the backbone of the system, leading to Google BigQuery for analytical queries.

## Data Visualization in Looker

<p align="center">
  <img src="looker-visual.png" alt="Data Visualization in Looker" height="350" width="350"/> 
</p>

Dashboard offering a insights on New York City's yellow taxi usage, delivering insights spanning two years.

### Daily Trip Volume Trends
The line graph reveals the daily trip volumes, showing peak times and can aid in optimizing driver schedules and fleet management. 

### Total Trips Overview
There is over 55 million trips in this dataset. This metric illustrates the vast scope of the taxi service industry in NYC, highlighting the critical role it plays in urban mobility.

### Service Type Distribution
The pie chart represents yellow taxi services only, indicating a focused analysis on a specific service type within the city's transportation network.

### Pickup Zone Popularity
A detailed table shows the top pickup zones. This information can inform taxi dispatching to ensure that high-demand areas have adequate service availability.

### Monthly and Yearly Comparison
The bar chart compares monthly trip volumes across 2019 and 2020, providing a clear visual representation of how external factors (COVID-19) have impacted service usage.

## Data Description

In this project, we ingested and processed comprehensive trip record data for yellow and green taxis, as well as For-Hire Vehicles (FHV), provided by the NYC Taxi and Limousine Commission (TLC). Detailed records from these datasets offer valuable insights into urban transportation patterns and behaviors.

### Data Source

The data utilized in this analysis can be found on the [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

### Yellow and Green Taxi Data Fields

| Field Name             | Description                                      |
|------------------------|--------------------------------------------------|
| `Pickup_DateTime`      | The date and time when the ride was initiated.   |
| `Dropoff_DateTime`     | The date and time when the ride was concluded.   |
| `Pickup_Location`      | The location where passengers were picked up.    |
| `Dropoff_Location`     | The location where passengers were dropped off.  |
| `Trip_Distance`        | The distance of the trip.                        |
| `Fare_Amount`          | The cost of the trip before tips and surcharges. |
| `Rate_Type`            | The type of rate applied to the trip.            |
| `Payment_Type`         | The method of payment used.                      |
| `Passenger_Count`      | The number of passengers reported by the driver. |

### FHV Data Fields

| Field Name               | Description                                    |
|--------------------------|------------------------------------------------|
| `Base_License_Number`    | The license number of the dispatching base.    |
| `Pickup_DateTime`        | The date and time when the ride was initiated. |
| `Pickup_Location_ID`     | The taxi zone location ID for the pickup.      |

## Technology Stack

During this data engineering programI used the following suite of technologies, libraries, and systems.

- **Python Libraries**: Incorporated Python libraries such as Pandas, NumPy, PyArrow, and others for data manipulation and processing tasks.
- **Shell Scripting**: Used for automating repetitive tasks, managing system operations, and streamlining data processing workflows.
- **Linux**: The preferred operating system for its stability, performance, and flexibility in managing data-intensive applications and services.
- **PostgreSQL**: Employed for sophisticated database management and operations.
- **Docker**: Utilized to containerize applications, ensuring consistent environments and deployment processes.
- **Google Cloud Platform**: Integrated GCP's BigQuery for advanced data analytics, Cloud Storage for durable and scalable storage solutions, and Cloud SQL for fully-managed database services.
- **Terraform**: Applied as an infrastructure-as-code tool to provision and manage cloud services and resources systematically.
- **Airflow**: Adopted to orchestrate complex workflows, ensuring efficient and reliable ETL processes.
- **DBT Cloud**: Implemented to transform data within the warehouse and construct data models seamlessly in the cloud.
- **Apache Spark**: Deployed for processing large-scale data with speed and ease.
- **Apache Kafka**: Leveraged for its real-time data streaming capabilities to process and move large amounts of data efficiently.

## Key Business Impact of the Tip Prediction Model

Through BigQuery, I implemented SQL-based supervised machine learning model to forecast tip amounts for different types of taxi. This way, we give taxi companies actionable insights that can impact their pricing strategies and enhance customer satisfaction. One of the most impactful outcomes is the ability to inform dynamic pricing models which adapt to tipping trends, thus maximizing profitability without compromising on service quality.

```sql
-- Hyperparameter tuning to optimize the prediction model
CREATE OR REPLACE MODEL trips_data_all.tip_hyperparam_model
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['tip_amount'],
  DATA_SPLIT_METHOD='AUTO_SPLIT',
  num_trials=5,
  max_parallel_trials=2,
  l1_reg=hparam_range(0, 20),
  l2_reg=hparam_candidates([0, 0.1, 1, 10])) AS
SELECT * FROM trips_data_all.yellow_tripdata_ml WHERE tip_amount IS NOT NULL;