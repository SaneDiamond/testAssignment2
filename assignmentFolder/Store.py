import datetime
now = datetime.datetime.now()
from OrderError import OrderError

class Store:
    """Manages inventory and daily transaction report."""

    def __init__(self):
        self.inventory = {}  # product_id -> [Items instance, quantity]
        self.daily_transactions = []

    def receive_order(self, order):
        """Process an incoming Order or OrderError."""
        if isinstance(order, OrderError):
            self.daily_transactions.append(
                f"Order {order.order_number}, Could not process order data was corrupted, {order.error_message}"
            )
            return

        if order.product_id not in self.inventory:
            # First time seeing this product, stock 100
            self.inventory[order.product_id] = [order.created_item, 100]

        # Check stock
        item_obj, current_qty = self.inventory[order.product_id]
        if current_qty < order.quantity:
            # Replenish by 100
            self.inventory[order.product_id][1] += 100
            item_obj, current_qty = self.inventory[order.product_id]

        # Deduct
        self.inventory[order.product_id][1] -= order.quantity

        # Log
        self.daily_transactions.append(
            f"Order {order.order_number}, Item {order.item_type}, "
            f"Product ID {order.product_id}, Name \"{order.name}\", Quantity {order.quantity}"
        )

    def check_inventory(self):
        """Print the stock status for each item."""
        print("\n=== Inventory Status ===")
        for product_id, (item_obj, qty) in self.inventory.items():
            if qty >= 10:
                status = "IN STOCK"
            elif 3 <= qty < 10:
                status = "LOW"
            elif 1 <= qty < 3:
                status = "VERY LOW"
            else:
                status = "OUT OF STOCK"
            print(f"Product ID: {product_id}, Name: {item_obj.name}, Qty: {qty}, Status: {status}")
        print("========================\n")

    def generate_daily_transaction_report(self):
        """Write the daily transaction report to a text file."""
        now = datetime.datetime.now()
        filename = f"DTR_{now.strftime('%d%m%y_%H%M')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)\n")
            f.write(now.strftime("%d-%m-%Y %H:%M") + "\n")
            for line in self.daily_transactions:
                f.write(line + "\n")
        print(f"Daily Transaction Report written to: {filename}")
