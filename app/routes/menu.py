
from fastapi import APIRouter, HTTPException, status

from app.models.schemas import MenuItemCreate, MenuItemUpdate
from app.storage.json_store import read_json, write_json


router = APIRouter(
    prefix="/menu",
    tags=["Menu Management"]
)


# CREATE: Add a new food item
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_menu_item(item: MenuItemCreate):

    menu = read_json("menu.json")

    for existing_item in menu:
        if existing_item["item_id"] == item.item_id:
            raise HTTPException(
                status_code=409,
                detail="Item ID already exists"
            )

    new_item = item.model_dump()

    menu.append(new_item)
    write_json("menu.json", menu)

    return {
        "message": "Menu item added successfully",
        "item": new_item
    }


# READ: Get all food items
@router.get("/")
def get_menu():

    menu = read_json("menu.json")

    return {
        "total_items": len(menu),
        "menu": menu
    }


# READ: Get a particular food item
@router.get("/{item_id}")
def get_menu_item(item_id: str):

    menu = read_json("menu.json")

    for item in menu:
        if item["item_id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Menu item not found"
    )


# UPDATE: Modify an existing food item
@router.put("/{item_id}")
def update_menu_item(item_id: str, updated_item: MenuItemUpdate):

    menu = read_json("menu.json")

    for item in menu:
        if item["item_id"] == item_id:

            updates = updated_item.model_dump(exclude_unset=True)

            if not updates:
                raise HTTPException(
                    status_code=400,
                    detail="No update fields provided"
                )

            if any(value is None for value in updates.values()):
                raise HTTPException(
                    status_code=422,
                    detail="Update fields cannot be null"
                )

            item.update(updates)

            write_json("menu.json", menu)

            return {
                "message": "Menu item updated successfully",
                "item": item
            }

    raise HTTPException(
        status_code=404,
        detail="Menu item not found"
    )


# DELETE: Remove a food item
@router.delete("/{item_id}")
def delete_menu_item(item_id: str):

    menu = read_json("menu.json")

    for item in menu:
        if item["item_id"] == item_id:

            menu.remove(item)
            write_json("menu.json", menu)

            return {
                "message": "Menu item deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Menu item not found"
    )
