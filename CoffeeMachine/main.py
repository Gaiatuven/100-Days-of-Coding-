resources = {
    'water': 1000,   # in ml
    'milk': 500,     # in ml
    'coffee': 250,   # in g
    'money': 0       # in $
}

MENU = {
    'espresso': {'water': 50, 'milk': 0, 'coffee': 18, 'cost': 1.5},
    'latte': {'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.5},
    'cappuccino': {'water': 250, 'milk': 100, 'coffee': 24, 'cost': 3.0}
}

def print_report():
    print("Current resources:")
    for resource, amount in resources.items():
        if resource == 'money':
            print(f"{resource.capitalize()}: ${amount:.2f}")
        else:
            print(f"{resource.capitalize()}: {amount}ml" if resource != 'coffee' else f"{resource.capitalize()}: {amount}g")

def check_resource_sufficiency(drink):
    for resource, amount in MENU[drink].items():
        if resource != 'cost' and resources[resource] < amount:
            print(f"Sorry, there is not enough {resource} to make {drink}.")
            return False
    return True

def process_coins(drink):
    print(f"The cost of {drink} is ${MENU[drink]['cost']:.2f}.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    return total

def check_transaction_success(drink, inserted_amount):
    cost = MENU[drink]['cost']
    if inserted_amount < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif inserted_amount > cost:
        change = round(inserted_amount - cost, 2)
        print(f"Here is ${change:.2f} dollars in change.")
        resources['money'] += cost
    else:
        resources['money'] += cost
    return True

def make_coffee(drink):
    for resource, amount in MENU[drink].items():
        if resource != 'cost':
            resources[resource] -= amount
    print(f"Here is your {drink}. Enjoy!")

while True:
    action = input("What would you like? (espresso/latte/cappuccino): ")
    action = action.lower()

    if action == "report":
        print_report()
    elif action == "off":
        print("Turning off the coffee machine.")
        break
    elif action in MENU:
        if check_resource_sufficiency(action):
            inserted_amount = process_coins(action)
            if check_transaction_success(action, inserted_amount):
                make_coffee(action)
    else:
        print("Sorry, we don't have that option. Please try again.")
