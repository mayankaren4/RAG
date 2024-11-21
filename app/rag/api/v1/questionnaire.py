import pickle
from fastapi import HTTPException
from sqlalchemy.orm import Session

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from rag.utils.utils import vectorizer
from rag.schemas.schema import QuestionRequest
from models.table import Document


async def api_question(question: QuestionRequest, db: Session) -> dict:
    """
    Finds the best match based on the question asked by comparing the question embedding with document embeddings.
    """
    # Load the saved fitted vectorizer
    try:
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)  # Load the pre-fitted vectorizer
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Vectorizer not found. Please ingest documents first.")

    # Retrieve all documents from the database
    documents = db.query(Document).all()

    # Transform the question using the same vectorizer (ensuring the same dimensionality as the document embeddings)
    question_embedding = vectorizer.transform([question.question]).toarray()

    # Retrieve embeddings and compute similarity
    similarities = []
    for doc in documents:
        doc_embedding = np.array(doc.embedding)  # Extracting stored embedding
        similarity = cosine_similarity(question_embedding, doc_embedding)
        similarities.append((doc.id, doc.title, similarity[0][0]))

    # Sort documents by similarity score in descending order
    similarities.sort(key=lambda x: x[2], reverse=True)

    # Return the most relevant document
    best_match = similarities[0] if similarities else None
    if best_match:
        doc_id, doc_title, _ = best_match
        doc_content = next(doc.content for doc in documents if doc.id == doc_id)
        response = {
            "question": question.question,
            "answer": doc_content,
            "document_title": doc_title
        }
    else:
        raise HTTPException(status_code=404, detail="No relevant documents found")

    return response
