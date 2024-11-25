from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
#print(machine.resources.items())

# print(till.report())
# print(machine.report())

is_on = True
profit = 0

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)




