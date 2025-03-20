from Store import Store
from OrderProcessor import OrderProcessor

def main():
    store = Store()
    processor = OrderProcessor()

    while True:
        print("========= HOLIDAY STORE =========")
        print("1. Process Web Orders")
        print("2. Check Inventory")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            filename = input("Enter the Excel filename (e.g. orders.xlsx): ").strip()
            for ord_obj in processor.process_orders(filename):
                store.receive_order(ord_obj)

        elif choice == '2':
            store.check_inventory()

        elif choice == '3':
            store.generate_daily_transaction_report()
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
