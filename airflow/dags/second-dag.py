from airflow import DAG
from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator  
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id="second_dag",
    start_date=datetime(2026, 10, 22),
    schedule=None
):

    task_1 = BashOperator(
        task_id="task_numero_uno",
        bash_command="echo 'Isso é a nossa segunda tarefa do Airflow'"
    )

    def message():
        print("Lets go to the next task")

    task_2 = PythonOperator(
        task_id="task_numero_dos",
        python_callable=message
    )

    task_1 >> task_2