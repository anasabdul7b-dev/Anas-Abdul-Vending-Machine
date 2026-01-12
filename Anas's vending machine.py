# ANAS'S VENDING MACHINE
# This is my vending machine program for the assignment.
# dictionary with all items (code : (name, price))
menu = {
    "1": ("Pepsi", 2.50), "2": ("Coke", 2.50), "3": ("Water", 1.00),
    "4": ("Lays", 3.00), "5": ("Dairy Milk", 4.00), "6": ("Ferrero", 6.00),
    "7": ("Milk", 6.00), "8": ("Orange Juice", 2.00), "9": ("Choco Milk", 2.00),
    "10": ("Gum", 2.50), "11": ("Noodles", 4.00), "12": ("Hot Sauce", 3.00),
    "13": ("Cheetos", 2.50), "14": ("Doritos", 2.00), "15": ("Redbull", 11.00),
    "16": ("KitKat", 2.00), "17": ("Snickers", 2.50), "18": ("Sprite", 2.00),
    "19": ("Fanta", 2.00), "20": ("Iced Tea", 3.00), "21": ("Coffee Can", 4.00),
    "22": ("Protein Bar", 5.00), "23": ("Chips Ahoy", 3.00), "24": ("Twix", 2.50),
    "25": ("Mars Bar", 2.50), "26": ("Pringles", 4.00), "27": ("Popcorn", 3.00),
    "28": ("Energy Bar", 3.50), "29": ("Apple Juice", 2.00), "30": ("Gatorade", 3.00),
    "31": ("Lemonade", 2.00), "32": ("Ice Cream Cup", 4.00), "33": ("Brownie", 3.00),
    "34": ("Muffin", 3.50), "35": ("Croissant", 3.00), "36": ("Sandwich", 5.00),
    "37": ("Wrap", 6.00), "38": ("Salad", 7.00), "39": ("Chocolate Donut", 2.50),
    "40": ("Vanilla Donut", 2.50)
}

# printing the menu so the user can see everything clearly
print("Welcome to my vending machine")
print("Here’s the menu:\n")
for code, item in menu.items():
    print(f"{code}. {item[0]} - ${item[1]}")

# this keeps the program running until the user buys something or quits
running = True

while running:
    # asking the user what they want to buy
    code = input("\nWhat do you want? (Enter code or 'q' to quit): ")

    # if the user wants to quit the program
    if code.lower() == 'q':
        print("Okay, maybe next time.")
        break

    # checking if the entered code exists in the menu
    if code not in menu:
        print("That's not an option, try again.")
        continue

    # getting the item name and price from the dictionary
    name, price = menu[code]
    print(f"That will be ${price}")

    try:
        # trying to convert the input to a number
        user_cash = float(input("Put your money in: "))

        # checking if the user paid enough
        if user_cash < price:
            print(f"Sorry, you need ${round(price - user_cash, 2)} more. Transaction ended.")
            continue

        # calculating change if they paid extra
        change = user_cash - price
        print(f"Enjoy your {name}!")

        # showing change only if needed
        if change > 0:
            print(f"Don't forget your change: ${round(change, 2)}")

        # ending the loop after a successful purchase
        running = False

    except ValueError:
        # this happens when the user enters something that isnt a number
        print("Please enter a number for the money!")