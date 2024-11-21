import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

from rag.utils.utils import vectorizer
from sqlalchemy.orm import Session
from rag.schemas.schema import DocumentRequest
from models.table import Document


async def doc_ingestion(document: DocumentRequest, db: Session) -> dict:
    """
    Ingests the document.

    Args:
        document (DocumentRequest): The document to be ingested.
        db (Session): The database session

    Returns:
        dict: Documnent ingestion message with id.
    """
async def doc_ingestion(document: DocumentRequest, db: Session) -> dict:
    """
    Ingests the document and stores it with the corresponding embeddings.
    """
    # Check if the vectorizer is already fitted by loading it from file (if exists)
    try:
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)  # Load the pre-fitted vectorizer
    except FileNotFoundError:
        # If no saved vectorizer, fit a new one with the document content
        vectorizer = TfidfVectorizer()
        # Fit on the current document content (can be extended to more documents if needed)
        vectorizer.fit([document.content])

        # Save the fitted vectorizer for future use
        with open("vectorizer.pkl", "wb") as f:
            pickle.dump(vectorizer, f)

    # Now, use the fitted vectorizer to transform the document content into embeddings
    embeddings = vectorizer.transform([document.content]).toarray()

    # Create and add document to the database
    db_document = Document(title=document.title, content=document.content, embedding=embeddings.tolist())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return {"message": "Document ingested successfully", "document_id": db_document.id}
