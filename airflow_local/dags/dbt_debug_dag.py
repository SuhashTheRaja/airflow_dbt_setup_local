from datetime import datetime

from airflow import DAG
from airflow.exceptions import AirflowException
from airflow.operators.python import PythonOperator


def run_dbt_debug():
    import docker

    client = docker.from_env()

    try:
        # Connect to the existing dbt container.
        container = client.containers.get("dbt-container")

        # Verify that the container is running.
        container.reload()

        if container.status != "running":
            raise AirflowException(
                f"dbt-container is not running. "
                f"Current status: {container.status}"
            )

        # Execute dbt inside the dbt container.
        result = container.exec_run(
            cmd=[
                "dbt",
                "debug",
                "--project-dir",
                "/workspace/projects/test_1",
                "--profiles-dir",
                "/workspace/profiles",
            ],
            workdir="/workspace",
            stdout=True,
            stderr=True,
        )

        # Capture and display the command output in Airflow logs.
        output = result.output.decode(
            "utf-8",
            errors="replace",
        )

        print(output)

        # Fail the Airflow task if dbt returns a non-zero exit code.
        if result.exit_code != 0:
            raise AirflowException(
                f"dbt debug failed with exit code {result.exit_code}"
            )

        print("dbt debug completed successfully.")

    finally:
        client.close()


with DAG(
    dag_id="dbt_debug_in_container",
    description="Execute dbt debug inside the existing dbt container",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dbt", "databricks", "docker"],
) as dag:

    dbt_debug = PythonOperator(
        task_id="run_dbt_debug",
        python_callable=run_dbt_debug,
    )