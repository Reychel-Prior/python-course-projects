MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True
money = 0

def report():
    print("==REPORT==")
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
        print("Money: " + str(money))


while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "off":
        machine_on = False
        print("Maintenance mode - Shutting down coffee machine...")
        break

    elif user_choice == "report":
        report()
        continue

    elif user_choice not in MENU:
        print("Please choose a drink from the menu!\n")
        continue

    drink_ingredients = MENU[user_choice]["ingredients"]

    if isinstance(drink_ingredients, dict):
        for ingredient in drink_ingredients:
            #print(ingredient)
            #print(drink_ingredients[ingredient]) # PRICE

            if drink_ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}!")
                continue

    print("==PAYMENT==")
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickles = int(input("Insert nickles: "))
    pennies = int(input("Insert pennies: "))

    user_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    drink_price = MENU[user_choice]["cost"]
    print(drink_price)

    if user_money < drink_price:
        print("Sorry, that is not enough money! Money refunded.")
        continue

    if user_money > drink_price:
        change = user_money - drink_price
        print("Here is $" + str(round(change, 2)) + " dollars in change.")

    if isinstance(drink_ingredients, dict):
        for ingredient in drink_ingredients:
            resources[ingredient] -= drink_ingredients[ingredient]





