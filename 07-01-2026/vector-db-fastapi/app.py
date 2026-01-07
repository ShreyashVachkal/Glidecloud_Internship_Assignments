from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
import ollama

# Create FastAPI app
app = FastAPI()

# Create ChromaDB client (local)
chroma_client = chromadb.Client()

# Create or get a collection
collection = chroma_client.get_or_create_collection(
    name="documents"
)

# Request body structure
class DocumentRequest(BaseModel):
    text: str

@app.post("/add-document")
def add_document(doc: DocumentRequest):
    # Generate embedding using Ollama
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=doc.text
    )

    embedding = response["embedding"]

    # Store in ChromaDB
    collection.add(
        documents=[doc.text],
        embeddings=[embedding],
        ids=[doc.text[:20]]  # simple unique id
    )

    return {"message": "Document stored successfully","embedding":embedding}
