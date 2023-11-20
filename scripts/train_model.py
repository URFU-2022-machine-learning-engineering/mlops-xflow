from sklearn.linear_model import LinearRegression
import pickle
import mlflow

import pandas as pd
 

from settings import DATASETS_PATH, SCRIPTS_PATH, MODELS_PATH, ML_FLOW_TRACKING_URI

# Установка URI для отслеживания экспериментов в MLflow
mlflow.set_tracking_uri(ML_FLOW_TRACKING_URI)
mlflow.set_experiment("train_model")

# Загрузка данных для обучения модели
df = pd.read_csv(f'{DATASETS_PATH}data_train.csv', header=None)
df.columns = ['id', 'counts']
model = LinearRegression()

# Запуск нового эксперимента в MLflow
with mlflow.start_run():
    mlflow.sklearn.log_model(model,
                             artifact_path="lr",
                             registered_model_name="lr")
    mlflow.log_artifact(local_path=f"{SCRIPTS_PATH}train_model.py",
                        artifact_path="train_model code")
    mlflow.end_run()

# Обучение модели на данных и сохранение её в файл 'data.pickle'
model.fit(df['id'].values.reshape(-1,1), df['counts'])
with open(f'{MODELS_PATH}data.pickle', 'wb') as f:
    pickle.dump(model, f)
 
