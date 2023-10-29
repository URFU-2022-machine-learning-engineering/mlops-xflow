cd /home/dzailz/project/ || exit 1
source venv/bin/activate
export AIRFLOW_HOME=/home/dzailz/project/airflow

airflow webserver -p 8080 -D
airflow scheduler -D
