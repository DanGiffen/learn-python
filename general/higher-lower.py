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


def till(quart, dime, nick, pen, drink):
    """function to calculate if money offered is enough for the drink"""
    cost = MENU[drink]["cost"] * 100
    money_total = (quart * 25) + (dime * 10) + (nick * 5) + (pen * 1)
    if money_total < cost:
        return False
    if money_total > cost:
        refund = (money_total - cost)/100
        print(f"Here is ${refund} in change")
        return True


def resource_check(ingredients):
    """returns true if sufficient resources for drink otherwise false"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f" Sorry there is not enough {item}")
            return False
        return True



    # if MENU[drink]["ingredients"]["water"] > water:
    #     print("Sorry there is not enough water")
    #     return False
    # elif MENU[drink]["ingredients"]["milk"] > milk:
    #     print("Sorry there is not enough milk")
    #     return False
    # elif MENU[drink]["ingredients"]["coffee"] > coffee:
    #     print("Sorry there is not enough coffee")
    #     return False
    # return True


# TODO 1 Prompt for user. While loop, show for next customer. capture drink


# TODO 2 "off" keyword to exit program
def coffeemachine():
    machine_on = True
    money = 0
    # coffee = resources["coffee"]
    # milk = resources["milk"]
    # water = resources["water"]
    while machine_on:
        choice = input(" What would you like? (espresso/latte/cappuccino): ")
        ingredients = MENU[choice]["ingredients"]
        # TODO 3 "report" keyword to call report.
        if choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif choice == "off":
            machine_on = False
        else:
            if resource_check(ingredients):
                print("Please insert coins.")
                quarters = int(input("how many quarters?:"))
                dimes = int(input("how many dimes?:"))
                nickles = int(input("how many nickles?:"))
                pennies = int(input("how many pennies?:"))
                if till(quarters, dimes, nickles, pennies, choice):
                    print(f"Here is your {choice} ☕. Enjoy!")
                    money += MENU[choice]["cost"]
                    for item in ingredients:
                        resources[item] -= ingredients[item]
                    # resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                    # resources["water"] -= MENU[choice]["ingredients"]["water"]
                    # resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                else:
                    print("Sorry that's not enough money. Money refunded.")


coffeemachine()

# TODO 4 report function return resource usage
# TODO 5 Drink choice function. Check resources, print sorry if not enough of a resource
# TODO 6 If statement for drink. If resources prompt for coins.
# TODO 7.0 Calc function to process coins. Convert money to value e.g. quarter = 0.25. 100 pennies is a dollar
# TODO 7.1 Calc to 1 decimal place
# TODO 7.2 Calc function check if sufficient money if not prompt to say not enough, money refund. next customer
# TODO 7.3 Calc function check if too much money change offered with drink


