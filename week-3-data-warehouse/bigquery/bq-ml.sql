-- Select columns of interest for predicting the tip amount
SELECT passenger_count, trip_distance, PUlocationID, DOlocationID, payment_type, fare_amount, tolls_amount, tip_amount
FROM dtc-de-371802.trips_data_all.yellow_tripdata_partitioned WHERE fare_amount != 0;

-- Create a ML table with appropriate types
CREATE OR REPLACE TABLE dtc-de-371802.trips_data_all.yellow_tripdata_ml (
  passenger_count INTEGER,
  trip_distance FLOAT64,
  PUlocationID STRING,
  DOlocationID STRING,
  payment_type STRING, 
  fare_amount FLOAT64,
  tolls_amount FLOAT64, 
  tip_amount FLOAT64
) AS (
    SELECT passenger_count, trip_distance, cast(PUlocationID AS STRING), cast(DOlocationID AS STRING),
    CAST(payment_type AS STRING), fare_amount, tolls_amount, tip_amount
    FROM dtc-de-371802.trips_data_all.yellow_tripdata_partitioned WHERE fare_amount != 0
);

-- Create a model with default settings
CREATE OR REPLACE MODEL trips_data_all.tip_model
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['tip_amount'],
  DATA_SPLIT_METHOD='AUTO_SPLIT') AS
SELECT * FROM trips_data_all.yellow_tripdata_ml WHERE tip_amount IS NOT NULL;

-- Check features
SELECT * FROM ML.FEATURE_INFO(MODEL trips_data_all.tip_model);

-- Evaluate the model
SELECT * FROM ML.EVALUATE(MODEL trips_data_all.tip_model, (SELECT * FROM trips_data_all.yellow_tripdata_ml WHERE tip_amount IS NOT NULL));

-- Predict the model
SELECT * FROM ML.PREDICT(MODEL trips_data_all.tip_model, (SELECT * FROM trips_data_all.yellow_tripdata_ml WHERE tip_amount IS NOT NULL));

-- Predict and explain
SELECT * FROM ML.EXPLAIN_PREDICT(MODEL trips_data_all.tip_model, (SELECT * FROM trips_data_all.yellow_tripdata_ml WHERE tip_amount IS NOT NULL),
STRUCT(3 AS top_k_features));

-- Hyper Param Tunning
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

