from dictionaries import MENU
from dictionaries import RESOURCES

profits = 0

left_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def valid_choice():
    """verifies that the input matches choices in the menu."""
    verified = input("What would you like? (espresso/latte/cappuccino):    ").lower()

    while verified != "espresso" and verified != "latte" and verified != "cappuccino" and verified != "report" and verified != "off":
        verified = input("Unrecognized input. Please select espresso/latte/cappuccino:    ").lower()
    return verified


def resources_needed(chosen_coffee):
    """finds the type of coffee from the menu and returns a list with the needed resources and price"""
    selected = MENU[chosen_coffee]
    cost = selected["cost"]
    ingredients = selected["ingredients"]
    water = ingredients["water"]
    milk = ingredients["milk"]
    coffee = ingredients["coffee"]
    return [water, milk, coffee, cost]


def available_resources():
    """ returns a list of resources from the resources dictionary."""
    water = left_resources["water"]
    milk = left_resources["milk"]
    coffee = left_resources["coffee"]
    return [water, milk, coffee]


def redefine_remaining_resources(requested, temp_available):
    """Updates the remaining resources in left_resources and checks if there's enough to make a coffee"""
    global left_resources
    left_water = temp_available[0] - requested[0]
    left_milk = temp_available[1] - requested[1]
    left_coffee = temp_available[2] - requested[2]

    # redefine dictionary
    left_resources["water"] = left_water
    left_resources["milk"] = left_milk
    left_resources["coffee"] = left_coffee


# output
    if left_water >= 0 and left_milk >= 0 and left_coffee >= 0:
        return True
    else:
        for voice in left_resources:
            quantity_left = left_resources[voice]
            if quantity_left < 0:
                print(f"Sorry, there is not enough {voice}.")
        return False


def insert_money():
    quarters = int(input("How many quarters? : ")) * 0.25
    dimes = int(input("How many dimes? : ")) * 0.10
    nickels = int(input("How many nickels? : ")) * 0.05
    pennies = int(input("How many pennies? : ")) * 0.01
    total = round(quarters + dimes + nickels + pennies, 3)
    return total


def coffe_machine():
    off = False

    while not off:
        global profits
        choice = valid_choice()

        while choice == "report":
            print(f"Profits: ${profits}")
            for key in left_resources:
                value = left_resources[key]
                print(f"{key} : {value}")
            choice = valid_choice()

        if choice == "off":
            off = True

        else:
            needed = resources_needed(choice)
            available = available_resources()
            enough_resources = redefine_remaining_resources(needed, available)
            if enough_resources:
                price = needed[3]
                print(f"{choice}'s price is: ${price}.")
                change = insert_money() - price

                while change < 0:
                    print(f"Oops, there's ${- change} missing.")
                    change += insert_money()

                if change >= 0:
                    profits += price
                    if change > 0:
                        print(f"Here's your change: $ {change}.")

                    print("Here's your coffee :) ")
            else:
                print("Please call maintenance or chose another coffee.")
                coffe_machine()

# BODY
off = True
while off:
    coffe_machine()

    off = True
    print("Turning OFF for maintenance.")
    print(f"Here's the profit ${profits}")
    print("Rebooting.")
    left_resources = RESOURCES
    profits = 0
