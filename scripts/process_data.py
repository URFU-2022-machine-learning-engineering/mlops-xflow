import pandas as pd

from settings import DATASETS_PATH

# Загрузка данных
df = pd.read_csv(f'{DATASETS_PATH}data.csv', header=None)
 
df[0] = (df[0]-df[0].min())/(df[0].max()-df[0].min())

# Запись обработанных данных в новый файл
with open(f'{DATASETS_PATH}data_processed.csv', 'w') as f:
    for i, item in enumerate(df[0].values):
        f.write("{},{}\n".format(i, item))
