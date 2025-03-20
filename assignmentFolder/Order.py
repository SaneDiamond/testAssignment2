from assignmentFolder import Items, ThemeFactory


class Order:
    """Holds information about a single order."""

    def __init__(self, order_number: int, product_id: str, quantity: int,
                 item_type: str, name: str, product_details: dict,
                 factory: ThemeFactory, created_item: Items = None):
        self.order_number = order_number
        self.product_id = product_id
        self.quantity = quantity
        self.item_type = item_type
        self.name = name
        self.product_details = product_details
        self.factory = factory
        self.created_item = created_item

    def __str__(self):
        return (f"Order({self.order_number}, product_id={self.product_id}, "
                f"quantity={self.quantity}, item_type={self.item_type}, name={self.name})")
