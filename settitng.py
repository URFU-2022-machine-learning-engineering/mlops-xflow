from decouple import config

API_KEY = config('API_KEY')

BASIC_PATH = config('BASIC_PATH', default="/home/dzailz/project/")
SCRIPTS_PATH = config('SCRIPTS_PATH', default=f"{BASIC_PATH}scripts/")
MODELS_PATH = config('MODELS_PATH', default=f"{BASIC_PATH}models/")
DATASETS_PATH = config('DATASETS_PATH', default=f"{BASIC_PATH}datasets/")
