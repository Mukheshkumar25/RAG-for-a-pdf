import os
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Updated imports (new packages)
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

# Directories
DATA_DIR = "data"
DB_DIR = "db"


def ingest(pdf_path: str):
    """Load PDF, split into chunks, and store in ChromaDB"""
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma(
        collection_name="docs",
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )
    vectordb.add_documents(chunks)
    print(f"Ingested {len(chunks)} chunks into {DB_DIR}")


def ask_question(question: str):
    """Query ChromaDB using Ollama LLM"""
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma(
        collection_name="docs",
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )

    retriever = vectordb.as_retriever()
    llm = OllamaLLM(model="llama3.2:3b")

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(question)


if __name__ == "__main__":
    # PDF path (updated)
    pdf_file = r"D:\Python\UROP\data\doc.pdf"



    # Step 1: Ingest PDF
    ingest(pdf_file)

    # Step 2: Ask a question
    question = input("Ask a question about the PDF: ")
    print("Answer:", ask_question(question))
