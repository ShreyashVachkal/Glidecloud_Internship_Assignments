from fastapi import APIRouter
from app.models.schemas import DocumentRequest, SearchRequest
from app.services.chunking import chunk_text
from app.services.embeddings import generate_embedding
from app.db.chroma import collection
import uuid

router = APIRouter()

@router.post("/add-document")
def add_document(doc: DocumentRequest):
    chunks = chunk_text(doc.text)

    for chunk in chunks:
        embedding = generate_embedding(chunk)

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(uuid.uuid4())]
        )

    return {
        "message": "Document chunked, embedded, and stored successfully",
        "total_chunks": len(chunks)
    }


@router.post("/search")
def search_document(search: SearchRequest):
    query_embedding = generate_embedding(search.query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return {
        "query": search.query,
        "results": results["documents"]
    }
