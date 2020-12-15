import json
import os.path
from discord import User
from discord.ext import commands
from guildSystem import guild, building

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
guilds_dict = []


with open('config.json') as json_file:
    config = json.load(json_file)
    bot = commands.Bot(command_prefix=config['prefix'])



#support commands

@bot.command(name='pd')
async def pd(ctx):
    print(guilds_dict)

def load_json():
    guilds_json = open(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', 'guild_map.json'), 'r')
    guilds_dict = json.load(guilds_json)
    guilds_json.close()
    return guilds_dict

async def save_json(g_dict):
    os.remove(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', 'guild_map.json'))
    guilds_json = open(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', 'guild_map.json'), 'w+')
    json.dump(g_dict, guilds_json)
    guilds_json.close()
    
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
    if not os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        name = ' '.join(name)
        new_guild = guild.Guild(name, ctx.author.id)
        new_guild.save()
        guilds_dict[name] = str(ctx.author.id)
        await save_json(guilds_dict)        
        await ctx.send('Nova guilda criada: ' + name)
    else:
        await ctx.send('O usuário já possui uma guilda nesse servidor.')

@bot.command(name='levelup', pass_context=True, aliases=['lu'])
async def level_up_building(ctx, building_name):
    if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        w_guild = guild.Guild.load(str(ctx.author.id))
        await ctx.send(w_guild.level_up(w_guild.get_building(building_name)))
        w_guild.save()
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

@bot.command(name='myguild', pass_context=True, aliases=['mg'])
async def guild_status(ctx):
    if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        w_guild = guild.Guild.load(str(ctx.author.id))
        await ctx.send(w_guild.guild_status())
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

@bot.command(name='deleteguild', pass_context=True, aliases=['delguild'])
async def delete_guild(ctx):
    if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        os.remove(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id)))
        w_guild = guild.Guild.load(str(ctx.author.id))
        del guilds_dict[w_guild.name]
        await save_json(guilds_dict)
        await ctx.send('Guilda removida com sucesso.')
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

# Combat methods

@bot.command(name='attack', pass_contex=True, aliases=['atk'])
async def attack_guild(ctx, *target):
    target = ' '.join(target)
    print(guilds_dict)
    if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', guilds_dict[target])):
            atk_guild = guild.Guild.load(str(ctx.author.id))
            def_guild = guild.Guild.load(guilds_dict[target])
            if (atk_guild.barracks.get_level() > def_guild.wall.get_level()):
                atk_guild.iron += def_guild.iron/2
                def_guild.iron -= def_guild.iron/2

                atk_guild.stone += def_guild.stone/2
                def_guild.stone -= def_guild.stone/2

                atk_guild.wood += def_guild.wood/2
                def_guild.wood -= def_guild.wood/2
                
                atk_guild.save()
                def_guild.save()
                await ctx.send('Vitória!')
        else:
            await ctx.send('A guilda alvo não existe.')
    else:
        await ctx.send('O usuário não possui uma guilda nesse servidor.')


#Run
guilds_dict = load_json()
print(guilds_dict)
json_file = open('config.json')
config = json.load(json_file)
bot.run(config['token'])
json_file.close()