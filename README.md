=========================================
PDF Question Answering using LangChain + Ollama + ChromaDB
=========================================

This project lets you ask natural language questions directly from a PDF document
using LangChain, Ollama, and ChromaDB. It automates reading the PDF, splitting it
into smaller chunks, embedding them locally with Ollama embeddings, and answering
questions using an Ollama LLM such as Llama 3.2.

-----------------------------------------
PROJECT STRUCTURE
-----------------------------------------

pdf-qa-ollama/
│
├── data/
│   └── doc.pdf              # Input PDF file
├── db/                      # Chroma vector database (auto-created)
├── main.py                  # Main script
├── requirements.txt         # Python dependencies
└── README.txt               # This file

-----------------------------------------
FEATURES
-----------------------------------------

- Load and process PDFs using PyPDFLoader
- Split documents into semantic chunks
- Generate embeddings using Ollama ("nomic-embed-text")
- Store vectors in ChromaDB locally
- Query the knowledge base with Llama 3.2 (offline)
- Fully local and private (no external API calls)

-----------------------------------------
REQUIREMENTS
-----------------------------------------

1. Python 3.10 or higher
2. Ollama installed and running (https://ollama.com/download)
3. Optional: Docker if you want to containerize Ollama

Python packages:
- langchain_community
- langchain_text_splitters
- langchain_ollama
- langchain_chroma

Install all dependencies with:
    pip install -r requirements.txt

-----------------------------------------
HOW IT WORKS
-----------------------------------------

1. PDF Loading:
   PyPDFLoader extracts text and metadata from your PDF.

2. Text Splitting:
   RecursiveCharacterTextSplitter breaks the document into smaller overlapping
   chunks for efficient retrieval.

3. Embedding & Storage:
   Each chunk is embedded using "nomic-embed-text" and stored persistently
   in a local ChromaDB directory.

4. Question Answering:
   When a user asks a question, the retriever finds relevant chunks and
   Llama 3.2 generates the answer.

-----------------------------------------
USAGE
-----------------------------------------

1. Place your PDF in the "data" folder.
2. Update the PDF path in main.py:
       pdf_file = r"D:\Python\UROP\data\doc.pdf"
3. Run the script:
       python main.py
4. Type a question when prompted.

Example:
-----------------------------------------
Ingested 42 chunks into db
Ask a question about the PDF: What is the main topic of the document?
Answer: The report focuses on the impact of AI in healthcare innovation.
-----------------------------------------

-----------------------------------------
CONFIGURATION
-----------------------------------------

You can modify parameters in main.py:

    chunk_size=1200
    chunk_overlap=200
    embedding model = "nomic-embed-text"
    LLM model = "llama3.2:3b"

-----------------------------------------
MODELS USED
-----------------------------------------

Embeddings Model:  nomic-embed-text
LLM Model:         llama3.2:3b

-----------------------------------------
FUTURE ENHANCEMENTS
-----------------------------------------

- Add web UI using Streamlit or FastAPI
- Support multiple PDF ingestion
- Enable document summarization
- Implement citation and source tracking

-----------------------------------------
AUTHOR
-----------------------------------------

Developed by:  Mukhesh Kumar Reddy
GitHub:        https://github.com/Mukheshkumar25
Email:         mukheshkumarreddy@gmail.com
-----------------------------------------
