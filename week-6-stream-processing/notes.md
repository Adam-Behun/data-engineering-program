# Data processing

Data exchange and its communication channels - remember postal Service
Computers use APIs 
Why do we need streaming for data? Is batch not good enough?


# Kafka

- Different configurations based on what the data and the task looks like. 
- This is the basics:
    Cluster (set of nodes), topic (collection of events), messsages inside the topic (key, value, timestamp), storing and replications, retention, partitions and paralization, producing, consuming (consumer groupid), offset (moving the pointer further), acknowledgment

Kafka Topic
- sequence of events coming in
- continous stream of events. Following the temperature of a room every 30 seconds - events across time go into the topic

Kafka replications
- topic will be in both nodes

Consumers, producers, leaders, followers

Kafka retention
- how long will Kafka keep the data?
- limited amount of memory

Partitions
- data stores topics in nodes
- partitions divide the data


Kafka Cluster 
- machines running Kafka
- it used zookeeper for this before
- now they use Kafka's internals - topic

Kafka Logs 
- data stored in a topic

Messages with Kafka
- Key
- Value
- Timestamp

Offset
- Auto offset-reset

Acknowledgment
- fire and forget or others


Kafka is used because
- Robustness, scalability, and flexibility

Kafka CDC

Kafka stream Join

Unit testing

Stream windowing
- tumbling
- hopping
- sliding
- session

Ksqldb and connect
- You can run queries on the incoming data
- It is better to use as much Java as possible
- Used for quick testing, analysis, before you build a stream application
- Persistent data 
- It runs on a different node

Schema registry
- cotract between the producers and consumers
- dictionary to encode and decode messages for producers and consumers

Compatibility
- forward compatible
- backward compatible
- fully compatible

Avro
- data serialization format making producers and consumers compatible
- Avro is the communication layer between them
- reads as simple as json for human but the date is in binary format so it is really efficient

What is gradlew?


Horizontal and vertical scale

Broadcasting

Global KTable

Kafka Connect