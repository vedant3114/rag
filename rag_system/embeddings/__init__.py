# Embeddings module: Generates vector representations

from typing import List, Dict

class EmbeddingPipeline:
	"""
	Generates vector embeddings for text chunks using a transformer model.
	"""
	def __init__(self, model_name='all-MiniLM-L6-v2'):
		self.model_name = model_name
		self.model = None
		self._load_model()

	def _load_model(self):
		try:
			from sentence_transformers import SentenceTransformer
			self.model = SentenceTransformer(self.model_name)
		except ImportError:
			raise ImportError("Please install sentence-transformers: pip install sentence-transformers")

	def embed_chunks(self, chunks: List[Dict]) -> List[Dict]:
		"""
		Accepts a list of chunk dicts with 'text' and 'page_num'.
		Returns a list of dicts with 'embedding', 'text', and 'page_num'.
		"""
		texts = [chunk['text'] for chunk in chunks]
		embeddings = self.model.encode(texts)
		embedded_chunks = []
		for chunk, emb in zip(chunks, embeddings):
			embedded_chunks.append({
				'page_num': chunk['page_num'],
				'text': chunk['text'],
				'embedding': emb
			})
		return embedded_chunks
