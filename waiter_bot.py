# Waiter bot will type.
# today's menu and ask for your order.
# Bot will then ask if you'd like to order again.

# Import the time module for delays
import time

# Refactor repetative print and time.sleep() code
def print_pause(string):
    print(string)
    time.sleep(2)

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response

def get_order():
    response = valid_input("Please place your order. Would you like waffles or pancakes?\n", "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")     
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    order_again()

def order_again():
    response = valid_input("Would you like to place another order? Please say 'yes' or 'no'.\n", "no", "yes")

    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()

def order_breakfast():
    intro()
    get_order()

order_breakfast()