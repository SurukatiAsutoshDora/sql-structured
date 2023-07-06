from sqlalchemy.orm import Session
from scripts.schemas.sql_model import Item
from scripts.logging.logs import logger

class sql_item_handler:

    def find_by_id(self,item_id: int,db: Session):
        try:
            data= db.query(Item).filter(Item.item_id == item_id).first()
            if data:
                return [data]
            else:
                return []
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}  
        


    def fetch(self, db: Session):
        return db.query(Item).all()

    def get_home_page(self, db: Session):
        return "Welcome to My Inventory"




    def delete_item(self,item_id: int,db: Session):
        item = db.query(Item).get(item_id)
        if item:
            db.delete(item)
            db.commit()
            return True
        return False

    def update_item(self, item_id: int, updated_values: dict,db: Session):
        item = db.query(Item).get(item_id)
        if item:
            for key, value in updated_values.items():
                setattr(item, key, value)
            db.commit()
            return True
        return False


    def add_item(self,item_id,item,db: Session):
        db_item = Item(item_id=item.item_id,item_name=item.item_name,item_price=item.item_price,item_volume=item.item_volume,item_manufacture_date=item.item_manufacture_date,item_expiry_date=item.item_expiry_date,item_shelf_number=item.item_shelf_number)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

sql_item_object=sql_item_handler()