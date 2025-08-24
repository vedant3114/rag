import streamlit as st
import tempfile
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ingestion import IngestionPipeline
from chunking import ChunkingPipeline
from embeddings import EmbeddingPipeline
from vector_index import VectorIndex
from retriever import Retriever
from generator import Generator

st.title("RAG System Demo")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
question = st.text_input("Ask a question about the PDF:")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    st.success("PDF uploaded successfully.")

    try:
        # Ingest PDF
        ingestion = IngestionPipeline(pdf_path)
        pages = ingestion.run(scanned=False)  # For demo, assume native PDF

        # Chunk text
        chunker = ChunkingPipeline(pages)
        chunks = chunker.chunk_by_paragraph()

        # Embed chunks
        embedder = EmbeddingPipeline()
        embedded_chunks = embedder.embed_chunks(chunks)

        # Build vector index
        dim = len(embedded_chunks[0]['embedding']) if embedded_chunks else 384
        index = VectorIndex(dim)
        index.add(embedded_chunks)

        # Set up retriever and generator
        retriever = Retriever(embedder, index)
        generator = Generator()

        if question:
            st.info("Processing your question...")
            # Retrieve relevant chunks
            results = retriever.retrieve(question, top_k=5)
            # Generate answer
            answer = generator.generate_answer(question, results)
            st.markdown(f"**Answer:** {answer}")
            st.markdown("**Citations:**")
            for chunk in results:
                st.markdown(f"- Page {chunk['page_num']}")
    finally:
        try:
            os.remove(pdf_path)
        except PermissionError:
            pass
