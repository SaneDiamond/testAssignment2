from Candy import Candy

class CremeEggs(Candy):
    """Easter candy: Creme Eggs."""

    def __init__(self, name, product_id, description,
                 has_nuts, has_lactose, pack_size):
        super().__init__(name, product_id, description, has_nuts, has_lactose)
        self.pack_size = pack_size

    def __str__(self):
        return (f"CremeEggs({self.name}, ID={self.product_id}, "
                f"has_nuts={self.has_nuts}, has_lactose={self.has_lactose}, "
                f"pack_size={self.pack_size})")
