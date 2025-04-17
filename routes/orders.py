from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.order_schema import OrderCreate, OrderResponse
from services.order_service import (
    place_order, get_all_orders, get_order_by_id,
    update_order, delete_order
)
from typing import List
from database import get_db

router = APIRouter()

# Create a new order
@router.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return place_order(db, order)

# Get all orders
@router.get("/orders", response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)

# Get a single order by ID
@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return get_order_by_id(db, order_id)

# Update an order
@router.put("/orders/{order_id}", response_model=OrderResponse)
def update_existing_order(order_id: int, order_data: OrderCreate, db: Session = Depends(get_db)):
    return update_order(db, order_id, order_data)

# Delete an order
@router.delete("/orders/{order_id}")
def delete_existing_order(order_id: int, db: Session = Depends(get_db)):
    delete_order(db, order_id)
    return {"detail": f"Order {order_id} deleted successfully"}
