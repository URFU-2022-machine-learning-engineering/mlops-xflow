import pandas as pd
import mlflow
import os

from settings import DATASETS_PATH, BASIC_PATH, ML_FLOW_TRACKING_URI, SCRIPTS_PATH
os.environ["MLFLOW_REGISTRY_URI"] = f"{BASIC_PATH}mlflow/"
mlflow.set_tracking_uri(ML_FLOW_TRACKING_URI)
mlflow.set_experiment("process_data")

df = pd.read_csv(f'{DATASETS_PATH}data.csv', header=None)

with mlflow.start_run():
   df[0] = (df[0] - df[0].min()) / (df[0].max() - df[0].min())

   with open(f'{DATASETS_PATH}data_processed.csv', 'w') as f:
      for i, item in enumerate(df[0].values):
            f.write("{},{}\n".format(i, item))

   mlflow.log_artifact(local_path=f"{SCRIPTS_PATH}process_data.py",
                           artifact_path="process_data code")
   mlflow.end_run()

