# Waiter bot will type 
# today's menu and ask for your order

# Import the time module for delays
import time

# Refactor repetative print and time.sleep() code
def print_pause(string):
    print(str(string))
    time.sleep(2)

# Bot will introduce themselves
print_pause("Hello! I am Bob, the Breakfast Bot.")
# Bot will type today's menu
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

while True:
    while True:
        response = input("Please place your order. "
                         "Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(2)
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    print("Your order will be ready shortly.")
    time.sleep(2)
    while True:
        order_again = input("Would you like to place another order? "
                            "Please say 'yes' or 'no'.\n").lower()
        if "no" in order_again:
            print("OK, goodbye!")
            time.sleep(2)
            break
        elif "yes" in order_again:
            print("Very good, I'm happy to take another order.")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    if "no" in order_again:
        break