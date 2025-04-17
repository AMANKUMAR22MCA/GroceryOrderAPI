from sqlalchemy import Column, Integer, String, Float
from db.base import Base


# Represents a grocery product (e.g., milk, bread)
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)

# Example
# {
#   "name": "Milk",
#   "price_per_unit": 20.5,
#   "unit": "liter"
# }

