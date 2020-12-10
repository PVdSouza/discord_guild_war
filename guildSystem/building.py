class Building:
    def __init__(self, type):
        if type == "hall":
            self.wood_cost = 150
            self.stone_cost= 100
            self.iron_cost = 0
            self.level = 1

        if type == "mine":
            self.wood_cost = 75
            self.stone_cost= 75
            self.iron_cost = 0
            self.level = 1

        if type == "quarry":
            self.wood_cost = 75
            self.stone_cost= 100
            self.iron_cost = 0
            self.level = 1

        if type == "cabin":
            self.wood_cost = 150
            self.stone_cost= 50
            self.iron_cost = 0
            self.level = 1
    
    def get_cost(self): 
        return (self.wood_cost*self.level, self.stone_cost*self.level, self.iron_cost*self.level)
    
    def get_level(self):
        return self.level

    def get_resource(self):
        return self.level*2

    def level_up(self):
        self.level += 1