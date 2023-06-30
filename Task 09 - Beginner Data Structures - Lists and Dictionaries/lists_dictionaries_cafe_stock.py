"""
Cafe Stock Management script.
This script calculates the total stock value of items in a cafe.
"""

print("\n-----Hyperion Cafe Stock Report -----\n")

# Menu item list.
menu = ["Coffee", "Tea", "Croissant", "Muffin"]

# Stock level dictionary.
stock = {
    "Coffee": 87,
    "Tea": 92,
    "Croissant": 56,
    "Muffin": 48
    }

# Price dictionary.
price = {
    "Coffee": 1.50,
    "Tea": 1.50,
    "Croissant": 2.20,
    "Muffin": 2.50
}

# Variable to store running stock value total.
total_stock = 0

# Iterates through the menu item list.
for key in menu:
    # Calculates the value of the menu item.
    item_value = stock[key] * price[key]
    
    print(
        f"\n---{key}---\nStock Level: {stock[key]}\nPrice: £{(price[key]):.2f}\n"
        f"{key} Stock Value = £{item_value:.2f}\n"
        )
    
    total_stock += item_value

# Displays the cafe's total stock value to user.
print(f"Total Stock Value: £{total_stock:.2f}")