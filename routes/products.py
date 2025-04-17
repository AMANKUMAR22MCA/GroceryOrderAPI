from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.product_schema import ProductCreate, ProductResponse
from services.product_service import (
    create_product, get_all_products,
    get_product_by_id, update_product,
    delete_product
)
from typing import List
from database import get_db

router = APIRouter()

# Create a new product
@router.post("/products", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

# List all products
@router.get("/products", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)

# Get a product by ID
@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(db, product_id)

# Update a product by ID
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_existing_product(product_id: int, product_data: ProductCreate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product_data)

# Delete a product by ID
@router.delete("/products/{product_id}")
def delete_existing_product(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"detail": f"Product {product_id} deleted successfully"}
