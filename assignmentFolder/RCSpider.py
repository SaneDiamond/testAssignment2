from Toy import Toy
from InvalidDataError import InvalidDataError

class RCSpider(Toy):
    """Halloween toy: RC Spider."""

    def __init__(self, name, product_id, description,
                 has_batteries, min_age,
                 speed, jump_height, has_glow, spider_type):
        super().__init__(name, product_id, description, has_batteries, min_age)
        if spider_type not in ["Tarantula", "Wolf Spider"]:
            raise InvalidDataError("spider_type must be 'Tarantula' or 'Wolf Spider'")
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow  # bool
        self.spider_type = spider_type

    def __str__(self):
        return (f"RCSpider({self.name}, ID={self.product_id}, "
                f"has_batteries={self.has_batteries}, min_age={self.min_age}, "
                f"speed={self.speed}, jump_height={self.jump_height}, "
                f"has_glow={self.has_glow}, spider_type={self.spider_type})")

