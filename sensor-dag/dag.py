from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor

def process_file():
    # Code to process the file once it exists
    print("Processing file...")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
}

with DAG('sensor_example', default_args=default_args, schedule_interval=None) as dag:
    # Define a FileSensor to wait for a file to be present
    file_sensor = FileSensor(
        task_id='wait_for_file',
        filepath='/path/to/file.csv',
        poke_interval=60,  # Check for the file every 60 seconds
    )

    # Define a PythonOperator to process the file
    process_task = PythonOperator(
        task_id='process_file',
        python_callable=process_file,
    )

    # Set the dependencies between tasks
    file_sensor >> process_task
