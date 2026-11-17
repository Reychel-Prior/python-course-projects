from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    user_choice = input("What would you like? " + menu.get_items() + ": ").lower()
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        coffee_maker.report()
    else:
        user_drink = menu.find_drink(user_choice)
        if user_drink is not None:
            if coffee_maker.is_resource_sufficient(user_drink):
                if not money_machine.make_payment(user_drink.cost):
                    print("Sorry, that is insufficient money! Try again.")
                else:
                    coffee_maker.make_coffee(user_drink)
