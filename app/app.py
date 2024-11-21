from fastapi import FastAPI
from settings.config import Settings
from rag.api.router import router as rag_router
from fastapi.middleware.cors import CORSMiddleware


RAG_TAG = {
    "name": "Retrieval Augmented System (RAG)",
    "description": "These endpoints are maintained for the RAG application.",
}


# Initialize RAG app
app = FastAPI(version="v0.1",
              title="Retrieval Augmented System",
              description="",
              summary="PI of the RAG application",
              terms_of_service=None,
              contact=None,
              license_info=None,
              openapi_tags=[RAG_TAG]
            )

# Add all routers
# app.include_router(auth_router)
app.include_router(rag_router)
app.mount("/api/v1", app)


# Add the middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:1025"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
