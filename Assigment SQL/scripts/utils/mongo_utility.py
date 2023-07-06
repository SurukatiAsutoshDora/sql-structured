from scripts.constants.db_constants import db_constant_object
from pymongo import MongoClient
from scripts.logging.logs import logger


try:
    client = MongoClient(db_constant_object.uri)
    mydb = client[db_constant_object.database_name]
    collection = mydb[db_constant_object.collection_name]
    logger.info({"Messgae:":"Succesfully connected Mongo"})
except Exception as e:
    logger.error({"Error:", "while connecting to MongoDB"})
