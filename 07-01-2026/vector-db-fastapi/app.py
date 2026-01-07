from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
import ollama


app = FastAPI()

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="documents"
)

class DocumentRequest(BaseModel):
    text: str

@app.post("/add-document")
def add_document(doc: DocumentRequest):
    
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=doc.text
    )

    embedding = response["embedding"]

    
    collection.add(
        documents=[doc.text],
        embeddings=[embedding],
        ids=[doc.text[:20]]  # simple unique id
    )

    return {"message": "Document stored successfully","embedding":embedding}

