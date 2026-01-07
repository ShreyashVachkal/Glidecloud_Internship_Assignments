# Vector Database Create API using FastAPI, Ollama & ChromaDB

## 📌 Project Overview
This project demonstrates a **basic Vector Database implementation** using **FastAPI**, **Ollama**, and **ChromaDB**.  
The API performs the **CREATE operation of CRUD**, where a text document is converted into **vector embeddings** and stored in a **vector database**.

The goal of this project is to understand:
- What vector databases are
- How embeddings are generated
- How vectors are stored for future semantic search or AI applications

---

## 🧠 What is Happening in This Project?
1. User sends a **text** to the API
2. The text is converted into **numerical vectors (embeddings)** using **Ollama**
3. These embeddings are stored inside **ChromaDB**
4. The stored vectors can later be used for:
   - Semantic search
   - Similarity matching
   - Retrieval-Augmented Generation (RAG)

---

## 🛠 Tech Stack Used
- **FastAPI** – API framework
- **Uvicorn** – ASGI server
- **Ollama** – Local embedding generation
- **ChromaDB** – Vector database
- **Pydantic** – Request validation
- **Python 3.10**

---

## 📂 Project Structure

