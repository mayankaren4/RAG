from pydantic import BaseModel


# Pydantic models for request/response validation
class DocumentRequest(BaseModel):
    title: str
    content: str


class QuestionRequest(BaseModel):
    question: str


class DocumentSelection(BaseModel):
    document_ids: list[int]
