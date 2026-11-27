
from typing import Literal
from pydantic import BaseModel, Field


# ==========================================
# 1. MENU ITEM CREATE MODEL
# ==========================================

class MenuItemCreate(BaseModel):
    item_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    available: bool = True


# ==========================================
# 2. MENU ITEM UPDATE MODEL
# ==========================================

class MenuItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    price: float | None = Field(default=None, gt=0)
    available: bool | None = None


# ==========================================
# 3. ORDER ITEM CREATE MODEL
# ==========================================

class OrderItemCreate(BaseModel):
    item_id: str = Field(min_length=1)
    quantity: int = Field(gt=0)


# ==========================================
# 4. ORDER CREATE MODEL
# ==========================================

class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=1)
    items: list[OrderItemCreate] = Field(min_length=1)


# ==========================================
# 5. ORDER STATUS UPDATE MODEL
# ==========================================

class OrderStatusUpdate(BaseModel):
    status: Literal[
        "Pending",
        "Preparing",
        "Ready",
        "Completed"
    ]
