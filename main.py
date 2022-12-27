from machine import MENU, resources


# Keep machine on
is_on = True

money = 0


# TODO Make a function that gives the user their request and reduces from the total resources
def action():
    global money
    for item in resources:
        if item in MENU[request]['ingredients']:
            resources[item] -= MENU[request]['ingredients'][item]
    money += MENU[request]['cost']
    print(f"Here is your {request} ☕, enjoy!")


def enough_resources(order_ingredients):
    """Returns True if order can be made, False if ingredients insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennie?: ")) * 0.01
    return total


# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino)
# Ask what the user wants
global request
while is_on:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "report":
        print(f"coffee: {resources['coffee']}g")
        print(f"milk: {resources['milk']}ml")
        print(f"water: {resources['water']}ml")
        print(f"money: ${money}")
    elif request == "off":
        is_on = False
    # Check if resources are enough elif resources['water'] > MENU[request]['ingredients']['water'] and resources[
    # 'milk'] > MENU[request]['ingredients']['milk'] and resources['coffee'] > MENU[request]['ingredients'][
    # 'coffee']: action()

    else:
        if request in MENU:
            drink = MENU[request]
            if enough_resources(drink['ingredients']):
                payment = process_coins()
                change = round(payment - drink['cost'], 2)
                if payment >= MENU[request]['cost']:
                    print(f"Here is ${change} in change")
                    action()
                else:
                    print("Sorry, that isn't enough money")
        else:
            print(f"Please use an existing choice")
