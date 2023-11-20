from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime as dt

from settings import SCRIPTS_PATH
 
args = {
    "owner": "dzailz",
    "start_date": dt.datetime(2023, 10, 28),
    "retries": 1,
    "retry_delays": dt.timedelta(minutes=1),
    "depends_on_past": False
}

# Определение DAG с идентификатором "youtube_comments_score"
# и установка параметров и расписания выполнения
with DAG(
    dag_id="youtube_comments_score",
    default_args=args,
    schedule_interval=None,
    tags=["youtube", "score"],
) as dag:
    # Определение задач
    get_data = BashOperator(task_id="get_data",
                            bash_command=f"python3 {SCRIPTS_PATH}get_data.py",
                            dag=dag)
    process_data = BashOperator(task_id="process_data",
                            bash_command=f"python3 {SCRIPTS_PATH}process_data.py",
                            dag=dag)
    train_test_split_data = BashOperator(task_id="train_test_split_data",
                            bash_command=f"python3 {SCRIPTS_PATH}train_test_split_data.py",
                            dag=dag)  
    train_model = BashOperator(task_id="train_model",
                            bash_command=f"python3 {SCRIPTS_PATH}train_model.py",
                            dag=dag)
    test_model = BashOperator(task_id="test_model",
                            bash_command=f"python3 {SCRIPTS_PATH}test_model.py",
                            dag=dag)

    # Определение порядка выполнения задач
    get_data >> process_data >> train_test_split_data >> train_model >> test_model
