from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from scripts.logging.logs import logger
from scripts.constants.sql_constants import sql_db_object


try:
    SQLALCHEMY_DATABASE_URL = sql_db_object.database_url

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    logger.info({"Successfully connected to the database"})
except Exception as e:
    logger.error({"Error":"Failed to connect the database"}  )
    