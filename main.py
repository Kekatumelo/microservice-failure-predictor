from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
class NewOrder(BaseModel):
  quantity:int
  customer_id:int
  order_id:int|None=None
orders={}

@app.post("/orders")
def create_order(order:NewOrder):
  if not orders:
    order_id=1
  else:
    order_id = max(orders)+1
  updated_order=order.model_copy(update = {"order_id":order_id})
  orders[order_id]=updated_order
  
  return orders[order_id]
@app.get("/orders/{order_id}")
def retrieve_order(order_id:int):
  if order_id not in orders:
    raise HTTPException(status_code=404,detail="Item Not Found")
  return orders[order_id]


