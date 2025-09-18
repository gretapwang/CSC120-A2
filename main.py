# Import a few useful containers from the typing module
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

# Import object oriented code
from computer import *
from oo_resale_shop import *

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():
    
    # First, let's make a computer
    computer = create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")


"""
Tests object oriented code
"""
def test():

    # Create a resale shop
    shop = ResaleShop()
    shop.print_inventory()

    # Buy two computers
    print("Buying 2 computers:")
    shop.buy("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    computer_id: int = shop.buy("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    shop.print_inventory()

    # Test updating price
    print("Updating price of item 1:")
    shop.update_price(computer_id, 1700)
    shop.print_inventory()

    # Test refurbishing
    print("Refurbishing item 1:")
    shop.refurbish(computer_id, "MacOS Monterey")
    shop.print_inventory()

    # Test selling
    print("Selling item 1:")
    shop.sell(computer_id)
    shop.print_inventory()

    # Test error messages
    print("Error messages:")
    shop.update_price(3, 1000)
    shop.sell(3)
    shop.refurbish(3)




# Calls the main() function when this file is run
if __name__ == "__main__": 
    test_mode: bool = True
    if test_mode:
        test()
    else:
        main()
