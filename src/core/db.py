import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("db url is niet gezet!")

# Configure engine with connection pooling settings
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Test connections before use
    pool_recycle=3600,   # Recycle connections after 1 hour
    pool_timeout=30,     # Wait up to 30 seconds for a connection
    pool_size=5,         # Maintain up to 5 connections
    max_overflow=10      # Allow up to 10 additional connections
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

# Dependency for getting DB sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
