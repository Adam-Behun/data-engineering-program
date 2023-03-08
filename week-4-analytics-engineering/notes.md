* https://www.youtube.com/watch?v=uF76d5EmdtU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=29&ab_channel=DataTalksClub%E2%AC%9B
* https://www.youtube.com/watch?v=4eCouvVOJUw&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=30&ab_channel=DataTalksClub%E2%AC%9B
  
# Data Engineering Positions

Usually
- Data Engineer
    - Getting data into the warehouse
    - Little business logic
- Analytics Engineer
    - Create the core datasets
    - Business logic and software knowledge (testing and CI/CD)
- Analyst
    - Business logic and analysis
    - Dashboards

How much value are you providing?
What problems are you solving?
How difficult those problems are?
Do you like to work on infra or statistics? Business or software? What tools do you like to use

## Data structures --> data in databases --> query performance

Data structures determine how data is organized in the database and that determines query performance

# DBT
- taking this course
    - https://courses.getdbt.com/courses/fundamentals
- this is my repo:
    - https://github.com/Adam-Behun/dbt-training
## Data modeling

- Process of creating the data model before it is loaded to the warehouse
- It enforces the rules for the database - gives it the structure
- Data modeling needs to be done in databases as well as in visualization tools
- it is the architecture of how the data is stored and organized

## Kimball
- data warehousing methodology developed by Kimball
- bottom-up approach that emphasizes the dimensional modeling 
- TWO TYPES OF TABLES with The Kimball approach
    - fact tables containing quantitative data
    - dimension tables provide the content, the description
- denormalize the noramlized data because we need lots of joins from these separate (normalized) tables 
    - this was sueful when storage was expensive but "not anymore"
### Dimensional modeling
- what can be combined into dimensions and then connected t the fact tables?
- this depends on the business needs -- how do we need to pull the queries not to use joins
- minimize the amount of joins we need to create our dashboards

## Computer Architecture
- taking this course
    - https://www.coursera.org/learn/comparch
- will be found in my githhub: https://github.com/Adam-Behun

## Database management
- DDL
    - Data Definition Language used to create and modify the structure of database objects, such as tables, views, indexes, and constraints. DDL commands include CREATE, ALTER, and DROP
- DML
    - Data Manipulation Language used to manage the data stored in a database. DML commands include INSERT, UPDATE, DELETE, and SELECT.
- DWh
    - Data warehouse


## Looker studio for cloud and metabase for local visualizations