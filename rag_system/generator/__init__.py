# Generator module: Uses LLM to answer questions


from typing import List, Dict
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

class Generator:
	"""
	Uses OpenRouter API to generate answers from retrieved chunks, with citations.
	"""
	def __init__(self, model_name='mistralai/mistral-small-3.2-24b-instruct:free'):
		self.model_name = model_name
		self.api_key = os.getenv('OPENROUTER_API_KEY', 'YOUR_API_KEY_HERE')  # Replace with your key or set as env var
		self.api_url = 'https://openrouter.ai/api/v1/chat/completions'

	def generate_answer(self, question: str, retrieved_chunks: List[Dict], max_length=512) -> str:
		"""
		Generate an answer using OpenRouter API, including citations for each chunk.
		"""
		context = "\n\n".join([
			f"[Page {chunk['page_num']}] {chunk['text']}" for chunk in retrieved_chunks
		])
		prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
		headers = {
			'Authorization': f'Bearer {self.api_key}',
			'Content-Type': 'application/json'
		}
		data = {
			"model": self.model_name,
			"messages": [
				{"role": "user", "content": prompt}
			],
			"max_tokens": max_length
		}
		response = requests.post(self.api_url, headers=headers, json=data)
		if response.status_code == 200:
			result = response.json()
			answer = result['choices'][0]['message']['content']
			return answer
		else:
			return f"Error: {response.status_code} - {response.text}"
