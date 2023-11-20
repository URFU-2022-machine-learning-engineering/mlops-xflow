import pandas as pd
import numpy as np

from settings import DATASETS_PATH 

# Загрузка обработанных данных
df = pd.read_csv(f'{DATASETS_PATH}data_processed.csv', header=None)

# Разделение данных на обучающую и тестовую выборки
idxs = np.array(df.index.values)
np.random.shuffle(idxs)
l = int(len(df)*0.7)
train_idxs = idxs[:l]
test_idxs = idxs[l+1:]

# Запись данных
df.loc[train_idxs, :].to_csv(f'{DATASETS_PATH}data_train.csv',
                        header=None,
                        index=None)
df.loc[test_idxs, :].to_csv(f'{DATASETS_PATH}data_test.csv',
                        header=None,
                        index=None)
