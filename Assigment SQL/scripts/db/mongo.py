from scripts.schemas.inventory_schemas import Item
from scripts.utils.mongo_utility import collection
from scripts.logging.logs import logger
from scripts.constants.db_constants import db_constant_object


class Item_handler:

    def add_item(self, item_id: int, item: Item):
        try:
            if list(collection.find({"item_id": item_id})):
                logger.warning({"Warning": "This ID is already present"})
                return {"Warning": "This ID is already present"}
            collection.insert_one(item.dict())
            logger.info({"message": "Successfully Added"})
            return {"message": "Successfully Added"}

        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def delete_item(self, item_id: int):
        try:
            if list(collection.find({"item_id": item_id})) == []:
                logger.warning({"Warning": "Item not found"})
                return {"Warning": "Item not found"}

            else:
                collection.delete_one({"item_id": item_id})
                logger.info({"Message": "Item deleted succesfully"})
                return {"Message": "Item deleted succesfully"}

        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def update_item(self, item_id: int, item: Item):
        try:
            if list(collection.find({"item_id": item_id})) != []:
                collection.update_one({"item_id": item_id}, {
                                      "$set": item.dict()})
                logger.info({"Message": "It is updated successfully"})
                return {"Message": "It is updated successfully"}

            else:
                logger.error({"error": "Item not found"})
                return {"error": "Item not found"}

        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def fetch(self):
        try:
            items = list(collection.find({}, {'_id': 0}))
            if items == []:
                logger.warning({"Warning:": "there are not items "})
                return {"Warning:": "there are not items"}
            else:
                logger.info({"Message:": "Succesfully fetched "})
                return items
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def find_by_id(self, id):
        try:
            found_data = list(collection.find(id, {"_id": False}))
            logger.info({"Message": "Item found succesfully successfully"})
            return found_data
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def find_total(self):
        try:
            total = collection.aggregate(db_constant_object.aggregate)
            if total == 0:
                logger.warning({"Warning:": "there are not items "})
                return {"Warning:": "there are no items so the total price is zero"}
            else:
                logger.info({"Message:": "Succesfully found the total"})
            return (list(total))[0]['total']
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}


item_object = Item_handler()
