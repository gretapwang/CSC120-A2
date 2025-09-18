class Computer:
    """
    Holds details about a computer and can update them
    """

    """
    Attributes are each a piece of information about the computer
    """
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    """
    Constructor takes in information about a computer and assigns it to the attributes
    """
    def __init__(self, details: str, processor: str, capacity: int, mem: int, os: str, year:int, money: int):
        self.description = details
        self.processor_type = processor
        self.hard_drive_capacity = capacity
        self.memory = mem
        self.operating_system = os
        self.year_made = year
        self.price = money

    """
    Takes in a new price, updates the computer's price accordingly
    """
    def update_price(self, new_price: int):
        self.price = new_price

    """
    Takes in a new OS, updates computer's OS accordingly and updates price based on year made
    """
    def refurbish(self, new_os: str = ""):
        if self.year_made < 2000:
            self.price = 0 # too old to sell, donation only
        elif self.year_made < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif self.year_made < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

        if new_os != "":
            self.operating_system = new_os # update details after installing new OS 
    
    """
    Returns a dictionary with all the computer's information, for the resale shop to use when 
    printing inventory
    """
    def get_info(self) -> dict:
        return({"description": self.description, "processor_type": self.processor_type, 
                "hard_drive_capacity": self.hard_drive_capacity, "memory": self.memory, 
                "operating_system": self.operating_system, "year_made": self.year_made, "price": self.price})
