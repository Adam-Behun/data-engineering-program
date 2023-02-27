# Data processing

Data exchange and its communication channels - remember the example of a postal service
Computers just use zeros and ones 

## Latency 

- time that it takes from source to destination
- low latency means that we can make faster decisions such as recommendation systems and systems where we need to access the data ASAP 

# Batch processing

* Takes large volumes of the data at a scheduled time
* 80% of data processing is done using batch

Problem was that unstructured large data sets were difficult to process
One machine takes a lot of time
Hadoop is a framework that gives me the capability of parallel processing:
- Distributed File System - HDFS stores the data
- MapReduce processes the data
- Yarn package manager storing all dependencies locally
- Open-source - you have to buy the machines in order to build an HDFS, the software framework is free

## Distributed file systems

- Parallel processing
  - Network bandwidth
- Different physical machines connected over a network
  - Each machine has local physical file system
  - Distributed file system (DFS) means it is not physical
  - Cluster is machines connected over a network
    - Master remembers the metadata of the other nodes
    - Replication factor - block are replicated in different nodes
  
## MapReduce

- Map (Divide) and Reduce (Conquer)
- actual parallel processing with Hadoop
- job scheduling and tracking job progress
- arrived at yet another computational limits
- moved to yarn - MapReduce version 2

## Yarn

- splits map and reduce into resource manager and application master
- central resource manager
- package manager making stuff much faster and dependencies available offline


# Hadoop and Spark
- Hadoop is older
- Spark runs faster but requires more RAM
- Hadoop runs in batches (think of it as queues), but spark does batch, real-time, and graph
- Hadoop is complex to code, spark is relativelly simple
- Spark has built-in ML library

Spark does not have storage.
It is common to use HDFS as a file system and Spark as the processor.
You can deploy Spark to an RDBMS.

## Spark

- Data processing framework faster than Hadoop
- In-memory processing - understand RAM and cache
- Streaming and real-time processing
- Ability to work in many different languages
- Resilient Distributed Datasets
- Directed Acyclic Graph
- Ability to process structured, and unstructured data

### RDDs as Spark's data structure

- Immutable, distributed collection of objects that can be operated on in parallel
- You can do queries on RDDs and those can return new RDDs or results
- Transformations and actions

### Directed Acyclic Graph
- Represent the relationship between different entitites
- Different processing steps in the process
- Set of vertices and edges connecting them, there are no edges
- Spark divides the entire computation into stages represented by DAGs
- DAGs allow Spark to work efficiently in a distributed environment

### Spark components
- Spark core - base engine which has RDDs
- Spark SQL
- Spark Streaming
- MLlib
- GraphX - data represented naturally by a network

### Spark-SQL
- data is stored in a RDBMS and they use spark to process the data
- reads from csv, json, jdbc
- Dataframe DSL

### Spark streaming
- real-time processing of what the recommendations are for the customer
- processes the data as they come in - clicks of a customer for example

### Spark MLlib
- Spark for processing and libraries for ML work, clustering, supervised, unsupervised learning

### GraphX
- Data naturally in a network like Facebook, LinkedIn data

### Spark Cluster Managers
- Spark stand-alone mode
- Mesos
- Hadoop Yarn
- Kubernetes


### Applications of Spark
- Real-time processing for banking industry
- Alibaba real-time recommendations
- Iqvia analysing patients based on mdeical history
- Netflix user recommnedations