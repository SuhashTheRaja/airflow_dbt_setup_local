from airflow.sdk import dag, task
from datetime import datetime   

@dag(
    dag_id="second_learning_dag",
    description="This is my second learning DAG",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def second_learning_dag():

    @task
    def print_hello():
        return "Hello World!"

    @task
    def print_goodbye(message: str):
        print(f"Goodbye World! {message}")

    @task
    def print_greetings():
        print(f"Greetings! Learner!!")

    @task
    def print_greetings2():
        print(f"I'm the last task!!")

    task1 = print_hello()
    task2 = print_goodbye(task1)
    task3 = print_greetings()
    task4 = print_greetings2()

    task1 >> task3
    [task2,task3] >> task4

    # TaskFlow automatically passes task1's return value to task2
    # through XCom and establishes the dependency between the tasks.
second_learning_dag()
