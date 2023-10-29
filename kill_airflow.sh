kill -9 `ps aux | grep airflow | awk ‘{print $2}’`

