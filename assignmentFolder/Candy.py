from assignmentFolder.Items import Items


class Candy(Items):
    """Base class for Candy items."""

    def __init__(self, name: str, product_id: str, description: str,
                 has_nuts: bool, has_lactose: bool):
        super().__init__(name, product_id, description)
        self.has_nuts = has_nuts
        self.has_lactose = has_lactose

    def __str__(self):
        return (f"Candy({self.name}, ID={self.product_id}, "
                f"has_nuts={self.has_nuts}, has_lactose={self.has_lactose})")