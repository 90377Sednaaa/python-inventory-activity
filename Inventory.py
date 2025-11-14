items = []
prices = {}

while True:
    print("\n==== Inventory Menu ====")
    print(f"Current Items: {prices}")
    print("[1] Add Item")
    print("[2] Update Item")
    print("[3] Exit")
    choice = input("Choice: ")

    if choice == '1':
        print(f"\nChoice:1 ")
        while True:
            try:
                item = input("Enter item name: ")
                if item in prices:
                    print(
                        f"{item} already exists in inventory. Please enter a different item.")
                    continue
                price = float(input("Enter item price: "))
                if price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                    continue
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            break
        items.append(item)
        prices[item] = price
        print(f"{item} added successfully! Price: ${price}")

    elif choice == '2':
        print(f"\nChoice:2 ")
        while True:
            try:
                item = input("Enter item name: ")
                if item not in prices:
                    print(f"{item} not found in inventory.")
                    continue
                new_price = float(input("Enter new price: "))
                if new_price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                    continue
                prices[item] = new_price
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            break
        print(f"{item} updated successfully! New Price: ${new_price}")

    elif choice == '3':
        print(f"\nChoice:3 ")
        print("Exiting System...")
        break
    else:
        print("Invalid choice. Please try again.")
