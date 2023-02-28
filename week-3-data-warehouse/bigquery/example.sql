-- Public query example
SELECT station_id,name FROM `bigquery-public-data.new_york_citibike.citibike_stations` LIMIT 100; 

-- Check yellow external table
SELECT * FROM dtc-de-371802.trips_data_all.yellow_tripdata_external_table LIMIT 10;

-- Create a non-partitioned table from the external table
CREATE OR REPLACE TABLE dtc-de-371802.trips_data_all.yellow_tripdata_non_partitioned AS
SELECT * FROM dtc-de-371802.trips_data_all.yellow_tripdata_external_table;

-- Create a partitioned table from the external table
CREATE OR REPLACE TABLE dtc-de-371802.trips_data_all.yellow_tripdata_partitioned
PARTITION BY
  DATE(tpep_pickup_datetime) AS
SELECT * FROM dtc-de-371802.trips_data_all.yellow_tripdata_external_table;

-- Impact of partitioning 
-- Non-partitioned 
SELECT DISTINCT(VendorID)
FROM dtc-de-371802.trips_data_all.yellow_tripdata_non_partitioned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';

-- Partitioned
SELECT DISTINCT(VendorID)
FROM dtc-de-371802.trips_data_all.yellow_tripdata_partitioned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';

-- Looking into the partitions
SELECT table_name, partition_id, total_rows
FROM trips_data_all.INFORMATION_SCHEMA.PARTITIONS
WHERE table_name = 'yellow_tripdata_partitioned'
ORDER BY total_rows DESC;

-- Create a partitioned + clustered table from the external table
CREATE OR REPLACE TABLE dtc-de-371802.trips_data_all.yellow_tripdata_partitioned_clustered
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM dtc-de-371802.trips_data_all.yellow_tripdata_external_table;

-- Impact of clustering
-- Non-clustered
SELECT COUNT(*) AS trips
FROM dtc-de-371802.trips_data_all.yellow_tripdata_partitioned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
AND VendorID = '1';

-- Clustered
SELECT COUNT(*) AS trips
FROM dtc-de-371802.trips_data_all.yellow_tripdata_partitioned_clustered
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
AND VendorID = '1';
