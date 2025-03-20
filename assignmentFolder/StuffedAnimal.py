from InvalidDataError import InvalidDataError
from assignmentFolder.Items import Items


class StuffedAnimal(Items):
    """Base class for Stuffed Animal items."""

    def __init__(self, name: str, product_id: str, description: str,
                 stuffing: str, size: str, fabric: str):
        super().__init__(name, product_id, description)

        valid_stuffings = ["Polyester Fibrefill", "Wool"]
        if stuffing not in valid_stuffings:
            raise InvalidDataError(f"Stuffing can only be {valid_stuffings}")

        valid_sizes = ["S", "M", "L"]
        if size not in valid_sizes:
            raise InvalidDataError(f"Size can only be {valid_sizes}")

        valid_fabrics = ["Linen", "Cotton", "Acrylic"]
        if fabric not in valid_fabrics:
            raise InvalidDataError(f"Fabric can only be {valid_fabrics}")

        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric

    def __str__(self):
        return (f"StuffedAnimal({self.name}, ID={self.product_id}, "
                f"stuffing={self.stuffing}, size={self.size}, fabric={self.fabric})")