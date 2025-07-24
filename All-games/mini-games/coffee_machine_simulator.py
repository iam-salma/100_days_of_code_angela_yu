resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}
espresso = {
    "water": 50,
    "coffee": 18,
    "milk": 0,
    "cost": 1.50
}
latte = {
    "water": 200,
    "coffee": 24,
    "milk": 150,
    "cost": 2.50
}
cappuccino = {
    "water": 250,
    "coffee": 24,
    "milk": 100,
    "cost": 3.00
}


def resource_chk(chose):
    global choose
    for key, value in chose.items():
        if key == "cost":
            resources["money"] += value
            continue
        else:
            resources[key] -= value
            if resources[key] < 0:
                print(f"Sorry, there is not enough {key}.")
                return
    print(f"Here's your {choose} ☕, ENJOY!\u2764\uFE0F")


def amount(ch, p, n, d, q):
    total = p + n + d + q
    if ch["cost"] < total:
        change = total - ch["cost"]
        print(f"Here is ${change} dollars in change")
    if ch["cost"] > total:
        print("Sorry that's not enough money. Money refunded!")
        return
    resource_chk(ch)


def choice_mapping(ch):
    if ch == "espresso":
        ch = espresso
    elif ch == "latte":
        ch = latte
    elif ch == "cappuccino":
        ch = cappuccino
    elif ch == "report":
        for key, value in resources.items():
            print(f"{key}: {value}\n")
        return
    else:
        print(f"{choose}is not on our menu....\nPlease try again...\n")
        return
    return ch


while True:
    choose = input("******* OUR MENU ********\n"
                    "1. Espresso - $1.50\n"
                    "2. Latte - $2.50\n"
                    "3. Cappuccino - $3.00\n"
                    "What would you like to have? : ").lower()

    choice = choice_mapping(choose)

    if choice is not None:
        pen = float(input("please insert the coins :\n"
                          "How many pennies? : ")) * 0.01
        nic = float(input("How many nickels? : ")) * 0.05
        dim = float(input("How many dimes? : ")) * 0.10
        qua = float(input("How many quarters? : ")) * 0.25

        amount(choice, pen, nic, dim, qua)
    print("\n" * 5)
