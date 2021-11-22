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
daily_gains = 0
def reduc(drink):
    resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
#   resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
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
def payment():
    print("Payment: ")
    quarters = float(input("Quarters = "))
    dimes = float(input("Dimes = "))
    nickles = float(input("Nickles = "))
    payment.price = float(0.25* quarters + 0.1 * dimes + 0.01 * nickles)
    print(f"Amount paid = ${payment.price}")
    return payment.price

end = False
while end is False:
    option = input("\n\nSelect an option\nWhat would you like? \n1.Expresso\n2.Latte \n3.Cappuccino\n")
    option = option.lower() 
    
    if option == '1':
        payment()
        if MENU["espresso"]["cost"] > payment.price:
            print("Insufficient fund, deposit $", MENU["espresso"]["cost"] - payment.price,"more.")
        else:
            print("Dispensing $", payment.price - MENU["espresso"]["cost"]," as change.")
            daily_gains = daily_gains + payment.price
            expresso()

    elif option == '2':
        payment()
        if MENU["latte"]["cost"] > payment.price and MENU["espresso"]["cost"] < payment.price :
            print("Insufficient fund, deposit $", MENU["latte"]["cost"] - payment.price,"more or try buying espresso.")
        elif MENU["latte"]["cost"] > payment.price:
            print("Insufficient fund, deposit $", MENU["latte"]["cost"] - payment.price,"more.")
        
        else:
            print("Dispensing $"+ payment.price - MENU["latte"]["cost"]," as change.")
            daily_gains = daily_gains + payment.price
            latte()

    elif option == '3':
        payment()
        if MENU["cappuccino"]["cost"] > payment.price and MENU["latte"]["cost"] < payment.price :
            print("Insufficient fund, deposit $", MENU["cappuccino"]["cost"] - payment.price,"more but you can afford latte or espresso.")
        elif MENU["cappuccino"]["cost"] > payment.price and MENU["expresso"]["cost"] < payment.price :
            print("Insufficient fund, deposit $", MENU["cappuccino"]["cost"] - payment.price,"more but you can afford espresso.")
        elif MENU["cappuccino"]["cost"] > payment.price:
            print("Insufficient fund, deposit $", MENU["cappuccino"]["cost"] - payment.price,"more.")
        else:
            print("Dispensing $", payment.price - MENU["cappuccino"]["cost"]," as change.")
            daily_gains = daily_gains + payment.price
            cappuccino()
    
    elif option == 'report':
        print(f"Profit for the day = ${daily_gains} ")
        print(resources)
    elif option == 'off':
        end = True
        print(f"Profit for the day = ${daily_gains} ")
        print(resources)
        print("Machine Shutdown ")
        quit()
    else:
        print("Command not recognized.")
        quit()


