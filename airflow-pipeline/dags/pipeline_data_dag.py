from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from pathlib import Path


base_path = "~/NoCountry/velarion_fintech/"

project_ariflow = Path(__file__).resolve().parent

with DAG(
    dag_id="load_data_pg_pipeline",
    start_date=datetime.today(),
    schedule_interval=None,
    catchup=False,
    tags=["data", "churn", "load"],
) as dag:

    data_preprocessing = BashOperator(
        task_id="data_preprocessing",
        bash_command=f"python3.10 {base_path}data_preprocessing.py"
    )

    load_pg = BashOperator(
        task_id="load_database",
        bash_command=f"python3.10 {project_ariflow}/load_database.py"
    )


    data_preprocessing >> load_pg
