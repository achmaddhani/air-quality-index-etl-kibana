# Air Quality Index (AQI) Monitoring Pipeline 🌍

## Objective 🎯

### Overall
The AQI Monitoring Pipeline is crucial for evaluating and overseeing air pollution levels, as indicated by the Air Quality Index (AQI). As pollution intensifies, the AQI rises, posing substantial health threats to residents. This initiative offers a systematic method to gather, process, and display air quality data, aiding in public health decision-making and policy development.

### ETL Process
The ETL component is essential for compiling air quality data from various sources, refining it for analytical use, and loading it into a database or dashboard for real-time observation. This enables environmental agencies and the public to efficiently react to fluctuations in air quality.

## Workflow 🔄

1. **Jupyter**: Loading data from SQL Database
2. **Jupyter**: Crafting Functions for ETL
3. **Jupyter**: Validating the cleansed file with Great Expectations
4. **Docker**: Establishing container environment
5. **Airflow**: Executing DAG functions
6. **Kibana**: Undertaking Exploratory Data Analysis and Visualization

## Libraries 📚

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

## ETL Conclusion 🛠️

Through standardization, elimination of duplicates, and data type adjustments, a robust dataset cleaning process has been established. Missing 'country' values are filled using the Geoname API, while extraneous city entries are removed to preserve data integrity. The ETL functions, automated through Docker and Airflow for 6:30 AM WIB, streamline the data pipeline, with Great Expectations ensuring data quality. Future versions aim to lessen missing values, particularly location-related, to enhance efficiency and reduce reliance on APIs.

## Kibana Objective 📊

This Kibana analysis seeks to provide insights to support public health advisories, help tourists make safer travel choices worldwide, and assist policymakers and environmental agencies in focusing interventions to ameliorate air quality in the most impacted regions in Indonesia.

## Kibana Conclusion 📈

The visualizations reveal that although half of the cities maintain acceptable AQI levels, an alarming 12% endure unhealthy air conditions. Supported by data from the EPA and New York State Department of Health, the findings emphasize the critical need to enhance air quality in 26% of Indonesian cities, including Jakarta, which likely affects nearby areas. Expanding future analyses to specific city sections could yield more detailed insights for targeted local interventions.