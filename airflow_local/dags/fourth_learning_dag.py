from airflow.sdk import dag, task
from datetime import datetime, timedelta


@dag(
    dag_id="retry_learning_dag",
    description="Learning task retries and failure handling",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
)
def retry_learning_dag():

    @task(
        retries=2,
        retry_delay=timedelta(seconds=10),
    )
    def extract_data():
        print("Attempting to extract data")

        raise ValueError("Simulated extraction failure")

    @task
    def process_data():
        print("Processing data")

    extract = extract_data()
    process = process_data()

    extract >> process


retry_learning_dag()