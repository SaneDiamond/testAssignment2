from StuffedAnimal import StuffedAnimal

class Reindeer(StuffedAnimal):
    """Christmas stuffed animal: Reindeer."""

    def __init__(self, name, product_id, description,
                 stuffing, size, fabric, has_glow):
        super().__init__(name, product_id, description, stuffing, size, fabric)
        self.has_glow = has_glow  # bool

    def __str__(self):
        return (f"Reindeer({self.name}, ID={self.product_id}, "
                f"stuffing={self.stuffing}, size={self.size}, fabric={self.fabric}, "
                f"has_glow={self.has_glow})")