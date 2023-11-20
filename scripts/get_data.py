import os
import mlflow
import requests
import json
from pyyoutube import Api
from settings import SCRIPTS_PATH, DATASETS_PATH, API_KEY, BASIC_PATH, ML_FLOW_TRACKING_URI

# Установка URI для отслеживания экспериментов в MLflow
os.environ["MLFLOW_REGISTRY_URI"] = f"{BASIC_PATH}mlflow/"
mlflow.set_tracking_uri(ML_FLOW_TRACKING_URI)
mlflow.set_experiment("get_data")

# Инициализация объекта API для доступа к YouTube Data API с использованием API-ключа
api = Api(api_key=API_KEY)

# Поиск видео по ключевым словам (query) с использованием YouTube Data API
query = "'Mission Impossible'"
video = api.search_by_keywords(q=query, search_type=["video"], count=10, limit=30)
maxResults = 100
nextPageToken = ""
s = 0

# Запуск MLflow эксперимента
with mlflow.start_run():
    for i, id_ in enumerate([x.id.videoId for x in video.items]):
        # Формирование URI для получения комментариев к видео с использованием YouTube Data API
        uri = "https://www.googleapis.com/youtube/v3/commentThreads?" + \
              "key={}&textFormat=plainText&" + \
              "part=snippet&" + \
              "videoId={}&" + \
              "maxResults={}&" + \
              "pageToken={}"
        uri = uri.format(API_KEY, id_, maxResults, nextPageToken)
        # Запрос данных о комментариях к видео
        content = requests.get(uri).text
        data = json.loads(content)
        # Обработка каждого комментария и суммирование количества лайков
        for item in data['items']:
            s += int(item['snippet']['topLevelComment']['snippet']['likeCount'])
    # Логирование кода скрипта в MLflow
    mlflow.log_artifact(local_path=f"{SCRIPTS_PATH}get_data.py",
                        artifact_path="get_data code")
    mlflow.end_run()

# Запись суммарного количества лайков в файл CSV
with open(f'{DATASETS_PATH}data.csv', 'a') as f:
    f.write("{}\n".format(s))
