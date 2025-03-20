from Candy import Candy
from InvalidDataError import InvalidDataError

class PumpkinCaramelToffee(Candy):
    """Halloween candy: Pumpkin Caramel Toffee."""

    def __init__(self, name, product_id, description,
                 has_nuts, has_lactose, variety):
        super().__init__(name, product_id, description, has_nuts, has_lactose)
        if variety not in ["Sea Salt", "Regular"]:
            raise InvalidDataError("PumpkinCaramelToffee 'variety' must be 'Sea Salt' or 'Regular'")
        self.variety = variety

    def __str__(self):
        return (f"PumpkinCaramelToffee({self.name}, ID={self.product_id}, "
                f"has_nuts={self.has_nuts}, has_lactose={self.has_lactose}, "
                f"variety={self.variety})")
