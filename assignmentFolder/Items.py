from abc import ABC, abstractmethod

class Items(ABC):
    """Abstract base class for all items in the store."""

    def __init__(self, name: str, product_id: str, description: str):
        self.name = name
        self.product_id = product_id
        self.description = description

    @abstractmethod
    def __str__(self):
        pass