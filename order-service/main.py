from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from models import Order,NewOrder

app = FastAPI()

orders={  1: Order(order_id=1, quantity=3, customer_id=101),
    2: Order(order_id=2, quantity=5, customer_id=102),
    3: Order(order_id=3, quantity=2, customer_id=103)}

@app.post("/orders",response_model=Order)
def create_order(order:NewOrder):
  if not orders:
    order_id=1
  else:
    order_id = max(orders)+1
  created_order=order.model_copy(update = {"order_id":order_id})
  orders[order_id]=created_order
  return orders[order_id]
@app.get("/orders/{order_id}")
def retrieve_order(order_id:int):
  if order_id not in orders:
    raise HTTPException(status_code=404,detail="Item Not Found")
  return orders[order_id]

@app.delete("/orders/{order_id}")
def delete_order(order_id:int):
  if order_id not in orders:
    raise HTTPException(status_code=404,detail="This particular order id is not in orders")
  del orders[order_id]
  return f"order {order_id} is deleted"

@app.put("/orders/{order_id}")
def update_order(order_id:int,order:NewOrder)->NewOrder:
  if order_id not in orders:
    raise HTTPException(status_code=404,detail="This particular order id is not in orders")   
  del orders[order_id]
  return {"message": f"Order {order_id} deleted successfully"}

@app.get("/health/")
def health_check():
  return {"status":"healthy"}
    

