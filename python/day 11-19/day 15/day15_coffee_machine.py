from day15_coffee_machine_menu import MENU

cash = 0
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    money = "{:.2f}".format(round(cash, 2))
    print(f"Water: {resource["water"]}ml\nMilk: {resource["milk"]}ml\nCoffee: {resource["coffee"]}g\nMoney: ${money}")


def check_resources(coffee):
    if resource["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    if resource["milk"] < MENU[coffee]["ingredients"]["milk"]:
        print("Sorry there is not enough water.")
        return False
    if resource["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough water.")
        return False
    return True


def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many quarters?: "))
    nickles = int(input("How many quarters?: "))
    pennies = int(input("How many quarters?: "))
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01


def resources(coffee):
    resource["water"] -= MENU[coffee]["ingredients"]["water"]
    resource["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resource["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def transaction(coffee, money):
    global cash
    cash += MENU[coffee]["cost"]
    change = "{:.2f}".format(round(money - MENU[coffee]["cost"], 2))
    print(f"Change Refunded: ${change}")


def execute_order(coffee):
    if check_resources(coffee):
        total = coins()
        if total >= MENU[coffee]["cost"]:
            resources(coffee)
            print(f"Transaction Successful! Here is your {coffee.title()}!")
            transaction(coffee, total)
        else:
            print("Insufficient Money! Transaction Failed!!")


def load_machine():
    resource["water"] += int(input("Enter the amount of water to add: "))
    resource["milk"] += int(input("Enter the amount of milk to add: "))
    resource["coffee"] += int(input("Enter the amount of coffee to add: "))


order = input("What would you like? (espresso/latte/cappuccino): ").lower()
while order != 'off':
    if order == "report":
        report()
    elif order in ["espresso", "latte", "cappuccino"]:
        execute_order(order)
    elif order == "load":
        load_machine()
    else:
        print("Invalid Input!!")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
print("Shutting down the coffee machine..")
