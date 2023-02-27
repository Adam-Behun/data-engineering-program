# Data Warehouse

# OLTP and OLAP

- OLAP = Online analytical processing
- OLTP = Online transactional processing

- Many companies have OLTP (processing massive number of transactions) to provide data to OLAP (providing data for data analysts)
- Manage daily transactions or have single platform for all my data

## OLAP
- BI, financial analysis, data from a structured warehouse
- OLAP Cube
  - Allowing quick queries

## OLTP
- Real-time execution of transactions - ATM, password changes
- Relational Database processing relativelly large volume of transactions
- Multi users and indexed datasets 


# BigQuery
- Serverless data warehouse with two parts - Replicated distributed storage and High-available cluster compute (Dremel)
- Google File System (2003) inspired Hadoop
- Colossus (2010) - Google Cloud Storage and BIgQuery
    - Internals - https://www.youtube.com/watch?v=eduHi1inM4s&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=25&ab_channel=DataTalksClub%E2%AC%9B

## Storage

- BigQuery is an analytical tool using columnar storage which makes it fast in aggregations 
- Capacitor as the file format that reorders the rows
- Colossus - distributed file system
- Storage optimization
  - Partitioning based on:
      - Ingestion time
      - Date-TimeStamp Column
      - Integer column
  - Clustering
    - Sorting tables based on particular columns (max=4)

## Processing in BigQuery
- High-available cluster compute (Dremel)
- Distributed
- Query your data in BQ means
  - API request management
  - Lexing and parsing SQL
  - Catalog resolution
  - Query Planning
  - Query Plan execution
  - Scheduling and dynamic planning
  - Finalized results


## ML in BigQuery
- feature auto and manual preprocessing 
- multi-hot encoding

# Tensorflow

# Postman