import os
from dotenv import load_dotenv


load_dotenv()

FOLDER_ID = os.getenv('FOLDER_ID')

GPT_MODEL = "yandexgpt"
MAX_MODEL_TOKENS = 50
MODEL_TEMPERATURE = 0.6

IAM_TOKEN_ENDPOINT = "http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token"
IAM_TOKEN_PATH = "token_data.json"
TOKENS_DATA_PATH = "tokens_count.json"
