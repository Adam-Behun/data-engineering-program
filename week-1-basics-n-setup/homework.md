## Week 1 Homework

## Question 1. Google Cloud SDK

Install Google Cloud SDK. What's the version you have? 


- Google Cloud SDK 412.0.0
- bq 2.0.83
- core 2022.12.09
- gcloud-crc32c 1.0.0
- gsutil 5.17`

## Google Cloud account 

Create an account in Google Cloud and create a project.

- Done and billing is enabled. Watch the zones. 

## Question 2. Terraform 

Now install terraform and go to the terraform directory (`week_1_basics_n_setup/1_terraform_gcp/terraform`)

After that, run

* `terraform init`
* `terraform plan`
* `terraform apply` 

Apply the plan and copy the output (after running `apply`) to the form.

It should be the entire output - from the moment you typed `terraform init` to the very end.

# 
adamb@Mine MINGW64 ~/tech/de-zoomcamp/week-1-basics-n-setup/1-terraform-gcp (main)
$ terraform init

Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/google from the dependency lock file
- Using previously-installed hashicorp/google v4.43.1

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

adamb@Mine MINGW64 ~/tech/de-zoomcamp/week-1-basics-n-setup/1-terraform-gcp (main)
$ terraform plan
var.project
  GCP Project ID

  Enter a value: dtc-de-371802

google_storage_bucket.data-lake-bucket: Refreshing state... [id=dtc_data_lake_dtc-de-371802]
google_bigquery_dataset.dataset: Refreshing state... [id=projects/dtc-de-371802/datasets/trips_data_all]

No changes. Your infrastructure matches the configuration.

Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are
needed.

adamb@Mine MINGW64 ~/tech/de-zoomcamp/week-1-basics-n-setup/1-terraform-gcp (main)
$ terraform apply
var.project
  GCP Project ID

  Enter a value: dtc-de-371802

google_storage_bucket.data-lake-bucket: Refreshing state... [id=dtc_data_lake_dtc-de-371802]
google_bigquery_dataset.dataset: Refreshing state... [id=projects/dtc-de-371802/datasets/trips_data_all]

No changes. Your infrastructure matches the configuration.

Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are
needed.

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

- The GCP configuration can be seen in my terraform files. I did not save the output the first time...
#

## Prepare Postgres 

Run Postgres and load data as shown in the videos

We'll use the yellow taxi trips from January 2021:

```bash
wget https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv
```

You will also need the dataset with zones:

```bash 
wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
```

Download this data and put it to Postgres

## Question 3. Count records 

- How many taxi trips were there on January 15?

`SELECT COUNT(*)
FROM yellow_taxi_trips
WHERE TEXT(tpep_pickup_datetime) LIKE '2021-01-15%';
`

RESULT = 53024 

## Question 4. Largest tip for each day

Find the largest tip for each day. 
On which day it was the largest tip in January?
Use the pick up time for your calculations.

`SELECT date_trunc('day', tpep_pickup_datetime) AS pickup_day, MAX(tip_amount) AS max_tip
FROM yellow_tripdata_2021_01
GROUP BY pickup_day
ORDER BY max_tip DESC
LIMIT 1;
`

RESULT = 2021-01-20 

## Question 5. Most popular destination
NOT RUNNING

What was the most popular destination for passengers picked up 
in central park on January 14?
Use the pick up time for your calculations.
Enter the zone name (not id). If the zone name is unknown (missing), write "Unknown" 

SELECT COALESCE(dozones.zone, 'Unknown') AS zone, 
COUNT(*) AS cant_trips
FROM taxi

INNER JOIN zones AS puzones
ON "PULocationID" = "LocationID"

LEFT JOIN zones AS dozones
ON "DOLocationID" = "dozones.locationid"

WHERE puzones.zone ILIKE '%central park%'
AND tpep_pickup_datetime::date = '2021-01-14'
GROUP BY 1
ORDER BY cant_trips DESC
LIMIT 1;


## Question 6. Most expensive locations
NOT RUNNING


What's the pickup-dropoff pair with the largest 
average price for a ride (calculated based on `total_amount`)?
Enter two zone names separated by a slash
For example:
"Jamaica Bay / Clinton East"
If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East".

select concat(coalesce(puzones.zone, 'Unknown'), '/', coalesce(dozones.zone, 'Unknown')), avg(total_amount) as avg_price_ride
from taxi

left join zones as puzones
on taxi.pulocationid = puzones.locationid
left join zones as dozones
on taxi.dolocationid = dozones.locationid
group by 1
order by avg_price_ride desc
limit 1;