from pydantic import BaseModel

#Request Model
class NewOrder(BaseModel):
  quantity:int
  customer_id:int

#Response Model
class Order(BaseModel):
  order_id:int
  quantity:int
  customer_id:int