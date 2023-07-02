from data import MENU, resources


def print_report(money: int):
    """Accepts amount of money collected as a parameter
       and prints a formatted report about remaining
       resources and amount of money collected."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def get_money_from_user():
    """Prompts the users for the number of each supported type of coin.
       Calculates and returns the total money."""
    print("Please insert coins.")
    coins = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
    value = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    for coin_type in coins:
        coins[coin_type] = int(input(f"How many {coin_type}?: "))

    total_money = 0
    for coin_type in coins:
        total_money += coins[coin_type] * value[coin_type]

    return total_money


def resources_available(ingredients_for_drink: dict):
    """Returns true if the machine has enough resources,
       for the selected type of drink."""
    for ingredient, amount in ingredients_for_drink.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


def update_resources(ingredients: dict):
    """Deducts the ingredients used by the current drink
       from the machine's resources."""
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount


def coffee_machine():
    """The main coffee machine brains"""
    money_in_machine = 0
    machine_on = True

    while machine_on:
        input_msg = "What would you like? (espresso/latte/cappuccino): "
        user_choice = input(input_msg).lower()
        if user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            print_report(money_in_machine)
        elif user_choice in MENU:
            if not resources_available(MENU[user_choice]["ingredients"]):
                continue

            inserted_money = get_money_from_user()
            drink_cost = MENU[user_choice]["cost"]

            if inserted_money < drink_cost:
                print("Sorry that's not enough money. Money refunded.")
                continue

            money_in_machine += drink_cost
            change = inserted_money - drink_cost

            update_resources(MENU[user_choice]["ingredients"])

            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {user_choice} ☕️.Enjoy!")
        else:
            print("Invalid input. Please retry...")


coffee_machine()
