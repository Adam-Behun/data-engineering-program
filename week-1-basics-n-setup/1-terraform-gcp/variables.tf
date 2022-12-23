locals {
    data_lake_bucket = "dtc_data_lake"
}

variable "project" {
    description = "GCP Project ID"
}

variable "region" {
    description = "Region for resources"
    default = "us-central1"
    type = string
}

variable "storage_class" {
    description = "Storage class for your bucket"
    default = "STANDARD"
}

variable "BQ_DATASET" {
    description = "BigQuery dataset that raw data will be written to"
    type = string
    default = "trips_data_all"
}

variable "TABLE_NAME" {
    description = "BigQuery Table"
    type = string
    default = "ny_trips"
}