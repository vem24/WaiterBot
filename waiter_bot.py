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

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            print_pause("Sorry, I don't understand.")

while True:
    response = valid_input("Please place your order. "
                    "Would you like waffles or pancakes?\n", "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
        
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
  
    # Let cusomer know their order will be ready soon.            
    print_pause("Your order will be ready shortly.")
   
    # Ask customer if they'd like to place another order.
    order_again = valid_input("Would you like to place another order? "
                        "Please say 'yes' or 'no'.\n", "no", "yes")
    if "no" in order_again:
        print_pause("OK, goodbye!")
        break
    elif "yes" in order_again:
        print_pause("Very good, I'm happy to take another order.")
    