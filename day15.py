#!/usr/bin/env python3

logo = """COFFEE MACHINE"""


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

def reduc(drink):
    resources["water"] = resources["water"] - MENU[drink]["ingredents"]["water"]
    resources["milk"] = resources["milk"] - MENU[drink]["ingredents"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[drink]["ingredents"]["coffee"]
    return resources

print(logo)
def expresso():
    if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
        print("Insufficient Water")
    elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient Coffee")
    elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"] and MENU["espresso"]["ingredients"]["water"] > resources["water"]:
        print("Insufficient water and coffee")
    else:
        reduc("espresso")
        print("Just a second")
        print("Here is your espresso, Enjoy!")
 
 
def latte():
    if MENU["latte"]["ingredients"]["water"] > resources["water"]:
        print("Insufficient Water")
    elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient Coffee")
    elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
        print("Insufficient milk")
    else:
        reduc("latte")
        print("Just a second")
        print("Here is your latte, Enjoy!")


def cappuccino():
    if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
        print("Insufficient Water")
    elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient Coffee")
    elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
        print("Insufficient milk")
    else:
        reduc("cappuccino")
        print("Just a second")
        print("Here is your cappuccino, Enjoy!")


while option is not "off":
    option = input("Select an option\nWhat would you like? \n1.Expresso\n2.Latte \n3.Cappuccino\n")
    option = option.lower() 
    print("payment = ")
    quarters = input(" Quarters = ")
    dimes = input(" Dimes = ")
    nickles = input(" Nickles = ")
    price = (0.25* quarters + 0.1 * dimes + 0.01 * nickles)
    print(f"Amount paid = ${price}")
    if option == '1':
        if MENU["espresso"]["cost"] > price:
            print("Insufficient fund, deposit $"+ MENU["espresso"]["cost"] - price,"more.")
        else:
            expresso()
    elif option == '2':
        if MENU["latte"]["cost"] > price:
            print("Insufficient fund, deposit $"+ MENU["latte"]["cost"] - price,"more.")
        elif MENU["latte"]["cost"] > price and MENU["espresso"]["cost"] < price :
            print("Insufficient fund, deposit $"+ MENU["latte"]["cost"] - price,"more or try buying espresso.")
        else:
            latte()
    elif option == '3':
        if MENU["cappuccino"]["cost"] > price:
            print("Insufficient fund, deposit $"+ MENU["cappuccino"]["cost"] - price,"more.")
        elif MENU["cappuccino"]["cost"] > price and MENU["latte"]["cost"] < price :
            print("Insufficient fund, deposit $"+ MENU["cappuccino"]["cost"] - price,"more but you can afford latte or espresso.")
        elif MENU["cappuccino"]["cost"] > price and MENU["expresso"]["cost"] < price :
            print("Insufficient fund, deposit $"+ MENU["cappuccino"]["cost"] - price,"more but you can afford espresso.")
        cappuccino()
    elif option == 'report':
        print(resources)
    elif option == 'off':
        print("Machine Shutdown ")
        quit()
    else:
        print("Command not recognized.")
        quit()


