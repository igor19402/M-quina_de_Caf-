# -------------------FIRST PART--------------------------------------
# Write your code here
# print("""
# Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!
# """)

# -------------------SECOND PART--------------------------------------
# print("Write how many cups of coffee you will need:")
# qtd_cups = int(input())
# qtd_water = qtd_cups * 200
# qtd_milk = qtd_cups * 50
# qtd_beans = qtd_cups * 15
# print(f"For {qtd_cups} cups of coffee you will need:")
# print(f"{qtd_water} ml of water")
# print(f"{qtd_milk} ml of milk")
# print(f"{qtd_beans} g of coffee beans")

# -------------------THIRD PART--------------------------------------
# qtd_water_cup = 200
# qtd_milk_cup = 50
# qtd_beans_cup = 15
# print("Write how many ml of water the coffee machine has:")
# qtd_water_machine = int(input())
# print("Write how many ml of milk the coffee machine has:")
# qtd_milk_machine = int(input())
# print("Write how many grams of coffee beans the coffee machine has:")
# qtd_beans_machine = int(input())
# print("Write how many cups of coffee you will need:")
# qtd_cup = int(input())
#
# reason_water = qtd_water_machine // qtd_water_cup
# reason_milk = qtd_milk_machine // qtd_milk_cup
# reason_beans = qtd_beans_machine // qtd_beans_cup
#
# qtd_cup_done = min(reason_water, reason_milk, reason_beans)
#
# if qtd_cup == qtd_cup_done:
#     print("Yes, I can make that amount of coffee")
# elif qtd_cup_done > qtd_cup:
#     print("Yes, I can make that amount of coffee (and even {} more than that)".format(qtd_cup_done - qtd_cup))
# elif qtd_cup_done < qtd_cup:
#     print("No, I can make only {} cups of coffee".format(qtd_cup_done))


# -------------------FOURTH PART--------------------------------------
initial_water = 400
initial_milk = 540
initial_coffee_beans = 120
initial_disposable_cups = 9
initial_money = 550

qtd_water_espresso = 250
qtd_beans_espresso = 16
price_espresso = 4

qtd_water_latte = 350
qtd_milk_latte = 75
qtd_beans_latte = 20
price_latte = 7

qtd_water_cappuccino = 200
qtd_milk_cappuccino = 100
qtd_beans_cappuccino = 12
price_cappuccino = 6


def remaining(water, milk, coffee_beans, cups, money):
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")


while True:
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        option_buy = input()
        if option_buy == "back":
            continue
        if option_buy == "1":
            reason_water = qtd_water_espresso / initial_water
            reason_beans = qtd_beans_espresso / initial_coffee_beans
            if reason_water > 1:
                print("Sorry, not enough water!")
            elif reason_beans > 1:
                print("Sorry, not enough coffee beans")
            elif initial_disposable_cups < 1:
                print("Sorry, not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                initial_water -= qtd_water_espresso
                initial_coffee_beans -= qtd_beans_espresso
                initial_money += price_espresso
                initial_disposable_cups -= 1
        elif option_buy == "2":
            reason_water = qtd_water_latte / initial_water
            reason_beans = qtd_beans_latte / initial_coffee_beans
            reason_milk = qtd_milk_latte / initial_milk
            if reason_water > 1:
                print("Sorry, not enough water!")
            elif reason_beans > 1:
                print("Sorry, not enough coffee beans")
            elif reason_milk > 1:
                print("Sorry, not enough milk")
            elif initial_disposable_cups < 1:
                print("Sorry, not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                initial_coffee_beans -= qtd_beans_latte
                initial_water -= qtd_water_latte
                initial_milk -= qtd_milk_latte
                initial_money += price_latte
                initial_disposable_cups -= 1
        elif option_buy == "3":
            reason_water = qtd_water_cappuccino / initial_water
            reason_beans = qtd_beans_cappuccino / initial_coffee_beans
            reason_milk = qtd_milk_cappuccino / initial_milk
            if reason_water > 1:
                print("Sorry, not enough water!")
            elif reason_beans > 1:
                print("Sorry, not enough coffee beans")
            elif reason_milk > 1:
                print("Sorry, not enough milk")
            elif initial_disposable_cups < 1:
                print("Sorry, not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                initial_disposable_cups -= 1
                initial_water -= qtd_water_cappuccino
                initial_coffee_beans -= qtd_beans_cappuccino
                initial_milk -= qtd_milk_cappuccino
                initial_money += price_cappuccino
    elif action == "fill":
        print("Write how many ml of water you want to add:")
        fill_water = int(input())
        initial_water += fill_water
        print("Write how many ml of milk you want to add:")
        fill_milk = int(input())
        initial_milk += fill_milk
        print("Write how many grams of coffee beans you want to add:")
        fill_coffee_beans = int(input())
        initial_coffee_beans += fill_coffee_beans
        print("Write how many disposable coffee cups you want to add:")
        fill_disposable_cups = int(input())
        initial_disposable_cups += fill_disposable_cups
    elif action == "take":
        print(f"I gave you ${initial_money}")
        initial_money -= initial_money
    elif action == "remaining":
        remaining(initial_water, initial_milk, initial_coffee_beans, initial_disposable_cups, initial_money)
    elif action == "exit":
        break






