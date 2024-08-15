# Brazilian Customers Orders ETL Pipeline and API
This project creates an ETL (Extract, Transform, Load) workflow for Olist's Brazilian E-Commerce Public Dataset. It employs Polars for data manipulation and DuckDB as the target data store. The complete process—including data intake scripts, unit tests, and the DuckDB database—is packaged in Docker containers to facilitate deployment and scaling. The Docker setup is engineered to extract the data and offer a command-line interface (CLI) for running queries against the data using DuckDB.

## Features

- Harvesting data from various CSV files within the Olist dataset
- Reshaping and structuring data to form dimensional and fact tables
- Conducting sophisticated data analysis to produce informative summary tables
- Populating a DuckDB database with the processed data
- Implementing thorough unit testing for data preparation and database functions
- Encapsulating the entire ETL workflow in Docker for consistency and easy deployment
- Creating a Flask API that helps load,retreive and process Data.
Deployment to an AWS EC2 instance

# Prerequisites

- Docker and Docker Compose
- Git
- FLASK
- SWAGGER
- AWS 

Output Tables
The pipeline generates the following analytical and aggregate tables in DuckDB
fact_table
top_loyal_customers
top_sellers

Project Structure

customer_orders_analysis/
├── data/
│   └── orders.csv
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── processing.py
│   ├── api.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_database.py
│   ├── test_processing.py
│   └── test_api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md

