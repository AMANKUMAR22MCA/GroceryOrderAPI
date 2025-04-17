from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.product_schema import ProductCreate, ProductResponse
from services.product_service import create_product, get_all_products
from database import SessionLocal
from typing import List
from database import get_db

router = APIRouter()
# Endpoint to create a new product
@router.post("/products", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)
# Endpoint to list all the products avialiable
@router.get("/products", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)
