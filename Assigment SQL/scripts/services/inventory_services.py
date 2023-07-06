from fastapi import APIRouter
from scripts.core.handler.email_handler import Email
from scripts.schemas.inventory_schemas import Item
from scripts.api import EndPoints
from scripts.logging.logs import logger
from scripts.core.handler.inventory_handler import sql_item_object
from sqlalchemy.orm import Session
from scripts.schemas.sql_model import Item
from scripts.utils.sql_utility import Base
from scripts.schemas.sql_schemas import Item
from fastapi import Depends
from scripts.utils.sql_utility import SessionLocal, engine

try:
    item_router = APIRouter()
    logger.info({"Message": "succesfully established the api router"})
except Exception as e:
    logger.error({"Error": str(e)})


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@item_router.post(EndPoints.adding_item)
def adding_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    try:
        return sql_item_object.add_item(item_id, item, db)
        
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.delete(EndPoints.deleting_item)
def deleting_item(item_id: int, db: Session = Depends(get_db)):
    try:

        del_item = sql_item_object.delete_item(item_id, db)
        return del_item
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.put(EndPoints.updating_item)
def updating_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    try:
        updated_values = item.dict(exclude_unset=True)
        up_item = sql_item_object.update_item(item_id, updated_values, db)
        return up_item
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.get(EndPoints.getting_items)
def fetch(db: Session = Depends(get_db)):
    try:
        get_items = sql_item_object.fetch(db)
        return get_items
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}
