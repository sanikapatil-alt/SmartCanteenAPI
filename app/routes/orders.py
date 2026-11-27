
from fastapi import APIRouter, HTTPException, status
from uuid import uuid4

from app.models.schemas import OrderCreate, OrderStatusUpdate
from app.storage.json_store import read_json, write_json
from app.services.billing import calculate_bill


router = APIRouter(
    prefix="/orders",
    tags=["Order Management"]
)


# CREATE: Place a new order
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):

    menu = read_json("menu.json")
    orders = read_json("orders.json")

    # Convert Pydantic objects into dictionaries
    ordered_items = [
        item.model_dump() for item in order.items
    ]

    try:
        bill = calculate_bill(ordered_items, menu)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    new_order = {
        "order_id": str(uuid4())[:8].upper(),
        "customer_name": order.customer_name,
        "items": ordered_items,
        "bill": bill,
        "status": "Pending"
    }

    orders.append(new_order)

    write_json("orders.json", orders)

    return {
        "message": "Order created successfully",
        "order": new_order
    }


# READ: Get all orders
@router.get("/")
def get_orders():

    orders = read_json("orders.json")

    return {
        "total_orders": len(orders),
        "orders": orders
    }


# READ: Get a specific order
@router.get("/{order_id}")
def get_order(order_id: str):

    orders = read_json("orders.json")

    for order in orders:
        if order["order_id"] == order_id:
            return order

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )


# UPDATE: Change order status
@router.put("/{order_id}/status")
def update_order_status(
    order_id: str,
    updated_status: OrderStatusUpdate
):

    orders = read_json("orders.json")

    for order in orders:
        if order["order_id"] == order_id:

            order["status"] = updated_status.status

            write_json("orders.json", orders)

            return {
                "message": "Order status updated successfully",
                "order": order
            }

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )
