from abc import ABC, abstractmethod

from assignmentFolder.Items import Items


class Toy(Items):
    """Base class for Toy items."""

    def __init__(self, name: str, product_id: str, description: str,
                 has_batteries: bool, min_age: int):
        super().__init__(name, product_id, description)
        self.has_batteries = has_batteries
        self.min_age = min_age

    def __str__(self):
        return (f"Toy({self.name}, ID={self.product_id}, "
                f"has_batteries={self.has_batteries}, min_age={self.min_age})")

