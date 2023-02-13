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

Resilient Distributed Datasets (RDD)

Dataframes, RDDs, partitions, parallel computing (processing), distributed data, map partition

lambda function

why jupyter and not just python
what's the difference between jupyter and ipython

what is java

data structures -- RDD

what are the different nodes within spark - paralel computing
what are the different data structures and algorithms used in the backend
why do we actually need this? Parallel processing? Partitioning?

Where are the executors of the spark framework? Is this VMs? 

ML in pandas

Spark internals - clusters

what are internals and clusters

stand-alone mode


# NOTES:

I cannot execute this command while creating a Local Spark Cluster:
min --> 2:13
https://www.youtube.com/watch?v=HXBwSlXo5IA&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=54&ab_channel=DataTalksClub%E2%AC%9B

## I tried to install older version of java

Set up env. variables
SPARK_HOME and JAVA_HOME
I might have to go through the installation of hadoop, spark, and java again

## Error Message:

failed to launch: nice -n 0 C:\apps\spark-3.0.3-bin-hadoop3.2/bin/spark-class org.apache.spark.deploy.master.Master --host --port 7077 --webui-port 8080
  Spark Command: C:\apps\jdk-11.0.13\bin\java -cp C:\apps\spark-3.0.3-bin-hadoop3.2/conf\;C:\apps\spark-3.0.3-bin-hadoop3.2\jars\* -Xmx1g org.apache.spark.deploy.master.Master --host --port 7077 --webui-port 8080
  ========================================
  C:\apps\jdk-11.0.13\bin\java -cp "C:\apps\spark-3.0.3-bin-hadoop3.2/conf\;C:\apps\spark-3.0.3-bin-hadoop3.2\jars\*" -Xmx1g org.apache.spark.deploy.master.Master --host --port 7077 --webui-port 8080
  C:\apps\spark-3.0.3-bin-hadoop3.2/bin/spark-class: line 96: CMD: bad array subscript
full log in C:\apps\spark-3.0.3-bin-hadoop3.2/logs/spark--org.apache.spark.deploy.master.Master-1-Nope.out