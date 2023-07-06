from fastapi import FastAPI
from scripts.services.inventory_services import item_router
from scripts.logging.logs import logger

app = FastAPI()
item_data = {}

try:
    app.include_router(item_router)
except :
    logger.error({"Error:":"Unexpected scenario happened with the router"})    


