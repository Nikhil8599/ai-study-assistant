from sentence_transformers import SentenceTransformer
import chromadb
from documents import documents

embedder = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()
collection = client.create_collection(name="study_assistant")

texts = [doc["text"] for doc in documents]
ids = [doc["id"] for doc in documents]

embeddings = embedder.encode(texts).tolist()

collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=ids
)