from abc import ABC, abstractmethod

from assignmentFolder import Candy, StuffedAnimal, Toy


class ThemeFactory(ABC):
    """Abstract factory for each holiday theme."""

    @abstractmethod
    def create_toy(self, **kwargs) -> Toy:
        pass

    @abstractmethod
    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        pass

    @abstractmethod
    def create_candy(self, **kwargs) -> Candy:
        pass
