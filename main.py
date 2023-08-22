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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resourcess_sufficient(ordered_ingredients):

    """ return true if the ordered ingredients are lesser than
    resources, then return false if the ordered ingredients are greater
    than the resources """

    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def insert_coins():

    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):

    """ return True if the payment is successful or False if money is
    insufficient"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} dollars in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def coffee(drink_name,ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}.Enjoy")



is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "Report".lower():
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:

        user_want = MENU[user_choice]
        if is_resourcess_sufficient(ordered_ingredients=user_want['ingredients']):
            payment = insert_coins()
            if is_transaction_successful(payment,user_want['cost']):
                coffee(user_choice,user_want['ingredients'])
