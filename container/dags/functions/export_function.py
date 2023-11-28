import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# exporting to elasticsearch DAG
def export_elastic():
    es = Elasticsearch(hosts=["http://elasticsearch:9200"])

    df = pd.read_csv('/opt/airflow/data/P2M3_dhani_data_clean.csv')
    actions = [
        {
            "_index": "milestone3_dhani_data_clean",
            "_source": row.to_dict()
        }
        for i, row in df.iterrows()
    ]
    bulk(es, actions)
