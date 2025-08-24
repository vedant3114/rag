# Evidence Highlighter: Maps citations to PDF evidence

import fitz  # PyMuPDF

class EvidenceHighlighter:
	"""
	Maps cited chunks to PDF pages and optionally highlights evidence in the PDF.
	"""
	def __init__(self, pdf_path):
		self.pdf_path = pdf_path
		self.doc = fitz.open(pdf_path)

	def highlight_chunks(self, chunks, output_path):
		"""
		Highlights the text of each chunk on its source page in the PDF.
		Saves the annotated PDF to output_path.
		"""
		for chunk in chunks:
			page_num = chunk['page_num'] - 1  # fitz is 0-indexed
			text = chunk['text']
			page = self.doc.load_page(page_num)
			areas = page.search_for(text)
			for area in areas:
				page.add_highlight_annot(area)
		self.doc.save(output_path)
