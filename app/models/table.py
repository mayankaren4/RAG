from sqlalchemy import Column, Integer, String, Text, JSON
from database.db import Base, engine


# Define Document table (SQLAlchemy model)
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    embedding = Column(JSON)  # Store embeddings as JSON

# Create tables in the database (if they do not exist)
Base.metadata.create_all(bind=engine)
