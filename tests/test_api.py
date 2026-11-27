
import pytest

from fastapi.testclient import TestClient
from app.main import app
from app.storage import json_store


client = TestClient(app)


# Create separate temporary storage for every test
@pytest.fixture(autouse=True)
def setup_test_storage(tmp_path, monkeypatch):
    monkeypatch.setattr(
        json_store,
        "DATA_DIR",
        tmp_path
    )


# Helper function to create a menu item
def create_sample_menu_item():
    response = client.post(
        "/menu/",
        json={
            "item_id": "F001",
            "name": "Veg Burger",
            "price": 80,
            "available": True
        }
    )
    return response


# TEST 1: Create menu item successfully
def test_create_menu_item():

    response = create_sample_menu_item()

    assert response.status_code == 201
    assert response.json()["item"]["name"] == "Veg Burger"


# TEST 2: Reject negative menu price
def test_negative_menu_price():

    response = client.post(
        "/menu/",
        json={
            "item_id": "F002",
            "name": "Pizza",
            "price": -50,
            "available": True
        }
    )

    assert response.status_code == 422


# TEST 3: Create order and calculate bill
def test_create_order_and_bill():

    create_sample_menu_item()

    response = client.post(
        "/orders/",
        json={
            "customer_name": "Sanika",
            "items": [
                {
                    "item_id": "F001",
                    "quantity": 2
                }
            ]
        }
    )

    assert response.status_code == 201

    bill = response.json()["order"]["bill"]

    assert bill["subtotal"] == 160
    assert bill["tax"] == 8
    assert bill["total"] == 168


# TEST 4: Reject negative quantity
def test_negative_order_quantity():

    create_sample_menu_item()

    response = client.post(
        "/orders/",
        json={
            "customer_name": "Sanika",
            "items": [
                {
                    "item_id": "F001",
                    "quantity": -2
                }
            ]
        }
    )

    assert response.status_code == 422


# TEST 5: Reject unknown menu item
def test_unknown_menu_item():

    response = client.post(
        "/orders/",
        json={
            "customer_name": "Sanika",
            "items": [
                {
                    "item_id": "F999",
                    "quantity": 1
                }
            ]
        }
    )

    assert response.status_code == 400


# TEST 6: Return 404 for missing order
def test_missing_order():

    response = client.get("/orders/UNKNOWN")

    assert response.status_code == 404


# TEST 7: Update order status
def test_update_order_status():

    create_sample_menu_item()

    order_response = client.post(
        "/orders/",
        json={
            "customer_name": "Sanika",
            "items": [
                {
                    "item_id": "F001",
                    "quantity": 1
                }
            ]
        }
    )

    order_id = order_response.json()["order"]["order_id"]

    response = client.put(
        f"/orders/{order_id}/status",
        json={"status": "Preparing"}
    )

    assert response.status_code == 200
    assert response.json()["order"]["status"] == "Preparing"


# TEST 8: Verify JSON persistence
def test_order_persistence():

    create_sample_menu_item()

    client.post(
        "/orders/",
        json={
            "customer_name": "Sanika",
            "items": [
                {
                    "item_id": "F001",
                    "quantity": 1
                }
            ]
        }
    )

    saved_orders = json_store.read_json("orders.json")

    assert len(saved_orders) == 1
    assert saved_orders[0]["customer_name"] == "Sanika"
