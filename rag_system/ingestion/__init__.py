# Ingestion module: Handles PDF loading and OCR

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

class IngestionPipeline:
	"""
	Pipeline for ingesting native and scanned PDFs.
	Extracts text and page metadata for downstream processing.
	"""
	def __init__(self, pdf_path):
		self.pdf_path = pdf_path
		self.doc = fitz.open(pdf_path)

	def extract_native_pdf(self):
		"""Extract text from native PDF pages."""
		pages = []
		for page_num in range(len(self.doc)):
			page = self.doc.load_page(page_num)
			text = page.get_text()
			pages.append({
				'page_num': page_num + 1,
				'text': text
			})
		return pages

	def extract_scanned_pdf(self):
		"""Extract text from scanned PDF pages using OCR."""
		pages = []
		for page_num in range(len(self.doc)):
			page = self.doc.load_page(page_num)
			pix = page.get_pixmap()
			img = Image.open(io.BytesIO(pix.tobytes()))
			text = pytesseract.image_to_string(img)
			pages.append({
				'page_num': page_num + 1,
				'text': text
			})
		return pages

	def run(self, scanned=False):
		"""Run the pipeline for either native or scanned PDF."""
		if scanned:
			return self.extract_scanned_pdf()
		else:
			return self.extract_native_pdf()
