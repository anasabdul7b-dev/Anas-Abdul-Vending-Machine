# - ANAS'S VENDING MACHINE -

menu = [
    "1. Pepsi - $2.50", "2. Coke - $2.50", "3. Water - $1.00",
    "4. Lays - $3.00", "5. Dairy Milk - $4.00", "6. Ferrero - $6.00",
    "7. Milk - $6.00", "8. Orange Juice - $2.00", "9. Choco Milk - $2.00",
    "10. Gum - $2.50", "11. Noodles - $4.00", "12. Hot Sauce - $3.00",
    "13. Cheetos - $2.50", "14. Doritos - $2.00", "15. Redbull - $11.00"
]

print("Welcome to my shop!")
for item in menu:
    print(item)

# This loop lets the user try again if they mess up the code
running = True
while running:
    code = input("What do you want? (Enter code or 'q' to quit): ")
    
    if code.lower() == 'q':
        running = False
        break

    # Using a simple check to give price and name
    if code == "1" or code == "2":
        name, price = "Soda", 2.50
    elif code == "3":
        name, price = "Water", 1.00
    elif code == "4" or code == "12" or code == "13":
        
        if code == "4": name = "Lays"
        elif code == "12": name = "Hot Sauce"
        else: name = "Cheetos"
        price = 3.00 if code == "12" else 2.50 
    elif code == "15":
        name, price = "Redbull", 11.00
    else:
        name, price = "Unknown", 0

    if price == 0:
        print("That's not an option, try again.")
        continue

    print(f"That will be ${price}")
    
    # Handling payment
    try:
        user_cash = float(input("Put your money in: "))
        
        if user_cash < price:
            print(f"Sorry, you need ${price - user_cash} more. Transaction ended.")
        else:
            change = user_cash - price
            print(f"Enjoy your {name}!")
            if change > 0:
                print(f"Don't forget your change: ${round(change, 2)}")
            running = False # End the loop after a successful buy
            
    except ValueError:
        print("Please enter a number for the money!")