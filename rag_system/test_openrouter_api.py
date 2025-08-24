import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load .env
load_dotenv(dotenv_path=Path(__file__).resolve().parent / '.env')
api_key = os.getenv('OPENROUTER_API_KEY')

url = "https://openrouter.ai/api/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(url, headers=headers)
print("Status code:", response.status_code)
print("Response:", response.text)
