#Import the Computer class
from computer import *

class ResaleShop:
    """
    Has an inventory list of Computers and can add/remove items or print the inventory
    """

    """
    inventory is a list of Computer objects belonging to the shop
    """
    inventory: list

    """
    Constructor makes a shop with an empty inventory
    """
    def __init__(self):
        self.inventory = []
    
    """
    Takes in a Computer object and adds it to the inventory
    """
    def buy(self, computer: Computer):
        self.inventory.append(computer)
    
    """
    Takes in an item_id, removes item from inventory if it was there, prints error 
    message otherwise 
    """
    def sell(self, item_id: int):
        if 0 <= item_id and item_id < len(self.inventory):
            self.inventory.pop(item_id)
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    Prints information about all items in inventory, or prints error message if inventory
    is empty
    """
    def print_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print("Item ID:", self.inventory.index(item), ":", item.get_info())
        else:
            print("No inventory to display.")

