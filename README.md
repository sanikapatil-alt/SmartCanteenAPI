# Smart Canteen Ordering and Billing API

**MCA Python Programming – Industry Case Study 02**

## 1. Project Overview

The Smart Canteen Ordering and Billing API is a Python-based application developed using FastAPI. It is designed to simplify food menu management, customer ordering, billing and order status tracking in a college canteen.

The application replaces manual order recording with REST API endpoints. It uses JSON files for data persistence and Pydantic models for request validation.

This project is an educational prototype and does not process real payments.

## 2. Problem Statement

Traditional college canteens often manage food orders manually, which can result in calculation errors, inefficient order management and difficulties tracking order status.

The proposed system provides an API-based solution to manage menu items, customer orders and billing through a structured application.

## 3. Project Objectives

- Develop REST APIs using FastAPI.
- Manage canteen menu items using CRUD operations.
- Allow customers to create and retrieve orders.
- Calculate bills automatically.
- Update order statuses.
- Store menu and order records in JSON files.
- Validate user input using Pydantic.
- Test API functionality using Pytest.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Programming language |
| FastAPI | REST API development |
| Pydantic | Data validation |
| Uvicorn | Application server |
| JSON | Data persistence |
| Pytest | Automated testing |
| HTTPX | API testing support |

## 5. Features

### Menu Management
- Add new food items.
- View all available menu records.
- Retrieve an item using its ID.
- Update item name, price and availability.
- Delete menu items.
- Prevent duplicate item IDs.

### Order Management
- Create customer orders.
- Support multiple food items in an order.
- Retrieve all orders.
- Retrieve an individual order.
- Update order status.
- Generate unique order IDs.

### Automatic Billing
- Calculate item-wise subtotal.
- Calculate demonstration tax at 5%.
- Apply a discount of ₹0 in the current implementation.
- Calculate the final bill automatically.

### Validation and Error Handling
- Reject negative prices.
- Reject negative quantities.
- Reject unknown menu item IDs.
- Reject unavailable food items.
- Handle missing menu and order records.
- Validate order status values.

## 6. Project Structure

```text
SmartCanteenAPI/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── routes/
│   │   ├── menu.py
│   │   └── orders.py
│   │
│   ├── services/
│   │   └── billing.py
│   │
│   └── storage/
│       └── json_store.py
│
├── data/
│   ├── menu.json
│   └── orders.json
│
├── tests/
│   └── test_api.py
│
├── AI_VERIFICATION_LOG.md
├── README.md
├── requirements.txt
└── pytest.ini
```

## 7. Installation and Setup

### Step 1: Clone or download the project

Open the project folder in Terminal.

### Step 2: Create a virtual environment

```bash
python3 -m venv venv
```

### Step 3: Activate the environment

For macOS/Linux:

```bash
source venv/bin/activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

## 8. Running the Application

Start the FastAPI application using:

```bash
uvicorn app.main:app --reload
```

The application runs locally at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## 9. API Endpoints

### Menu Management

| Method | Endpoint | Description |
|---|---|---|
| GET | /menu/ | View all menu items |
| POST | /menu/ | Add a menu item |
| GET | /menu/{item_id} | Retrieve an item |
| PUT | /menu/{item_id} | Update an item |
| DELETE | /menu/{item_id} | Delete an item |

### Order Management

| Method | Endpoint | Description |
|---|---|---|
| POST | /orders/ | Create an order |
| GET | /orders/ | Retrieve all orders |
| GET | /orders/{order_id} | Retrieve a specific order |
| PUT | /orders/{order_id}/status | Update order status |

## 10. Sample Order Request

```json
{
  "customer_name": "Sanika",
  "items": [
    {
      "item_id": "F001",
      "quantity": 2
    }
  ]
}
```

### Sample Billing Calculation

For two Veg Burgers costing ₹80 each:

- Subtotal: ₹160
- Demonstration tax (5%): ₹8
- Discount: ₹0
- Total: ₹168

## 11. Order Status Values

The application supports the following statuses:

- Pending
- Preparing
- Ready
- Completed

## 12. Running Automated Tests

Execute the following command:

```bash
python -m pytest -v
```

### Test Results

The implemented test suite contains eight test cases covering:

1. Successful menu item creation.
2. Negative price validation.
3. Order creation and bill calculation.
4. Negative quantity validation.
5. Unknown menu item validation.
6. Missing order handling.
7. Order status updates.
8. JSON persistence.

**Observed test result:** 8 passed, 0 failed.

## 13. Data Persistence

The application stores data in two JSON files:

- `menu.json` – Stores food menu records.
- `orders.json` – Stores customer orders and billing information.

The storage module uses temporary-file replacement when writing updated JSON data.

## 14. Known Limitations

- JSON files are used instead of a production database.
- Concurrent writes are not protected by database transactions or locking.
- The application does not process real payments.
- Authentication and role-based access control are not implemented.
- The tax rate is an illustrative project assumption.
- The application is designed as an educational prototype rather than a production canteen system.

## 15. Conclusion

The Smart Canteen Ordering and Billing API demonstrates the practical use of Python programming, REST API development, Pydantic validation, JSON file handling, business logic and automated testing.

The project provides a basic digital solution for managing college canteen operations and demonstrates important software development concepts through an industry-oriented case study.