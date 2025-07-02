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
money=56
resources = {
    "water": 300,
    "milk": 200,
    "coffee":100}


def check_resources(user_choice):
    if resources['water']>=MENU[user_choice]['ingredients']['water'] and \
            resources['coffee']>=MENU[user_choice]['ingredients']['coffee'] and \
            resources['milk'] >= MENU[user_choice]["ingredients"].get("milk", 0):

        return True
    elif resources['water'] < MENU[user_choice]['ingredients']['water']:
        print('SORRY!! NOT ENOUGH WATER.')


    elif resources['coffee'] < MENU[user_choice]['ingredients']['coffee']:
        print("SORRY!! Not enough coffee.")
    elif resources['milk'] < MENU[user_choice]['ingredients'].get('milk', 0):
        print("SORRY!! Not enough milk.")


def check_money(user_choice):
    global money,total

    print("Please insert coins.")
    quarters = int(input("How many quarters? "))  # $0.25
    dimes = int(input("How many dimes? "))  # $0.10
    nickels = int(input("How many nickels? "))  # $0.05
    pennies = int(input("How many pennies? "))
    total= quarters*0.25+ dimes*0.10+ nickels*0.05+ pennies*0.01
    print(total)
    change = total - MENU[user_choice]["cost"]


    if total< MENU[user_choice]["cost"]:
        print("SORRY!! YOU DON'T HAVE ENOUGH MONEY. MONEY INSERTED WILL BE RETURNED.")
        return
    else:
        if change>0:
            print(f"Here is your change of {change} rs.")

        money += total
        resources["water"] -= MENU[user_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
        resources["milk"] -= MENU[user_choice]["ingredients"].get("milk",0)
        print(f"Here is your {user_choice}. Enjoy! ☕")
        return



is_working=True
while is_working:

    print(" What would you like? espresso/latte/cappuccino.")
    user_choice = input(" You can also 'off' the machine by typing off and can even ask for report by typing 'report' ").lower()
    if user_choice == "off":
        print("This machine has turned off.")
        is_working = False
    elif user_choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money = ${money}")
    else:
        check_resources(user_choice)
        if check_resources(user_choice)==True:
            check_money(user_choice)


















