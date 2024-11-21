import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


# Read the environment variables
# db_user = os.getenv('DB_USER', 'postgres')
# db_password = os.getenv('DB_PASSWORD', 'postgres')
# db_host = os.getenv('DB_HOST', 'localhost')
# db_port = os.getenv('DB_PORT', 5432)
# db_name = os.getenv('DB_NAME', 'rag_test')

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Construct the database connection URL
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


# SQLAlchemy Engine and Session Local
engine = create_engine(DATABASE_URL)
# Check if DB exists. If not, create the database
if not database_exists(engine.url):
    create_database(engine.url)

# SQLAlchemy Setup
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables in the database (if they do not exist)
Base.metadata.create_all(bind=engine)
