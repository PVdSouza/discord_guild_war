import json
import os.path

from discord import User
from discord.ext import commands

import guild as Guild
import building as Building

database = load_database()

with open('config.json') as config_file:
    config = json.load(config_file)
bot = commands.Bot(command_prefix=config['prefix'])

#support commands
@bot.command(name='pd')
async def pd(ctx):
    print(database)

def load_database():
    with open('refactored/live_guilds/database.json', 'r') as database_file:
        database = json.load(database_file)
    return database

async def save_database(database):
    with open('refactored/live_guilds/database.json', 'w+') as database_file:
        json.dump(database, database_file, indent=4)
    
@bot.command(pass_context=True)
@commands.is_owner()
async def getid(ctx, user: User):
    await ctx.send("Id do usuário: {}".format(user.id))

#info commands
@bot.command(name='devinfo', aliases=['dinfo'])
async def dev_info(ctx):
    await ctx.send('Todos os links relevantes em: https://linktr.ee/pedrodsz')

@bot.command(name='guildinfo', aliases=['ginfo'])
async def guild_info(ctx):
    await ctx.send('Você pode criar uma guilda usando o comando ```$createguild <name>```')

#guild commands
@bot.command(name='createguild', pass_context=True)
async def create_guild(ctx, *name):
    if os.path.exists('refactored/live_guilds/' + str(ctx.author.id) + '.json'):
        await ctx.send('O usuário já possui uma guilda nesse servidor.')
        return
    
    name = ' '.join(name)
    new_guild = Guild.create_guild(name, ctx.author.id)
    Guild.save(new_guild)
    database['guilds'][name] = str(ctx.author.id)
    await save_database(database)        
    await ctx.send('Nova guilda criada: ' + name)

@bot.command(name='levelup', pass_context=True, aliases=['lu'])
async def level_up_building(ctx, building_name):
    if os.path.exists('refactored/live_guilds/' + str(ctx.author.id) + '.json'):
        guild = Guild.load(str(ctx.author.id))
        message = Guild.level_up_building(guild, building_name)
        Guild.save(guild)
        await ctx.send(message)
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

@bot.command(name='myguild', pass_context=True, aliases=['mg'])
async def guild_status(ctx):
    if os.path.exists('refactored/live_guilds/' + str(ctx.author.id) + '.json'):
        guild = Guild.load(str(ctx.author.id))
        status = Guild.guild_status_str(guild)
        await ctx.send(status)
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

@bot.command(name='deleteguild', pass_context=True, aliases=['delguild'])
async def delete_guild(ctx):
    if os.path.exists('refactored/live_guilds/' + str(ctx.author.id) + '.json'):
        guild = Guild.load(str(ctx.author.id))
        del database['guilds'][guild.name]
        await save_database(database)
        os.remove('refactored/live_guilds/' + str(ctx.author.id) + '.json')
        await ctx.send('Guilda removida com sucesso.')
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

# Combat methods
@bot.command(name='attack', pass_contex=True, aliases=['atk'])
async def attack_guild(ctx, *target):
    target = ' '.join(target)
    if os.path.exists('refactored/live_guilds/' + str(ctx.author.id) + '.json'):
        if os.path.exists('refactored/live_guilds/' + database['guilds'][target] + '.json'):
            attacking_guild = Guild.load(str(ctx.author.id))
            defending_guild = Guild.load(database['guilds'][target])
            if (attacking_guild['barracks']['level'] > defending_guild['wall']['level']): # barracks and walls building types not exists
                # steal wood
                attacking_guild['wood'] += defending_guild['wood']/2
                defending_guild['wood'] -= defending_guild['wood']/2

                # steal stone
                attacking_guild['stone'] += defending_guild['stone']/2
                defending_guild['stone'] -= defending_guild['stone']/2

                # steal iron
                attacking_guild['iron'] += defending_guild['iron']/2
                defending_guild['iron'] -= defending_guild['iron']/2

                # save
                Guild.save(attacking_guild)
                Guild.save(defending_guild)
                await ctx.send('Vitória!')
            else:
                await ctx.send('Seu Ataque falhou.')
        else:
            await ctx.send('A guilda alvo não existe.')
    else:
        await ctx.send('O usuário não possui uma guilda nesse servidor.')


#Run
if __name__ == '__main__':
    print(database)
    print(config)
    bot.run(config['token'])
