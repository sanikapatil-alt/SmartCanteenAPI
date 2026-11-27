
TAX_RATE = 0.05


def calculate_bill(items, menu):

    subtotal = 0.0

    for ordered_item in items:

        item_id = ordered_item["item_id"]
        quantity = ordered_item["quantity"]

        # Find the food item in the menu
        menu_item = next(
            (item for item in menu
             if item["item_id"] == item_id),
            None
        )

        if menu_item is None:
            raise ValueError(f"Item {item_id} not found")

        if not menu_item["available"]:
            raise ValueError(f"{menu_item['name']} is unavailable")

        price = menu_item["price"]

        subtotal += price * quantity

    tax = round(subtotal * TAX_RATE, 2)

    total = round(subtotal + tax, 2)

    return {
        "subtotal": round(subtotal, 2),
        "tax_rate": TAX_RATE,
        "tax": tax,
        "discount": 0.0,
        "total": total
    }
