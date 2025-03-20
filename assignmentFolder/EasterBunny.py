from StuffedAnimal import StuffedAnimal
from InvalidDataError import InvalidDataError

class EasterBunny(StuffedAnimal):
    """Easter stuffed animal: Easter Bunny."""

    def __init__(self, name, product_id, description,
                 stuffing, size, fabric, colour):
        super().__init__(name, product_id, description, stuffing, size, fabric)
        if colour not in ["White", "Grey", "Pink", "Blue"]:
            raise InvalidDataError("Easter Bunny 'colour' must be 'White', 'Grey', 'Pink', or 'Blue'")
        self.colour = colour

    def __str__(self):
        return (f"EasterBunny({self.name}, ID={self.product_id}, "
                f"stuffing={self.stuffing}, size={self.size}, fabric={self.fabric}, "
                f"colour={self.colour})")
