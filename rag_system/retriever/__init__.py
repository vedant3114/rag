# Retriever module: Retrieves relevant chunks

class Retriever:
	"""
	Embeds user queries and retrieves relevant chunks from the vector index.
	"""
	def __init__(self, embedding_model, vector_index):
		self.embedding_model = embedding_model
		self.vector_index = vector_index

	def retrieve(self, query, top_k=5):
		"""
		Embed the query and retrieve top_k relevant chunks.
		Returns chunk metadata for citation and evidence.
		"""
		query_embedding = self.embedding_model.model.encode([query])[0]
		results = self.vector_index.search(query_embedding, top_k=top_k)
		return results
