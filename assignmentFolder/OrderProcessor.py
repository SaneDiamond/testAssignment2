import pandas as pd
from InvalidDataError import InvalidDataError
from Order import Order
from OrderError import OrderError
from ChristmasFactory import ChristmasFactory
from HalloweenFactory import HalloweenFactory
from EasterFactory import EasterFactory

class OrderProcessor:
    """Responsible for reading the Excel and creating Orders."""

    def __init__(self):
        self.factory_mapping = {
            'Christmas': ChristmasFactory(),
            'Halloween': HalloweenFactory(),
            'Easter': EasterFactory()
        }

    def process_orders(self, filename: str):
        """Read the Excel file and yield Order or OrderError objects."""
        try:
            df = pd.read_excel(filename)
        except Exception as e:
            yield OrderError(None, f"Could not read file '{filename}': {e}")
            return

        for index, row in df.iterrows():
            order_number = row.get('order_number', None)
            try:
                holiday = row['holiday']
                item_type = row['item']
                factory = self.factory_mapping.get(holiday, None)
                if factory is None:
                    raise InvalidDataError(f"Unknown holiday: {holiday}")

                product_id = row['product_id']
                quantity = int(row['quantity'])
                name = row['name']
                description = row['description']

                # Collect remaining columns into product_details
                product_details = {}
                for col in row.index:
                    if col not in [
                        'order_number', 'holiday', 'item', 'quantity',
                        'name', 'product_id', 'description'
                    ]:
                        product_details[col] = row[col]

                # Convert any NaNs to None
                for k, v in product_details.items():
                    if pd.isna(v):
                        product_details[k] = None

                # Attempt to create the item now
                created_item = None
                if item_type == 'Toy':
                    created_item = factory.create_toy(
                        name=name,
                        product_id=product_id,
                        description=description,
                        **product_details
                    )
                elif item_type == 'StuffedAnimal':
                    created_item = factory.create_stuffed_animal(
                        name=name,
                        product_id=product_id,
                        description=description,
                        **product_details
                    )
                elif item_type == 'Candy':
                    created_item = factory.create_candy(
                        name=name,
                        product_id=product_id,
                        description=description,
                        **product_details
                    )
                else:
                    raise InvalidDataError(f"Unknown item type: {item_type}")

                yield Order(
                    order_number=order_number,
                    product_id=product_id,
                    quantity=quantity,
                    item_type=item_type,
                    name=name,
                    product_details=product_details,
                    factory=factory,
                    created_item=created_item
                )

            except Exception as e:
                yield OrderError(order_number, f"{type(e).__name__} - {e}")
