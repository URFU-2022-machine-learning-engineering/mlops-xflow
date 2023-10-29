import os
import mlflow
import requests
import json
from pyyoutube import Api
from ..settings import SCRIPTS_PATH, DATASETS_PATH, API_KEY, BASIC_PATH, ML_FLOW_TRACKING_URI

os.environ["MLFLOW_REGISTRY_URI"] = f"{BASIC_PATH}mlflow/"
mlflow.set_tracking_uri(ML_FLOW_TRACKING_URI)
mlflow.set_experiment("get_data")
 
api = Api(api_key=API_KEY)
 
query = "'Mission Impossible'"
video = api.search_by_keywords(q=query, search_type=["video"], count=10, limit=30)
maxResults = 100
nextPageToken = ""
s = 0
 
with mlflow.start_run():
    for i, id_ in enumerate([x.id.videoId for x in video.items]):
        uri = "https://www.googleapis.com/youtube/v3/commentThreads?" + \
              "key={}&textFormat=plainText&" + \
              "part=snippet&" + \
              "videoId={}&" + \
              "maxResults={}&" + \
              "pageToken={}"
        uri = uri.format(API_KEY, id_, maxResults, nextPageToken)
        content = requests.get(uri).text
        data = json.loads(content)
        for item in data['items']:
            s += int(item['snippet']['topLevelComment']['snippet']['likeCount'])
    mlflow.log_artifact(local_path=f"{SCRIPTS_PATH}get_data.py",
                        artifact_path="get_data code")
    mlflow.end_run()
 
with open(f'{DATASETS_PATH}data.csv', 'a') as f:
    f.write("{}\n".format(s))
