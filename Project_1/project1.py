# smart grocery bill generator

# prices(per kg/litre)
rice_price=60
wheat_price=40
sugar_price=50
milk_price=30

#input
name=input("Enter Customer Name:  ")
 
rice_qty=int(input("Enter rice(kg):  ")) 
wheat_qty=int(input("Enter wheat(kg):  ")) 
sugar_qty=int(input("Enter sugar(kg):  "))
milk_qty=int(input("Enter milk(litre):  "))  

#bill calculation
rice_total = rice_qty * rice_price
wheat_total = wheat_qty * wheat_price
sugar_total = sugar_qty * sugar_price
milk_total = milk_qty * milk_price

subtotal=rice_total+wheat_total+sugar_total+milk_total
final_amount=subtotal

# Output
print("\n======== Grocery Bill ========\n")

print("Customer :", name)
print()

print(f"Rice ({rice_qty} kg)      : ₹{rice_total}")
print(f"Wheat ({wheat_qty} kg)     : ₹{wheat_total}")
print(f"Sugar ({sugar_qty} kg)     : ₹{sugar_total}")
print(f"Milk ({milk_qty} L)       : ₹{milk_total}")

print("\nSubtotal        : ₹", subtotal)
print("Final Amount    : ₹", final_amount)

print("\nThank You ")