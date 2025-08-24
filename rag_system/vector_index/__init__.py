# Vector Index module: Stores and searches embeddings

import numpy as np
from typing import List, Dict

class VectorIndex:
	"""
	Stores embeddings and supports similarity search using FAISS.
	"""
	def __init__(self, dim: int):
		self.dim = dim
		self.embeddings = []
		self.metadata = []
		self.index = None
		self._init_index()

	def _init_index(self):
		try:
			import faiss
			self.faiss = faiss
			self.index = faiss.IndexFlatL2(self.dim)
		except ImportError:
			raise ImportError("Please install faiss-cpu: pip install faiss-cpu")

	def add(self, embedded_chunks: List[Dict]):
		"""
		Add embedded chunks to the index.
		Each chunk must have 'embedding', 'text', and 'page_num'.
		"""
		vectors = np.array([chunk['embedding'] for chunk in embedded_chunks]).astype('float32')
		self.index.add(vectors)
		self.embeddings.extend(vectors)
		self.metadata.extend(embedded_chunks)

	def search(self, query_embedding, top_k=5):
		"""
		Search for top_k most similar chunks to the query embedding.
		Returns metadata for the top results.
		"""
		query = np.array([query_embedding]).astype('float32')
		D, I = self.index.search(query, top_k)
		results = [self.metadata[i] for i in I[0]]
		return results
