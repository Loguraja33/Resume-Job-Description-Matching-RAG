Resume & Job Description Matching RAG System

An AI-powered Retrieval-Augmented Generation (RAG) application that analyzes a candidate’s resume against a job description to determine compatibility, highlight skill gaps, and provide an ATS-style match score.
Built using LangChain, HuggingFace Embeddings, FAISS Vector Database, Groq LLM, and Streamlit, this system helps candidates quickly understand how well their resume fits a specific job role.

🚀 Features
📂 Resume Upload

Upload resumes in PDF format

Automatically extracts text from resumes

Preprocesses the content for semantic analysis

📑 Job Description Input

Paste any job description directly into the application

Supports roles in AI, ML, Data Science, Software Engineering, and more

🔍 Semantic Matching

Resume content is split into chunks

Embedded using sentence-transformer models

Stored in FAISS vector database for efficient similarity search

🤖 Intelligent Analysis

The LLM performs multiple analyses:

ATS Match Score

Skill Matching

Missing Skills Identification

Resume Improvement Suggestions

⚡ Fast LLM Responses

Powered by Groq LLM

Uses Llama models for fast reasoning and responses

📊 Insightful Output

Provides clear results including:

ATS compatibility score

Matching skills

Missing skills

Suggestions to improve the resume

📊 Workflow Overview

Upload Resume (PDF)

Extract Text from Resume

Split Resume into Chunks

Generate Embeddings

Store in FAISS Vector Database

Input Job Description

Retrieve Relevant Resume Sections

LLM Analysis with Groq

Generate ATS Score + Feedback

🛠️ Tech Stack

LangChain – RAG pipeline and LLM orchestration
HuggingFace Transformers – Embedding models
FAISS – Vector similarity search
Groq LLM – High-speed LLM inference
Python – Backend development
Streamlit – Interactive UI
PyPDF2 / PDF Loader – Resume parsing

⚡ Getting Started
Prerequisites

Python 3.10+

Install dependencies

pip install -r requirements.txt
🔑 Environment Setup

Create a .env file and add your Groq API Key:

GROQ_API_KEY=your_api_key_here
▶ Run the Application

Start the Streamlit app:

streamlit run app.py

The application will run at:

http://localhost:8501
📌 Usage

Upload your resume (PDF)

Paste the job description

Click Analyze

View:

ATS Match Score

Matching Skills

Missing Skills

Resume Improvement Suggestions

💡 Example Queries

“How well does my resume match this Machine Learning Engineer role?”

“What skills are missing for this Data Scientist job?”

“Give suggestions to improve my resume for this job description.”

📈 Future Improvements

Multi-resume comparison

Automatic job scraping from LinkedIn

Resume rewriting using LLM

Interview question generation

Support for DOCX resumes