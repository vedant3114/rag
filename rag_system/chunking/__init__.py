# Chunking module: Splits text into chunks

import re

class ChunkingPipeline:
	"""
	Splits extracted PDF text into chunks for embedding and retrieval.
	Preserves page metadata for citation and evidence mapping.
	"""
	def __init__(self, pages, chunk_size=500):
		"""
		pages: List of dicts with 'page_num' and 'text'.
		chunk_size: Approximate number of characters per chunk.
		"""
		self.pages = pages
		self.chunk_size = chunk_size

	def chunk_by_paragraph(self):
		"""Split text into chunks by paragraphs."""
		chunks = []
		for page in self.pages:
			paragraphs = re.split(r'\n\s*\n', page['text'])
			for para in paragraphs:
				if para.strip():
					chunks.append({
						'page_num': page['page_num'],
						'text': para.strip()
					})
		return chunks

	def chunk_by_size(self):
		"""Split text into fixed-size chunks."""
		chunks = []
		for page in self.pages:
			text = page['text']
			for i in range(0, len(text), self.chunk_size):
				chunk_text = text[i:i+self.chunk_size]
				chunks.append({
					'page_num': page['page_num'],
					'text': chunk_text
				})
		return chunks
