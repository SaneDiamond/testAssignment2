from ThemeFactory import ThemeFactory
from SantasWorkshop import SantasWorkshop
from Reindeer import Reindeer
from CandyCanes import CandyCanes
from assignmentFolder import Candy, Toy, StuffedAnimal


class ChristmasFactory(ThemeFactory):
    """Creates Christmas-themed products."""

    def create_toy(self, **kwargs) -> Toy:
        # Santa's Workshop
        return SantasWorkshop(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            has_batteries=kwargs['has_batteries'],
            min_age=kwargs['min_age'],
            dimensions=kwargs['dimensions'],
            num_rooms=kwargs['num_rooms']
        )

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        # Reindeer
        return Reindeer(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            stuffing=kwargs['stuffing'],
            size=kwargs['size'],
            fabric=kwargs['fabric'],
            has_glow=kwargs['has_glow']
        )

    def create_candy(self, **kwargs) -> Candy:
        # Candy Canes
        return CandyCanes(
            name=kwargs['name'],
            product_id=kwargs['product_id'],
            description=kwargs['description'],
            has_nuts=kwargs['has_nuts'],
            has_lactose=kwargs['has_lactose'],
            variety=kwargs['variety']
        )
