export MLFLOW_REGISTRY_URI=mlflow
mlflow server --host 0.0.0.0 --port 5000 \
--backend-store-uri sqlite:///${MLFLOW_REGISTRY_URI}/mlflow.db \
--default-artifact-root ${MLFLOW_REGISTRY_URI} \
--gunicorn-opts "-D"

