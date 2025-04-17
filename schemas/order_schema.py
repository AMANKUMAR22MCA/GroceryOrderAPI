from pydantic import BaseModel, validator
from typing import List

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

    @validator("quantity")
    def quantity_positive(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v

class OrderCreate(BaseModel):
    customer_name: str
    items: List[OrderItemCreate]

class OrderItemResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float

class OrderResponse(BaseModel):
    order_id: int
    customer_name: str
    items: List[OrderItemResponse]
    total_amount: float
