from sqlalchemy.orm import Session
from models import Order, OrderItem, Product
from schemas.order_schema import OrderCreate, OrderResponse, OrderItemResponse
from utils.validators import raise_not_found, raise_bad_request

def place_order(db: Session, order_data: OrderCreate):
    """
    - Create a new order with multiple order items.
    - Validates product existence
    - Saves order and related order items
    """
    order = Order(customer_name=order_data.customer_name)
    db.add(order)
    db.commit()
    db.refresh(order)

    items = []
    total_amount = 0
    for item in order_data.items:
        product = db.query(Product).filter_by(id=item.product_id).first()
        if not product:
            raise_not_found(f"Product ID {item.product_id} not found")
        price = item.quantity * product.price_per_unit
        total_amount += price
        order_item = OrderItem(order_id=order.id, product_id=product.id, quantity=item.quantity)
        db.add(order_item)
        items.append(OrderItemResponse(
            product_id=product.id,
            product_name=product.name,
            quantity=item.quantity,
            price=price
        ))

    db.commit()
    return OrderResponse(
        order_id=order.id,
        customer_name=order.customer_name,
        items=items,
        total_amount=total_amount
    )

def get_all_orders(db: Session):
    """
    Retrieve all  orders.
    Includes related order items (if any).
    """
    orders = db.query(Order).all()
    results = []
    for order in orders:
        items = []
        total = 0
        for item in db.query(OrderItem).filter_by(order_id=order.id).all():
            product = db.query(Product).filter_by(id=item.product_id).first()
            price = item.quantity * product.price_per_unit
            total += price
            items.append(OrderItemResponse(
                product_id=product.id,
                product_name=product.name,
                quantity=item.quantity,
                price=price
            ))
        results.append(OrderResponse(
            order_id=order.id,
            customer_name=order.customer_name,
            items=items,
            total_amount=total
        ))
    return results
