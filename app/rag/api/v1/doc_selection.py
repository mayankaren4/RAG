from fastapi import HTTPException
from sqlalchemy.orm import Session

from rag.schemas.schema import DocumentSelection
from models.table import Document


async def api_doc_selection(selection: DocumentSelection, db: Session) -> dict:
    """
    Fetches the document based on the selected ids.

    Args:
        selection (DocumentSelection): The ids, based on which the data needs to be filtered.
        db (Session): The database session.

    Returns:
        dict: The document based on the ids.

    Raises:
        HTTPException: If the document is not found.
    """
    # Get selected documents from the database
    selected_docs = db.query(Document).filter(Document.id.in_(selection.document_ids)).all()

    if not selected_docs:
        raise HTTPException(status_code=404, detail="No documents found with the provided IDs")

    return {"selected_documents": [{"id": doc.id, "title": doc.title} for doc in selected_docs]}
