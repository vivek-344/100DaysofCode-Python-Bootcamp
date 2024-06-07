from day16_menu import Menu
from day16_coffee_maker import CoffeeMaker
from day16_money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def execute_order(coffee):
    drink = menu.find_drink(coffee)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)


options = menu.get_items()
order = input(f"What would you like? ({options}): ").lower()
while order != 'off':
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order in ["espresso", "latte", "cappuccino"]:
        execute_order(order)
    else:
        print("Invalid Input!!")
    order = input(f"What would you like? ({options}): ").lower()
print("Shutting down the coffee machine..")
