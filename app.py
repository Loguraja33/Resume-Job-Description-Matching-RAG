import streamlit as st
from utils.pdf_loader import load_pdf
from utils.chunking import chunk_text
from utils.vector_store import create_vector_store, retrieve
from agents.llm_agent import generate_response

st.title("Resume + JD Matching RAG")

resume_file = st.file_uploader("Upload Resume PDF", type="pdf")
job_description = st.text_area("Paste Job Description")

if resume_file and job_description:

    resume_text = load_pdf(resume_file)
    combined_text = resume_text + "\n" + job_description
    
    chunks = chunk_text(combined_text)
    index, embeddings = create_vector_store(chunks)
    
    retrieved = retrieve(job_description, chunks, index)
    
    response = generate_response(job_description, retrieved)
    
    st.subheader("ATS Analysis")
    st.write(response)