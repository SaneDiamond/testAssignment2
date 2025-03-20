from ThemeFactory import ThemeFactory
from RobotBunny import RobotBunny
from EasterBunny import EasterBunny
from CremeEggs import CremeEggs
from assignmentFolder import Candy, StuffedAnimal, Toy


class EasterFactory(ThemeFactory):
    """Creates Easter-themed products."""

    def create_toy(self, **kwargs) -> Toy:
        # Robot Bunny
        return RobotBunny(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            has_batteries=kwargs['has_batteries'],
            min_age=kwargs['min_age'],
            num_sound=kwargs['num_sound'],
            colour=kwargs['colour']
        )

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        # Easter Bunny
        return EasterBunny(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            stuffing=kwargs['stuffing'],
            size=kwargs['size'],
            fabric=kwargs['fabric'],
            colour=kwargs['colour']
        )

    def create_candy(self, **kwargs) -> Candy:
        # Creme Eggs
        return CremeEggs(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            has_nuts=kwargs['has_nuts'],
            has_lactose=kwargs['has_lactose'],
            pack_size=kwargs['pack_size']
        )
