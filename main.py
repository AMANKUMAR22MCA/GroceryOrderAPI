from fastapi import FastAPI
from database import Base, engine
from routes import products, orders

app = FastAPI()

# Create DB tables - This will create all the necessary tables in the database
# based on the models when the application starts for the first time.
Base.metadata.create_all(bind=engine)

# Registering routers for product and order endpoints
# These routes are imported from the `routes` module
# They handle all the HTTP requests related to products and orders
app.include_router(products.router)
app.include_router(orders.router)
