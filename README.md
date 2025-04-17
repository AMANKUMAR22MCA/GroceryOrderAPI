 # 🛒 Grocery Ordering System API

## 🚀 Project Overview
This project is a **Grocery Ordering System** built with **FastAPI** and **SQLAlchemy**. It allows customers to browse and place grocery orders with full support for products, orders, and order items.

The backend is designed using clean code principles, modular architecture, and efficient MySQL database handling.

---

## 🧰 Tech Stack

| Component           | Technology              |
|--------------------|--------------------------|
| Backend Framework  | FastAPI                  |
| Database           | MySQL                    |
| ORM                | SQLAlchemy               |
| Env Configuration  | Pydantic Settings        |
| API Documentation  | Swagger UI (via FastAPI) |
| Code Style         | Modular & Scalable       |

---

## 📁 Project Structure

| Folder/File         | Description                                                  |
|---------------------|--------------------------------------------------------------|
| `db/`               | Handles database connection and session management.          |
| `.gitignore`        | Files and directories to be excluded from version control.   |
| `models/`           | SQLAlchemy models for Product, Order, and OrderItem tables.  |
| `routes/`           | FastAPI route handlers for various endpoints.                |
| `schemas/`          | Pydantic models for validation and serialization.            |
| `services/`         | Business logic for product and order handling.               |
| `utils/`            | Utility functions and custom exception handlers.             |
| `config.py`         | App configuration (e.g., database URL, env vars).            |
| `database.py`       | Sets up the DB engine and creates tables.                    |
| `main.py`           | App entry point; registers routes and initializes DB.         |
| `requirements.txt`  | Python dependencies for the project.                         |

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the Repository
git clone https://github.com/AMANKUMAR22MCA/GroceryOrderAPI.git
cd GroceryOrderAPI

# 2. Create a Virtual Environment
python -m venv venv

# 3. Activate the Virtual Environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 4. Install Dependencies
pip install -r requirements.txt

# 5. Configure Environment Variables
# Create a .env file in the root directory with the following content:

DATABASE_URL="mysql+pymysql://username:password@localhost:3306/grocery_db"
Note : I am using mysql db change localhost and other details according to your db and keep your
database open in my case i will open the my sql workbench .

# 6. Run the Application
uvicorn main:app --reload
```

---

Now visit the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Endpoints

### 🧺 Product Endpoints

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| GET    | `/products`      | Get all products      |
| GET    | `/products/{id}` | Get a product by ID   |
| POST   | `/products`      | Create a new product  |
| PUT    | `/products/{id}` | Update product by ID  |
| DELETE | `/products/{id}` | Delete product by ID  |

#### 📥 Sample Request Body for `POST /products`

```json
{
  "name": "Bread",
  "price_per_unit": 45,
  "unit": "kg"
}
```
![image](https://github.com/user-attachments/assets/ca3d97b3-d1ba-47e3-b292-76fb1620b2bd)


### 🧾 Order Endpoints

| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| GET    | `/orders`        | Get all orders       |
| GET    | `/orders/{id}`   | Get an order by ID   |
| POST   | `/orders`        | Create a new order   |
| PUT    | `/orders/{id}`   | Update order by ID   |
| DELETE | `/orders/{id}`   | Delete order by ID   |

#### 📥 Sample Request Body for `POST /orders`

```json
{
  "customer_name": "John Doe",
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 5,
      "quantity": 1
    }
  ]
}
```
![image](https://github.com/user-attachments/assets/cbe5684b-d337-40f5-81a2-b0d595c90665)

---

## 🔧 Services

| File                          | Description                                                      |
|-------------------------------|------------------------------------------------------------------|
| `services/product_service.py` | 📦 Handles all product operations: create, read . |
| `services/order_service.py`   | 🧾 Processes order creation, total calculation, list all orders.|

---

## 🛠️ Utilities

| File                     | Description                                                                      |
|--------------------------|----------------------------------------------------------------------------------|
| `utils/exceptions.py`   | ❗ Used for raising structured HTTP errors like 404 (Not Found), 400 (Bad Request), etc. |

### 🔍 Example

```python
def raise_not_found(message):
    raise HTTPException(status_code=404, detail=message)
```

---

## 🗃️ Models

| Model         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| 🛒 `Product`   | Represents a grocery product with attributes like `name`, `price_per_unit`, and `unit`. |
| 📦 `Order`     | Represents a customer order, including the customer's name.                |
| 📄 `OrderItem` | Represents an item in an order, linking a product with a `quantity`.       |

---

## 🗄️ Database

All database configuration and session management are handled in the `database.py` file.

This includes setting up the connection engine and creating tables using SQLAlchemy’s `Base.metadata`.

### 🔧 Table Creation Example

```python
Base.metadata.create_all(bind=engine)
```

