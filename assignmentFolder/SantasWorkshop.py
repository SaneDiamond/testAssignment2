from Toy import Toy

class SantasWorkshop(Toy):
    """Christmas toy: Santa's Workshop."""

    def __init__(self, name, product_id, description,
                 has_batteries, min_age,
                 dimensions, num_rooms):
        super().__init__(name, product_id, description, has_batteries, min_age)
        self.dimensions = dimensions   # e.g. "20x30"
        self.num_rooms = num_rooms

    def __str__(self):
        return (f"SantasWorkshop({self.name}, ID={self.product_id}, "
                f"has_batteries={self.has_batteries}, min_age={self.min_age}, "
                f"dimensions={self.dimensions}, num_rooms={self.num_rooms})")