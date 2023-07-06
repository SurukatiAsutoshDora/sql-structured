from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    """This class takes the parameters for the item in the inventory"""
    item_id:int
    item_name: str
    item_price: int
    item_volume: int
    item_manufacture_date: datetime
    item_expiry_date: datetime
    item_shelf_number: str
    
    
class Email(BaseModel):
    """This class takes the parameters for the Emails"""
    rec_email: str
    subject: str
    body: str    
    