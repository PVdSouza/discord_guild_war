from . import building
import pickle, os

class Guild:
    def __init__(self, name, owner):
        self.owner = owner# guild owner discord ID
        self.name  = name # guild name

        self.money = 500  # starting money
        self.stone = 1500 # starting stone
        self.iron  = 500  # starting iron
        self.wood  = 1500 # starting wood

        self.hall = building.Building("hall")
        self.mine = building.Building("mine")
        self.quarry = building.Building("quarry")
        self.cabin = building.Building("cabin")

    # getter and setter section  
    def get_wood(self) -> int:
        return self.wood

    def set_wood(self, wood: int):
        self.wood = wood

    def get_stone(self) -> int:
        return self.stone

    def set_stone(self, stone: int):
        self.stone = stone

    def get_iron(self) -> int:
        return self.iron

    def set_iron(self, iron: int):
        self.iron = iron

    def get_money(self) -> int:
        return self.money

    def set_money(self, money: int):
        self.money = money   

    def is_owner(self, id):
        return (self.owner == id)     

    def level_up(self, building):
        resource_cost = building.get_cost()
        if ((self.wood >= resource_cost[0]) and (self.stone>= resource_cost[1]) and
            (self.iron >= resource_cost[2])):
            self.wood -= resource_cost[0]
            self.stone -=resource_cost[1]
            self.iron -= resource_cost[2]
            building.level_up()
            return "Leveled up successfully!"
        else:
            return "Not enough materials! :("

    # data persistance

    def save(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(THIS_FOLDER, 'live_guilds' ,self.name)
        with open(file_name, 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        
    def load(name):
        file_name = '/Documents/projects/discord_bot/live_guilds/' + name
        with open(file_name, 'rb') as input:
            return pickle.load(input)
