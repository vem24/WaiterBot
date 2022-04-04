# Waiter bot will type 
# today's menu and ask for your order

# Import the time module for delays
import time

# Refactor repetative print and time.sleep() code
def print_pause(string):
    print_pause(str(string))
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
            print_pause("Waffles it is!")
            break
        elif "pancakes" in response:
            print_pause("Pancakes it is!")
            break
        else:
            print_pause("Sorry, I don't understand.")
    # Let cusomer know their order will be ready soon.            
    print_pause("Your order will be ready shortly.")
   
    while True:
        order_again = input("Would you like to place another order? "
                            "Please say 'yes' or 'no'.\n").lower()
        if "no" in order_again:
            print_pause("OK, goodbye!")
            break
        elif "yes" in order_again:
            print_pause("Very good, I'm happy to take another order.")
            break
        else:
            print_pause("Sorry, I don't understand.")
        
    if "no" in order_again:
        break