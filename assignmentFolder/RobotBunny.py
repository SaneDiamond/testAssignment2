from Toy import Toy
from InvalidDataError import InvalidDataError

class RobotBunny(Toy):
    """Easter toy: Robot Bunny."""

    def __init__(self, name, product_id, description,
                 has_batteries, min_age,
                 num_sound, colour):
        super().__init__(name, product_id, description, has_batteries, min_age)
        if colour not in ["Orange", "Blue", "Pink"]:
            raise InvalidDataError("Robot Bunny 'colour' must be 'Orange', 'Blue', or 'Pink'")
        self.num_sound = num_sound
        self.colour = colour

    def __str__(self):
        return (f"RobotBunny({self.name}, ID={self.product_id}, "
                f"has_batteries={self.has_batteries}, min_age={self.min_age}, "
                f"num_sound={self.num_sound}, colour={self.colour})")
