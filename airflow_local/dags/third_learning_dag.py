from airflow.sdk import dag, task
from datetime import datetime, timedelta


@dag(
    dag_id="third_learning_dag",
    description="Learning task retries and timeouts",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
)
def third_learning_dag():

    @task(
        retries=2,
        retry_delay=timedelta(seconds=10),
        execution_timeout=timedelta(minutes=1),
    )
    def extract_data():
        print("Extracting data...")
        return 1500

    @task
    def process_data(record_count):
        print(f"Processing {record_count} records")

    count = extract_data()
    process_data(count)


third_learning_dag()