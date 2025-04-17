from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.order_schema import OrderCreate, OrderResponse
from services.order_service import place_order, get_all_orders
from database import SessionLocal
from typing import List
from database import get_db
router = APIRouter()

# create a new order
@router.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return place_order(db, order)

# get all orders associated wit a customer
@router.get("/orders", response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)

# Example POST request body:
# {
#   "customer_name": "John Doe",
#   "items": [
#     {
#       "product_id": 1,
#       "quantity": 2
#     },
#     {
#       "product_id": 5,
#       "quantity": 1
#     }
#   ]
# }