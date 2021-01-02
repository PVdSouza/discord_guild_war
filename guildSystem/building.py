
BUILDINGS_TYPES = ['hall', 'mine', 'quarry', 'cabin']
STARTER_BUILDINGS = {
    'hall': {
        'type': 'hall',
        'level': 1,
        'production_rate': 2,
        'wood_cost': 150,
        'stone_cost': 100,
        'iron_cost': 0
    },
    "mine": {
        'type': 'mine',
        'level': 1,
        'production_rate': 2,
        'wood_cost': 75,
        'stone_cost': 75,
        'iron_cost': 0
    },
    "quarry": {
        'type': 'quarry',
        'level': 1,
        'production_rate': 2,
        'wood_cost': 75,
        'stone_cost': 100,
        'iron_cost': 0
    },
    "cabin": {
        'type': 'cabin',
        'level': 1,
        'production_rate': 2,
        'wood_cost': 150,
        'stone_cost': 50,
        'iron_cost': 0
    }
}

def create_building(type):
    if type in BUILDINGS_TYPES:
        return STARTER_BUILDINGS[type]
    print('Failed to create building for type: '+ str(type)) # its a point to throw a exception if necessary

def cost_function(type, level): # i keep the original cost function
    building = STARTER_BUILDINGS[type]
    return {
        'wood_cost':  building['wood_cost']  * level,
        'stone_cost': building['stone_cost'] * level,
        'iron_cost':  building['iron_cost']  * level,
    }

# i make 2 functions to update level, choose one (i like the first):
def level_up(building):
    building['level'] += 1
    building['production_rate'] += 2

    new_costs = cost_function(building['type'], building['level'])
    building['wood_cost']  = new_costs['wood_cost']
    building['stone_cost'] = new_costs['stone_cost']
    building['iron_cost']  = new_costs['iron_cost']

def level_up_copy(building):
    new_costs = cost_function(building['type'], building['level'] + 1)
    return {
        'type': building['type'],
        'level': building['level'] + 1,
        'production_rate': building['production_rate'] + 2,
        'wood_cost': new_costs['wood_cost'],
        'stone_cost': new_costs['stone_cost'],
        'iron_cost': new_costs['iron_cost']
    }