## Learnings, code, problems encountered, solutions
- Docker, Jupyter, command line, mingw, gitbash, environment variables, http server from python   
- The task is to ingest data into PostgreSQL and explore the dataset

# Data pipeline

`A data pipeline is a set of processes that move data from one place to another. This typically involves extracting data from a source, transforming the data to fit the desired format or structure, and loading the data into a destination such as a database or data warehouse.`

## E - extracting

`Data extraction refers to the process of pulling data from one or more sources and making it available for further processing or analysis. This typically involves connecting to the source system, querying the data using a specific set of criteria, and extracting the data in a format that can be easily transported and transformed. The extracted data is often stored in a temporary location such as a staging area or buffer, from which it can be further processed and loaded into the destination.`

## T - transforming

`In the context of a data pipeline, data transformation refers to the process of converting the data from its raw, extracted form into a format that is more suitable for the intended use of the data.
`

* Removing or replacing missing or invalid data

* Standardizing and normalizing data values (e.g. converting all dates to a consistent format)

* Joining or merging data from multiple sources

* Aggregating or summarizing data (e.g. computing sums, averages, or counts)

* Applying specific rules or business logic to transform the data (e.g. calculating discounts or applying tax rates)

* Encoding or decoding data (e.g. applying a hash function to encrypt sensitive data)

## L - loading
` The process of transferring the transformed data from the pipeline into the final destination. This typically involves writing the data to a persistent storage system such as a database, data warehouse, or data lake, in a format that can be easily accessed and queried by downstream processes and applications. It is also typically the final step in the data pipeline process, and marks the point at which the data is considered to be "loaded" and ready for use.`

# Data warehouse

`Data warehouses are different from operational databases, which are used to store and manage current data for day-to-day operations. Data warehouses are designed to store large amounts of data that is extracted from operational databases, as well as from other sources such as text files and external databases. The data is then cleaned, transformed, and integrated into a consistent format, and loaded into the data warehouse. This allows users to access and analyze the data in a consistent and efficient way, without impacting the performance of the operational systems.`

# Data lake

`A data lake is a type of repository or storage system that is designed to store and manage large volumes of raw, unstructured data. Data lakes are often used in conjunction with data pipelines and other tools to extract, transform, and load data from a variety of sources. The raw data is then stored in the data lake `

# Pros and Cons -- Data lake

### Pros of a data lake:

* Flexibility: Designed to store data in its raw, unstructured form, without applying any schema or transformation to the data

* Scalability: Built using distributed systems and cloud technologies, which allows them to store and process large volumes of data

* Cost-effectiveness: They leverage the scale and efficiency of cloud computing to store and process data at a lower cost and open-source technologies

### Cons of a data lake:

* Complexity: Can be complex to set up and manage, especially for users who are not familiar with distributed systems, cloud computing, and big data

* Quality: Data lakes are designed to store data in its raw, unstructured form, without applying any cleansing, transformation, or validation to the data

* Governance: Variety of users and applications can make it difficult to manage data governance policies, such as data security, privacy, and compliance

# Pros and Cons -- Data warehouse

### Pros of a data warehouse:

* Structure: Data warehouses are designed to store structured, cleansed data that is ready for analysis and reporting

* Performance: Optimized for complex, ad-hoc queries and can use advanced indexing and query optimization techniques to deliver fast and efficient results

* Governance: Data warehouses are typically designed to support data governance policies, such as data security, privacy, and compliance

### Cons of a data warehouse:

* Lack of Flexibility: Designed to store structured data, which means that the schema and structure of the data must be defined in advance

* Cost: Can be expensive to set up and maintain, especially if they use proprietary technologies and require specialized skills and expertise

* Scalability: Designed to store and process large volumes of structured data can make them less scalable and efficient than data lakes

# Summary of data lakes vs data warehouses

`Data lakes provide flexibility and scalability, but can be complex and difficult to ensure data quality, while data warehouses provide structure and performance, but can be inflexible and expensive.`

## Conjunction of data lake and data warehouse infrastructure

`Data is typically extracted from a variety of sources, and is then transformed and cleansed in a data lake before being loaded into a data warehouse. The data warehouse is then used to store and manage the structured data, and to support complex queries and analysis on the data.`

### Benefits:

* Flexibility: Data lake allows users to store and process data in its raw, unstructured form, without the need to pre-define the schema of the data

* Scalability: Data lake is typically built using distributed systems and cloud technologies, which allows it to store and process large volumes of data

* Governance: Data warehouse provides a centralized and structured repository for the data making it easier to manage data security, privacy, and compliance

# Docker

`Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, it ensures that the application will run reliably on any other machine, regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.`

- Docker container
- Docker image
- Dockerfile
- Docker Compose
  - Run just one program and that starts the two containers
  - pgdatabase and pgadmin images
  - have it saved in vs code and run --> docker-compose up -d
  - localhost:8080 in a browser

# File formats to know

## YAML

YAML files are commonly used in applications that need to represent complex data structures in a simple and human-readable way. They are often used as configuration files for applications, because the simple syntax and indentation-based structure make them easy to read and edit.

## CSV

A CSV (comma-separated values) file is a type of plain text file that stores tabular data in a simple, human-readable format. Each line of the file represents a single row of data, and the values within each line are separated by commas.

## JSON

A JSON (JavaScript Object Notation) file is a type of plain text file that is used to store data in a structured, human-readable format. JSON files use a standard syntax for representing data in key-value pairs.
- application 
- name-value pairs -- object
- ordered list od values

## Avro
- row oriented storage format
- schema is stored as JSON within file
- ideal for write heavy operations
- excellent for entire row consumption and processing

## ORC
- column oriented file storage
- schema is stored in the footer of the file
- schema is limited to adding new columns
- works well with Hive

## Parquet
- column oriented storage format
- schema is stored in the footer of the file
- processing parquet files outputs multiple files
- due to merging of files across multiple files, schema evolution is more expensive
- ideal for read heavy operations
- works great with spark

## XML
- verbose and redundant markup language
- high storage costs
- doe not support an array


# Jupyter notebook

## Jupyter 

`Jupyter Notebook is a web-based interactive computing platform that allows users to create and share documents that contain live code, equations, visualizations, and narrative text. It is commonly used for data cleaning and transformation, numerical simulation, statistical modeling, data visualization, and machine learning.`

# PostgreSQL

## PostgreSQL

`PostgreSQL is a powerful, open-source, object-relational database management system (ORDBMS) that is widely used for managing large datasets. One of the main advantages of PostgreSQL over other relational database management systems is its ability to handle a wide variety of workloads.`

## Object-relational database

`An object-relational database (ORDBMS) is a type of database management system (DBMS) that combines the features of a relational database, which uses tables and rows to store data, with the features of an object-oriented database, which uses objects and classes to represent data. In an ORDBMS, data is stored in the form of objects, and those objects can be related to each other using the same kind of relationships that exist between objects in an object-oriented programming language. This allows for more flexibility and complexity in data modeling, making ORDBMSs well-suited for applications that require complex data structures or need to store data that doesn't fit neatly into a traditional relational database structure. Some examples of ORDBMSs include PostgreSQL, Oracle Database, and IBM DB2.`

## SQL Joins 

In SQL, a join is a way to combine data from two or more tables based on a common attribute.
- INNER JOIN
- OUTER JOIN
- LEFT JOIN
- RIGHT JOIN

# Terraform

`Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. It is an open-source tool that allows users to define and provision a datacenter infrastructure using a high-level configuration language, known as HashiCorp Configuration Language (HCL). This infrastructure can be represented as "infrastructure as code".`

## Infrastructure as code

`Infrastructure as code (IAC) is a way of managing and provisioning infrastructure using code and automation tools, rather than manually configuring resources through a web-based interface or a set of command-line tools. With IAC, the infrastructure is defined and managed using code, which allows it to be treated like any other codebase and managed using the same version control and collaboration tools. This makes it easier to manage and maintain the infrastructure over time, and also allows for more efficient and repeatable provisioning of resources.`

## Terraform's commands

- terraform init -- initialize and install
- terraform plan -- match changes against the previous state
- terraform apply -- apply changes to cloud
- terraform destroy -- remove your stack from cloud