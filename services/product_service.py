from sqlalchemy.orm import Session
from models import Product
from schemas.product_schema import ProductCreate
from utils.validators import raise_bad_request,raise_not_found

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


def get_product_by_id(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise_not_found(f"Product with ID {product_id} not found.")
    return product

def update_product(db: Session, product_id: int, new_data: ProductCreate):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise_not_found(f"Product with ID {product_id} not found.")
    
    product.name = new_data.name
    product.price_per_unit = new_data.price_per_unit
    product.unit = new_data.unit

    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise_not_found(f"Product with ID {product_id} not found.")
    
    db.delete(product)
    db.commit()