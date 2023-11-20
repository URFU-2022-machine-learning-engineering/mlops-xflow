from decouple import config
import pathlib

# Получение API-ключа из переменной окружения
API_KEY = config('API_KEY')

# Определение путей к переменным окружения
BASIC_PATH = config('BASIC_PATH', default=pathlib.Path(__file__).absolute())
SCRIPTS_PATH = config('SCRIPTS_PATH', default=f"{BASIC_PATH}scripts/")
MODELS_PATH = config('MODELS_PATH', default=f"{BASIC_PATH}models/")
DATASETS_PATH = config('DATASETS_PATH', default=f"{BASIC_PATH}datasets/")

# Определение URI для отслеживания экспериментов в MLflow
ML_FLOW_TRACKING_URI = config('ML_FLOW_TRACKING_URI', default="http://localhost:5000")
