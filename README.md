# Air Quality Index (AQI) Monitoring Pipeline

## Objective

### Overall
The AQI Monitoring Pipeline is designed to assess and monitor air pollution levels, represented by the Air Quality Index (AQI). As air pollution levels rise, so does the AQI, which can pose significant health risks to residents. This project provides a systematic approach to collect, transform, and present air quality data, aiding in public health decision-making and policy formulation.

### ETL Process
The ETL component is vital for aggregating air quality data from different sources, processing it for analytical purposes, and loading it into a database or dashboard for real-time monitoring. This facilitates environmental agencies and the public to effectively respond to air quality fluctuations.

## Workflow

1. **Jupyter**: Loading data from SQL Database
2. **Jupyter**: Creating Functions for ETL
3. **Jupyter**: Validating the cleaned file with Great Expectations
4. **Docker**: Setting up container environment
5. **Airflow**: Executing DAG functions
6. **Kibana**: Conducting Exploratory Data Analysis and Visualization

## Libraries

```python
# SQL import
import psycopg2
from sqlalchemy import create_engine
# Tools
import pandas as pd
import numpy as np
import requests
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from great_expectations.data_context import FileDataContext
```

## ETL Conclusion

Through normalization, removing duplications, and data type corrections, i have established a robust dataset cleaning process. Missing 'country' values are imputed using the Geoname API, while redundant city entries are dropped to maintain data integrity. The ETL functions, scheduled via Docker and Airflow for 6:30 AM WIB, automate the data pipeline, with Great Expectations confirming the data quality. Future iterations will focus on minimizing missing values, especially those related to location, to improve efficiency and reduce API dependency.

## Kibana Objective

This Kibana analysis aims to provide insights that can inform public health recommendations, guide tourists in making safer travel decisions around the world, and assist policymakers and environmental agencies in targeting interventions to improve air quality in the most affected regions in Indonesia.

## Kibana Conclusion

The visualizations indicate that while half of the cities maintain satisfactory AQI levels, a troubling 12% experience unhealthy air conditions. The data, corroborated by the EPA and New York State Department of Health, underscores the urgency of improving air quality in 26% of Indonesian cities, including Jakarta, which potentially influences surrounding regions. Expanding future analyses to city subsections could provide deeper insights for localized intervention strategies.