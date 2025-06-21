from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.fetch_weather import fetch_weather

with DAG("weather_pipeline",
         start_date=datetime(2024, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:

    fetch_task = PythonOperator(
         task_id="fetch_weather_data",
         python_callable=fetch_weather
    )

    fetch_task