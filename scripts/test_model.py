from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd

from ..settings import MODELS_PATH, DATASETS_PATH
 
df = pd.read_csv(f'{DATASETS_PATH}data_test.csv', header=None)
df.columns = ['id', 'counts']
 
model = LinearRegression()
with open(f'{MODELS_PATH}data.pickle', 'rb') as f:
    model = pickle.load(f)
 
score = model.score(df['id'].values.reshape(-1,1), df['counts'])
print("score=", score)
