from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
pos_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    input_msg = f"What would you like? ({menu.get_items()}): "
    user_choice = input(input_msg).lower()

    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        coffee_machine.report()
        pos_machine.report()
    else:
        drink = menu.find_drink(user_choice)

        if drink is None:
            continue

        if not coffee_machine.is_resource_sufficient(drink):
            continue

        if not pos_machine.make_payment(drink.cost):
            continue

        coffee_machine.make_coffee(drink)
