# RAG-based-LLM-Chatbot 📄🤖

This project leverages the power of LangChain, Google Generative AI, and FAISS to create a conversational AI that can interact with the content of PDF documents. 

---
## Features

- **PDF Content Extraction**: Extracts text from PDF documents using PyPDF2.
- **Text Chunking**: Efficiently splits large texts into manageable chunks for processing.
- **Vector Store Creation**: Utilizes FAISS and Google Generative AI for embedding and storing text chunks as vectors.
- **Conversational Chain**: Sets up a conversational AI chain using LangChain and Google’s Gemini model, with memory to track conversation history.
---
### Usage

#### Load PDFs and Process Text

- The `get_pdf_text()` function extracts text from a list of PDF documents.
- The `get_text_chunks()` function splits the extracted text into chunks for easier processing.

#### Create a Vector Store

- Use `get_vector_store()` to create a vector store from the text chunks, embed them using Google Generative AI and save them in Langchain's vector DB FAISS

#### Initiate a Conversational Chain

- Set up the conversational AI using `get_conversational_chain()`, which integrates a language model with memory and a retrieval-based system.

---

**Note:** This is just a basic Chatbot. Will be embedding more advanced features in it, Stay tuned!
