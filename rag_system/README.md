# RAG System

## Overview
This project implements a local, modular Retrieval-Augmented Generation (RAG) system for answering questions over PDF documents with citations and evidence highlighting.

## Modules
- **ingestion/**: PDF loading and OCR
- **chunking/**: Text chunking
- **embeddings/**: Vector generation
- **vector_index/**: Vector database
- **retriever/**: Chunk retrieval
- **generator/**: LLM-based answer generation
- **evidence_highlighter/**: Evidence mapping and highlighting
- **web_ui/**: Optional chat interface


## Getting Started
1. Place your PDFs in a designated folder (e.g., `data/`).
2. Run the ingestion pipeline to extract text and metadata.
   
### Example: Test Ingestion Pipeline
```python
from rag_system.ingestion import IngestionPipeline

# Path to your PDF file
pdf_path = 'data/sample.pdf'

# For native PDFs
pipeline = IngestionPipeline(pdf_path)
pages = pipeline.run(scanned=False)
# Retrieval-Augmented Generation (RAG) System

## Project Overview
This project is a modular, open-source Retrieval-Augmented Generation (RAG) system for answering questions over PDF documents. It supports both native and scanned PDFs, provides answers with citations, and can highlight the exact evidence in the source pages. The system uses a local stack and integrates with OpenRouter for free LLM inference.

### Features
- Ingest native and scanned PDFs (OCR supported)
- Chunk and embed text for semantic search
- Store and retrieve chunks using a vector database (FAISS)
- Generate answers with citations using a free Mistral LLM via OpenRouter
- Highlight evidence in source PDFs
- Web UI for interactive chat and document upload

## Directory Structure
- **ingestion/**: PDF loading and OCR
- **chunking/**: Text chunking
- **embeddings/**: Vector generation
- **vector_index/**: Vector database
- **retriever/**: Chunk retrieval
- **generator/**: LLM-based answer generation (OpenRouter integration)
- **evidence_highlighter/**: Evidence mapping and highlighting
- **web_ui/**: Streamlit chat interface

## Setup Instructions

### 1. Clone the Repository
Place your project files in a folder, e.g. `rag_system`.

### 2. Install Python Dependencies
Run the following in your project directory:
```powershell
pip install pymupdf pytesseract Pillow sentence-transformers faiss-cpu streamlit python-dotenv requests
```

### 3. Set Up OpenRouter API Key
Create a `.env` file in the `rag_system` folder with your OpenRouter API key:
```
OPENROUTER_API_KEY=your_openrouter_api_key
```

### 4. Run the Web UI
Open a terminal and run:
```powershell
cd path\to\rag_system
streamlit run web_ui\app.py
```
Open the provided local URL in your browser (e.g., http://localhost:8501).

### 5. Use the System
- Upload a PDF (native or scanned)
- Enter your question in the chat
- View the answer with citations and evidence highlights

## Example: Test Ingestion Pipeline (Python)
```python
from ingestion import IngestionPipeline
pdf_path = 'data/sample.pdf'
pipeline = IngestionPipeline(pdf_path)
pages = pipeline.run(scanned=False)
for page in pages:
	print(f"Page {page['page_num']}:\n{page['text'][:200]}\n---")
# For scanned PDFs (OCR):
# pages = pipeline.run(scanned=True)
```

## Quality
- Modular, testable code
- Open-source stack
- Measurable retrieval and citation accuracy

---
For questions or improvements, open an issue or contact the maintainer.
