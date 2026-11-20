from datetime import datetime

from airflow import DAG
from airflow.providers.databricks.operators.databricks import (
    DatabricksRunNowOperator,
)

with DAG(
    dag_id="databricks_test_job",
    description="Trigger an existing Databricks job",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["databricks", "test"],
) as dag:

    trigger_databricks_job = DatabricksRunNowOperator(
        task_id="trigger_databricks_job",
        databricks_conn_id="Databricks_rsuhash",
        job_id=1076451426290534,
        wait_for_termination=True,
    )
    