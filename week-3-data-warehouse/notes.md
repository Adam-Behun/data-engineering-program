# Notes for week 3 of Data Engineering Zoomcamp -> Data Warehouse


Slides: https://docs.google.com/presentation/d/1a3ZoBAXFk8-EhUsd7rAZd-5p_HpltkzSeujjRGB2TAI/edit#slide=id.p

## Topics covered

- cloud composer vs airflow vs kubernetes -> data workflow orchestration
- Moving from GCS to BQ
- Data Warehouse
- OLTP, OLAP
- BigQuery
- BigQuery public datasets, costs, partitioning and clustering and when to use each 
- Cost reduction and query performance

### Internals of BQ -> https://www.youtube.com/watch?v=eduHi1inM4s&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=25&ab_channel=DataTalksClub%E2%AC%9B
* look at references at the end
Storing is cheaper. computing is more expensive. 
record-oriented and column-oriented --> data structures
Aggregations

Dremel serving tree, leaf nodes

ML in BigQuery
- feature auto and manual preprocessing 
- multi-hot encoding

Tensorflow
Postman