from sqlalchemy import Column, Integer, String
from db.base import Base

# Represents a grocery order (e.g., milk, bread)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)


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