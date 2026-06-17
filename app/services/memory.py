from datetime import datetime
from uuid import uuid4
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from app.services.embeddings import create_embedding

COLLECTION_NAME='memories'

client = QdrantClient(host="localhost", port=6333)


def init_collection():
    collections = client.get_collections().collections

    exists = any(
        collection.name == COLLECTION_NAME
        for collection in collections
    )

    if not exists:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            ),
        )


def add(memory):
    embedding=create_embedding(memory['text'])
    client.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=[PointStruct(
            id=str(uuid4()),
            vector=embedding,
            payload={
                "text": memory["text"],
                "category": memory["category"],
                "importance": memory["importance"],
                "created_at": datetime.utcnow().isoformat()
            },
        )]
    )


def query(query:str):
    embedding=create_embedding(query)
    result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding
    )
    return result