# Batch processing

# Data processing 
* Batch
  * takes all the data for a day for example at once 
  * daily and hourly
  * 80% used batch
* Streaming
  * one ride gets processed right away, separatelly 


## Tech used for batch processing
* Python
* SQL
* Spark
* Flink
* Using Airflow to orchestrate the workflow
### Advantages
* simplicity, retry, scale 
### Disadvantages
* Delay 


## Spark
* Batch jobs as well as streaming
* Engine
* Cluster
* Multi-language --> wrapper for python is called PySpark
* Spark is Scala-native
* Raw data -> SQL, Athena -> Spark -> Python train ML

* Other tech: Hive, Presto, Athena

* Spark partitions

* Lazy commands

## Hadoop

Hadoop and hdfs are not as popular anymore thanks to the cloud tech nowadays. 