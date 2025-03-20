class OrderError:
    """Represents an order that could not be processed due to error."""

    def __init__(self, order_number, error_message):
        self.order_number = order_number
        self.error_message = error_message
