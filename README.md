# 🛒 Grocery Ordering System API

## 🚀 Project Overview
This project is a **Grocery Ordering System** built with **FastAPI** and **SQLAlchemy**. It allows customers to browse and place grocery orders with full CRUD support for products, orders, and order items.

The backend is designed using clean code principles, modular architecture, and efficient MySQL database handling.

---

## 🧰 Tech Stack

| Component           | Technology            |
|--------------------|------------------------|
| Backend Framework  | FastAPI                |
| Database           | MySQL                  |
| ORM                | SQLAlchemy             |
| Authentication     | JWT (JSON Web Tokens)  |
| Env Configuration  | Pydantic Settings      |
| API Documentation  | Swagger UI (via FastAPI) |
| Code Style         | Modular & Scalable     |

---

## 📁 Project Structure

| Folder/File         | Description |
|---------------------|-------------|
| `db/`               | Handles database connection and session management. |
| `.gitignore`        | Files and directories to be excluded from version control. |
| `models/`           | SQLAlchemy models for Product, Order, and OrderItem tables. |
| `routes/`           | FastAPI route handlers for various endpoints. |
| `schemas/`          | Pydantic models for validation and serialization. |
| `services/`         | Business logic for product and order handling. |
| `utils/`            | Utility functions and custom exception handlers. |
| `config.py`         | App configuration (e.g., database URL, env vars). |
| `database.py`       | Sets up the DB engine and creates tables. |
| `main.py`           | App entry point; registers routes and initializes DB. |
| `requirements.txt`  | Python dependencies for the project. |

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the Repository
git clone https://github.com/your-repository-url.git
cd grocery-ordering-system

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
# (replace with your actual DB credentials)
DATABASE_URL="mysql+pymysql://username:password@localhost:3306/grocery_db"

# 6. Run the Application
uvicorn main:app --reload

