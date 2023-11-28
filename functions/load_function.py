import pandas as pd
from sqlalchemy import create_engine

# loading DAG
def loading_data():
    '''Load data from postgre container and saving it as a CSV file
    '''
    engine = create_engine('postgresql+psycopg2://achmaddhani:container@postgres:5432/milestone') # using 5432 port since airflow is in container
    df = pd.read_sql_table('table_m3', engine)
    df.to_csv('/opt/airflow/data/P2M3_Dhani_data_raw.csv', index=False) # saving raw data