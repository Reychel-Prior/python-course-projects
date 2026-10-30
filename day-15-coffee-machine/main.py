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
    pass


while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino)")

    if user_choice == "off":
        machine_on = False
        print("Maintenance mode - Shutting down coffee machine...")
        break

    if user_choice == "report":
        report()