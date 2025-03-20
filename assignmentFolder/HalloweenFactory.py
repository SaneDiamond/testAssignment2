from ThemeFactory import ThemeFactory
from RCSpider import RCSpider
from DancingSkeleton import  DancingSkeleton
from PumpkinCaramelToffee import PumpkinCaramelToffee
from assignmentFolder import Candy, StuffedAnimal, Toy


class HalloweenFactory(ThemeFactory):
    """Creates Halloween-themed products."""

    def create_toy(self, **kwargs) -> Toy:
        # RC Spider
        return RCSpider(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            has_batteries=kwargs['has_batteries'],
            min_age=kwargs['min_age'],
            speed=kwargs['speed'],
            jump_height=kwargs['jump_height'],
            has_glow=kwargs['has_glow'],
            spider_type=kwargs['spider_type']
        )

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        # Dancing Skeleton
        return DancingSkeleton(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            stuffing=kwargs['stuffing'],
            size=kwargs['size'],
            fabric=kwargs['fabric'],
            has_glow=kwargs['has_glow']
        )

    def create_candy(self, **kwargs) -> Candy:
        # Pumpkin Caramel Toffee
        return PumpkinCaramelToffee(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            has_nuts=kwargs['has_nuts'],
            has_lactose=kwargs['has_lactose'],
            variety=kwargs['variety']
        )