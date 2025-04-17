from sqlalchemy.orm import Session
from models import Product
from schemas.product_schema import ProductCreate
from utils.validators import raise_bad_request

def create_product(db: Session, product: ProductCreate):
    """
    Create a new product.
    Checks for duplicate product names.
    """
    if db.query(Product).filter_by(name=product.name).first():
        raise_bad_request("Product name must be unique")
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all_products(db: Session):
    """
    Fetch all products from the database.
    """
    return db.query(Product).all()
