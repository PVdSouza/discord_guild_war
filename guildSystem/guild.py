from datetime import datetime
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

        self.last_loaded = datetime.now()

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

    def get_building(self, building_name):
        if building_name == 'hall':
            return self.hall
        if building_name == 'mine':
            return self.mine
        if building_name == 'quarry':
            return self.quarry
        if building_name == 'cabin':
            return self.cabin

    def guild_status(self):
        str_iron = 'Ferro: '   + str(self.get_iron())
        str_wood = 'Madeira: ' + str(self.get_wood())
        str_stone = 'Pedra: '  + str(self.get_stone())
        str_money = 'Ouro: '   + str(self.get_money())
        str_resources = str_iron + '\n' + str_wood + '\n' + str_stone + '\n' + str_money + '\n\n'

        str_mine = 'Nível Mina: '       + str(self.mine.get_level())
        str_quarry = 'Nível Pedreira: ' + str(self.quarry.get_level())
        str_cabin = 'Nível Cabana: '    + str(self.cabin.get_level())
        str_hall = 'Nível Castelo: '    + str(self.hall.get_level())
        str_buildings = str_mine + '\n' + str_quarry + '\n' + str_cabin + '\n' + str_hall + '\n\n' 

        return(self.name + '\n\n' + str_resources + str_buildings)
    
    def level_up(self, building):
        resource_cost = building.get_cost()
        if ((self.wood >= resource_cost[0]) and (self.stone>= resource_cost[1]) and
            (self.iron >= resource_cost[2])):
            self.wood  -= resource_cost[0]
            self.stone -= resource_cost[1]
            self.iron  -= resource_cost[2]
            building.level_up()
            return "Nivel aumentado com sucesso!"
        else:
            return "Recursos insuficientes. :("

    def time_sync(self):
        idle_time = datetime.now() - self.last_loaded
        self.last_loaded = datetime.now()
        idle_time = idle_time.total_seconds()

        self.wood  += int(idle_time * self.cabin.get_resource())
        self.iron  += int(idle_time * self.mine.get_resource())
        self.stone += int(idle_time * self.quarry.get_resource())
        
    # data persistance
    def save(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(THIS_FOLDER, 'live_guilds', str(self.owner))
        with open(file_name, 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        
    def load(user_id):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(THIS_FOLDER, 'live_guilds', str(user_id))
        with open(file_name, 'rb') as input:
            w_guild = pickle.load(input)
            w_guild.time_sync()    
            return w_guild
