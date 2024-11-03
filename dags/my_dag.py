from airflow import DAG
from datetime import datetime, timedelta

with DAG(
    dag_id='meqlad',
    description="this is my first dag",
    start_date=datetime.now(),
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=5),
    tags=['data engineering']
) as dag:
    None