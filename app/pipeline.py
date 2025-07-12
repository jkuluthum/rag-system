from langchain.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
import pdfplumber
import os

from dotenv import load_dotenv
load_dotenv()

pdf_path = Path("data/romeo-juliet.pdf")
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text
    
# Loading the document
def load_vectorstore():
    document = extract_text_from_pdf("data/romeo-juliet.pdf")
    
    #splitting/chunking the document into smaller parts
    text_splitter = RecursiveCharacterTextSplitter( #"\n\n" "\n" ""
        chunk_size = 300,
        chunk_overlap = 50,
    )

    #splitted texts
    texts = text_splitter.split_text(document)
    
    #for similarity search
    #embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",
        model_kwargs = {'device':'cpu'}
        )

    #creating a vector store and passing to it documents and embeddings
    # persistent_client = chromadb.PersistentClient()
    # collection = persistent_client.get_or_create_collection("collection_name")
    # collection.add(ids=["1", "2", "3"], documents=["a", "b", "c"])
    
    #database
    vectorstore = Chroma(
        collection_name = "collector", 
        embedding_function=embeddings,
        persist_directory="chromadb",
    )

    return vectorstore

retriever = load_vectorstore().as_retriever()

#Groq LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.8, #for model productivity
    max_tokens=400,  #token limit
)

qa_chain = RetrievalQA.from_chain_type(
    chain_type="stuff",
    llm=llm,
    retriever=retriever,
)

# This function takes a query and returns the answer using the QA chain
def ask_me(query):
    return qa_chain.run(query)
