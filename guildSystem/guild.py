import os
import json
from datetime import datetime

import building as Building

def create_guild(name, owner):
    return {
        'owner': owner,
        'name':  name,
        'money': 500,
        'wood':  1500,
        'stone': 1500,
        'iron':  500,
        'hall':   Building.STARTER_BUILDINGS['hall'],
        'mine':   Building.STARTER_BUILDINGS['mine'],
        'quarry': Building.STARTER_BUILDINGS['quarry'],
        'cabin':  Building.STARTER_BUILDINGS['cabin'],
        'last_updated': datetime.now()
    }

def guild_status_str(guild):
    str_name = guild['name'] + '\n'

    str_money = 'Ouro: '    + str(guild['money'])
    str_wood  = 'Madeira: ' + str(guild['wood'])
    str_stone = 'Pedra: '   + str(guild['stone'])
    str_iron  = 'Ferro: '   + str(guild['iron'])
    str_resources = (
                f'{str_money}' + '\n'
                f'{str_wood}'  + '\n'
                f'{str_stone}' + '\n'
                f'{str_iron}'  + '\n')

    str_hall = 'Nível Castelo: '    + str(guild['hall']['level'])
    str_mine = 'Nível Mina: '       + str(guild['mine']['level'])
    str_quarry = 'Nível Pedreira: ' + str(guild['quarry']['level'])
    str_cabin = 'Nível Cabana: '    + str(guild['cabin']['level'])
    str_buildings = (
                f'{str_hall}'   + '\n'
                f'{str_mine}'   + '\n'
                f'{str_quarry}' + '\n'
                f'{str_cabin}'  + '\n')

    return (
        f'{str_name}'      + '\n'
        f'{str_resources}' + '\n'
        f'{str_buildings}' + '\n')

def level_up_building(guild, building_type):
    if building_type not in Building.BUILDINGS_TYPES:
        return 'Essa guilda não possui uma building desse tipo'

    building = guild[building_type]
    have_wood =  guild['wood']  >= building['wood_cost']
    have_stone = guild['stone'] >= building['stone_cost']  
    have_iron =  guild['iron']  >= building['iron_cost']
    if (have_wood and have_stone and have_iron):
        guild.wood  -= building['wood_cost']
        guild.stone -= building['stone_cost']
        guild.iron  -= building['iron_cost']
        Building.level_up(building_type)
        return 'Nivel aumentado com sucesso!'
    else:
        return 'Recursos insuficientes. :(' # you can return the missing resource here

def time_sync(guild):
    now = datetime.now()
    guild['last_updated'] = now

    idle_time = now - guild['last_updated']
    idle_time = int(idle_time.total_seconds())

    guild['wood']  += idle_time * guild['cabin']['production_rate']
    guild['stone'] += idle_time * guild['quarry']['production_rate']
    guild['iron']  += idle_time * guild['mine']['production_rate']

    save(guild)

def save(guild):
    file_name = 'live_guilds/' + guild['owner'] + '.json'
    with open(file_name, "w+") as write_file:
        json.dump(guild, write_file, indent=4)

def load(owner):
    file_name = 'live_guilds/' + owner + '.json'
    with open(file_name, "r") as read_file:
        guild = json.load(read_file)
    time_sync(guild)
    return guild
    