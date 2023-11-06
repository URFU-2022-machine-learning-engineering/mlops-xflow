import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import mlflow
from settings import DATASETS_PATH, SCRIPTS_PATH, MODELS_PATH, ML_FLOW_TRACKING_URI

mlflow.set_tracking_uri(ML_FLOW_TRACKING_URI)
mlflow.set_experiment("train_model")

def load_data():
    df = pd.read_csv(f"{DATASETS_PATH}/data_train.csv", header=None)
    df.columns = ['id', 'counts']
    return df

def train_model(df):
    model = LinearRegression()
    model.fit(df['id'].values.reshape(-1,1), df['counts'])
    return model

def save_model(model):
    with open(f'{MODELS_PATH}data.pickle', 'wb') as f:
        pickle.dump(model, f)

def log_metrics(model):
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, artifact_path="lr", registered_model_name="lr")
        mlflow.log_artifact(local_path=f"{SCRIPTS_PATH}/train_model.py", artifact_path="train_model code")
        mlflow.end_run()

if __name__ == "__main__":
    df = load_data()
    model = train_model(df)
    save_model(model)
    log_metrics(model)

 