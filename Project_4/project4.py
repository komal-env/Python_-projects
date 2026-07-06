# Restaurant Ordering System

menu = (
    (1, "Chole Bhature", 120),
    (2, "Litti Chokha", 250),
    (3, "Paneer Chilli", 100),
    (4, "Dosa", 90),
    (5, "Lassi", 50),
    (6, "Aaam Panna", 80),
    (7, "Idli", 180),
    (8, "Jalebi", 150)
)

cart = []
customer = {}
unique_items = set()


def show_menu():
    print("\n========== RESTAURANT MENU ==========")
    print("ID\tItem\t\tPrice")
    print("-------------------------------------")
    for item in menu:
        print(f"{item[0]}\t{item[1]}\t\t₹{item[2]}")


def place_order():
    global customer

    if not customer:
        customer["name"] = input("Enter Customer Name: ")

        while True:
            mobile = input("Enter Mobile Number: ")
            if mobile.isdigit() and len(mobile) == 10:
                customer["mobile"] = mobile
                break
            else:
                print("Invalid Mobile Number!")

    while True:
        try:
            item_id = int(input("\nEnter Item ID (0 to Stop): "))

            if item_id == 0:
                break

            found = False

            for item in menu:
                if item[0] == item_id:
                    found = True

                    qty = int(input("Enter Quantity: "))

                    if qty < 1:
                        print("Quantity must be greater than 0")
                        break

                    cart.append({
                        "item": item[1],
                        "price": item[2],
                        "qty": qty
                    })

                    unique_items.add(item[1])

                    print(item[1], "added successfully!")
                    break

            if not found:
                print("Invalid Item ID!")

        except ValueError:
            print("Invalid Input!")


def view_cart():
    if not cart:
        print("\nCart is Empty!")
        return

    print("\n========== YOUR CART ==========")

    total = 0

    for item in cart:
        amount = item["price"] * item["qty"]
        total += amount

        print(f'{item["item"]} x{item["qty"]} = ₹{amount}')

    print("-----------------------------")
    print("Cart Total = ₹", total)


def remove_item():
    if not cart:
        print("Cart is Empty!")
        return

    name = input("Enter Item Name to Remove: ").lower()

    for item in cart:
        if item["item"].lower() == name:
            cart.remove(item)
            print("Item Removed Successfully!")
            return

    print("Item Not Found!")


def generate_bill():
    if not cart:
        print("Cart is Empty!")
        return

    subtotal = 0

    print("\n==============================")
    print("      RESTAURANT BILL")
    print("==============================")

    print("Customer :", customer["name"])
    print("Mobile   :", customer["mobile"])
    print()

    for item in cart:
        amount = item["price"] * item["qty"]
        subtotal += amount

        print(f'{item["item"]} x{item["qty"]}\t₹{amount}')

    gst = subtotal * 0.05
    final = subtotal + gst

    print("------------------------------")
    print(f"Subtotal : ₹{subtotal}")
    print(f"GST (5%) : ₹{gst:.2f}")
    print(f"Final Bill : ₹{final:.2f}")
    print("------------------------------")
    print("Unique Items Ordered :", unique_items)
    print("\nThank You!")
    print("Visit Again ❤️")


def save_order():
    if not cart:
        print("No Order to Save!")
        return

    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["qty"]

    gst = subtotal * 0.05
    final = subtotal + gst

    with open("orders.txt", "a") as file:

        file.write("\nCustomer : " + customer["name"] + "\n")
        file.write("Mobile : " + customer["mobile"] + "\n")

        for item in cart:
            file.write(f'{item["item"]} x{item["qty"]}\n')

        file.write(f"Total : ₹{final:.2f}\n")
        file.write("-----------------------------\n")

    print("Order Saved Successfully!")


def view_previous_orders():
    try:
        with open("orders.txt", "r") as file:
            print("\n====== PREVIOUS ORDERS ======\n")
            print(file.read())

    except FileNotFoundError:
        print("No Previous Orders Found!")


def main():

    while True:

        print("\n")
        print("====== RESTAURANT ORDERING SYSTEM ======")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. View Cart")
        print("4. Remove Item")
        print("5. Generate Bill")
        print("6. Save Order")
        print("7. View Previous Orders")
        print("8. Exit")

        try:
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                show_menu()

            elif choice == 2:
                place_order()

            elif choice == 3:
                view_cart()

            elif choice == 4:
                remove_item()

            elif choice == 5:
                generate_bill()

            elif choice == 6:
                save_order()

            elif choice == 7:
                view_previous_orders()

            elif choice == 8:
                print("Thank You for Visiting!")
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter Numbers Only!")


main()