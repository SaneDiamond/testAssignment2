from Candy import Candy
from InvalidDataError import InvalidDataError

class CandyCanes(Candy):
    """Christmas candy: Candy Canes."""

    def __init__(self, name, product_id, description,
                 has_nuts, has_lactose, colour):
        super().__init__(name, product_id, description, has_nuts, has_lactose)
        if colour not in ["Red", "Green"]:
            raise InvalidDataError("Candy Canes 'colour' must be 'Red' or 'Green'")
        self.colour = colour

    def __str__(self):
        return (f"CandyCanes({self.name}, ID={self.product_id}, "
                f"has_nuts={self.has_nuts}, has_lactose={self.has_lactose}, "
                f"colour={self.colour})")
