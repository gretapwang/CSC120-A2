#Import the Computer class
from computer import *

class ResaleShop:
    """
    Has an inventory list of computers and can add/remove or update items
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
    Takes in information about a computer, adds a Computer object to the inventory, returns item 
    number in inventory
    """
    def buy(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, 
            operating_system: str, year_made: int, price: int) -> int:
        new_computer = Computer(description, processor_type, hard_drive_capacity, 
                                          memory, operating_system, year_made, price)
        self.inventory.append(new_computer)
        return self.inventory.index(new_computer)
    
    """
    Takes in an item_id and new price, calls a Computer method to update price if the item
    is in the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int):
        if 0 <= item_id and item_id < len(self.inventory):
            self.inventory[item_id].update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")

    """
    Takes in an item_id, removes item from inventory if it was there, prints error 
    message otherwise 
    """
    def sell(self, item_id: int):
        if 0 <= item_id and item_id < len(self.inventory):
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    Prints information about all items in inventory, or prints error message if inventory
    is empty
    """
    def print_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print("Item ID:", self.inventory.index(item), ":", {"description": item.description, "processor_type": item.processor_type, "hard_drive_capacity": item.hard_drive_capacity, "memory": item.memory, "operating_system": item.operating_system, "year_made": item.year_made, "price": item.price})
        else:
            print("No inventory to display.")

    """
    Takes in an item_id and new OS, calls Computer method to update price and OS if item 
    is in inventory, prints error message otherwise
    """
    def refurbish(self, item_id: int, new_os: str = ""):
        if 0 <= item_id and item_id < len(self.inventory):
            self.inventory[item_id].refurbish(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
