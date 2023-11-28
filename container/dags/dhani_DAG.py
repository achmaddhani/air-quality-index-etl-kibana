import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from functions.clean_function import cleaning_data
from functions.load_function import loading_data
from functions.export_function import export_elastic

default_args = {
    'owner': 'dhani',
    'start_date': dt.datetime(2023, 11, 23),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('ETL',
         default_args=default_args,
         schedule_interval='30 23 * * *', # schedule for 6:30 AM WIB
         ) as dag:
    
    data_load = PythonOperator(
        task_id='Fetch from Postgresql',
        python_callable=loading_data
    )

    data_clean = PythonOperator(
        task_id='Data Cleaning',
        python_callable=cleaning_data
    )

    data_export = PythonOperator(
        task_id='Post to Elasticsearch',
        python_callable=export_elastic
    )

    # order of execution
    data_load >> data_clean >> data_export
