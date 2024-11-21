import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database.db import get_db
from ..utils.utils import add_application_tag
from ..schemas.schema import DocumentRequest, DocumentSelection, QuestionRequest
from ..api.v1.ingest_doc import doc_ingestion
from ..api.v1.questionnaire import api_question
from ..api.v1.doc_selection import api_doc_selection


# Define the router
router = APIRouter()


# Document ingestion API
@router.post("/ingest_document/",
             status_code=status.HTTP_201_CREATED)
async def ingest_document(document: DocumentRequest, db: Session = Depends(get_db)) -> dict:
    """
    Ingests a new document.

    Args:
        document (DocumentRequest): The data to be ingested.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: The result of the document ingestion.
    """
    logging.info("Received a request to ingest the document")
    ingestion_response = await doc_ingestion(document=document, db=db)
    result = add_application_tag(ingestion_response)
    return result


# Q&A API using RAG (with simulated embeddings and retrieval)
@router.post("/ask_question/",
             status_code=status.HTTP_200_OK)
async def ask_question(question: QuestionRequest, db: Session = Depends(get_db)) -> dict:
    """
    Finds the best match based on the question asked.

    Args:
        question (QuestionRequest): The question, based on which the response will be filtered.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: The response w.r.t the question.

    Raises:
        HTTPException: If no relevant documnet found.
    """
    logging.info("Received a request to find best match based on the question asked")
    question_response = await api_question(question=question, db=db)
    result = add_application_tag(question_response)
    return result

# Document selection API
@router.post("/select_documents/")
async def select_documents(selection: DocumentSelection, db: Session = Depends(get_db)) -> dict:
    """
    Selects the document to consider in the RAG based Q&A process

    Args:
        selection (DocumentSelection): The document id, based on which the document will be filtered.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: The response w.r.t the selected document id.

    Raises:
        HTTPException: If no relevant documnet found.
    """
    logging.info("Received a request to select the document based on the document id")
    question_response = await api_doc_selection(selection=selection, db=db)
    result = add_application_tag(question_response)
    return result
