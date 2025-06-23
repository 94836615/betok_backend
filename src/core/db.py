import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# If DATABASE_URL is not set and we're running tests, use SQLite in-memory database
if not DATABASE_URL:
    if 'pytest' in sys.modules:
        DATABASE_URL = "sqlite:///:memory:"
    else:
        raise ValueError("db url is niet gezet!")

# Configure engine with appropriate settings based on database type
if DATABASE_URL.startswith('sqlite'):
    # SQLite-specific settings
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True  # Test connections before use
    )
else:
    # PostgreSQL and other database settings with connection pooling
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
