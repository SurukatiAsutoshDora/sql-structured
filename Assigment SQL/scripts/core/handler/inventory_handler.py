from scripts.db.mongo import item_object
from scripts.logging.logs import logger
# from scripts.schemas.inventory_schemas import Item
from scripts.schemas.sql_schemas import Item
from scripts.db.sql import sql_item_object
from sqlalchemy.orm import Session


class Item_handler:
    def fetch(self, db: Session):
        try:
            all_items = sql_item_object.fetch(db)
            if all_items == []:
                logger.warning({"Warning": "No items present in the database"})
                return {"Warning": "No items present in the database"}
            return all_items
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def add_item(self, item_id: int, item: Item, db: Session):
        try:
            if list(sql_item_object.find_by_id(item_id, db)) != []:
                logger.warning({"Warning:": "item already exist"})
                return {"Warning:": "item already exist"}
            return sql_item_object.add_item(item, db)
        except Exception as e:
            logger.error({"error": str(e.args)})
            return {"error": str(e.args)}

    def update_item(self, item_id: int, item: Item, db: Session):
        try:
            if sql_item_object.find_by_id(item_id, db) == []:
                logger.warning({"Warning": "item does not exist"})
                return {"Warning": "item does not exist"}
            return sql_item_object.update_item(item_id, item, db)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def delete_item(self, item_id: int, db: Session):
        try:
            if sql_item_object.find_by_id(item_id, db) == []:
                logger.warning({"Warning": "item does not exist"})
                return {"Warning": "item does not exist"}
            return sql_item_object.delete_item(item_id, db)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}


sql_item_handler = Item_handler()
