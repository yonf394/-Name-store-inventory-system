# ============================================
# Store Inventory Management System
# ============================================

products = []

# 1. Add Product
def add_product():
    print("\n--- Add Product ---")
    name = input("Enter product name: ").strip()

    if not name:
        print("X Product name cannot be empty.")
        return

    for product in products:
        if product["name"].lower() == name.lower():
            print(f"X Product '{name}' already exists.")
            return

    try:
        price = float(input("Enter price: "))
        if price < 0:
            print("X Price must be a positive number.")
            return
    except ValueError:
        print("X Invalid price.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("X Quantity must be a positive number.")
            return
    except ValueError:
        print("X Invalid quantity.")
        return

    products.append({"name": name, "price": price, "quantity": quantity})
    print(f"Product '{name}' added successfully!")


# 2. Display All Products
def display_products():
    print("\n--- All Products ---")
    if not products:
        print("No products in inventory.")
        return

    print(f"{'Name':<20} {'Price':>10} {'Quantity':>10}")
    print("-" * 42)
    for product in products:
        print(f"{product['name']:<20} {product['price']:>10.2f} {product['quantity']:>10}")


# 3. Search for Product
def search_product():
    print("\n--- Search Product ---")
    name = input("Enter product name to search: ").strip()

    for product in products:
        if product["name"].lower() == name.lower():
            print(f"\nProduct Found:")
            print(f"  Name     : {product['name']}")
            print(f"  Price    : {product['price']:.2f}")
            print(f"  Quantity : {product['quantity']}")
            return

    print(f"X Product '{name}' not found.")


# 4. Update Product
def update_product():
    print("\n--- Update Product ---")
    name = input("Enter product name to update: ").strip()

    for product in products:
        if product["name"].lower() == name.lower():
            new_price = input(f"New price (current: {product['price']:.2f}) or Enter to skip: ").strip()
            if new_price:
                try:
                    new_price = float(new_price)
                    if new_price >= 0:
                        product["price"] = new_price
                except ValueError:
                    print("X Invalid price. Skipping.")

            new_qty = input(f"New quantity (current: {product['quantity']}) or Enter to skip: ").strip()
            if new_qty:
                try:
                    new_qty = int(new_qty)
                    if new_qty >= 0:
                        product["quantity"] = new_qty
                except ValueError:
                    print("X Invalid quantity. Skipping.")

            print(f"Product '{product['name']}' updated successfully!")
            return

    print(f"X Product '{name}' not found.")


# 5. Delete Product
def delete_product():
    print("\n--- Delete Product ---")
    name = input("Enter product name to delete: ").strip()

    for product in products:
        if product["name"].lower() == name.lower():
            products.remove(product)
            print(f"Product '{name}' deleted successfully!")
            return

    print(f"X Product '{name}' not found.")


# 6. Total Inventory Value
def total_value():
    print("\n--- Total Inventory Value ---")
    if not products:
        print("No products in inventory.")
        return

    total = 0
    for product in products:
        total += product["price"] * product["quantity"]

    print(f"Total Inventory Value: {total:.2f}")


# Main Menu
def main_menu():
    while True:
        print("\n===== Store Inventory System =====")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Search for Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Show Total Inventory Value")
        print("7. Exit")
        print("==================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            total_value()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("X Invalid choice. Please enter a number from 1 to 7.")


main_menu()