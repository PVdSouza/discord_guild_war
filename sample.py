import json
import os.path
from discord import User
from discord.ext import commands
from guildSystem import guild, building

with open('config.json') as json_file:
    config = json.load(json_file)
    bot = commands.Bot(command_prefix=config['prefix'])

#support commands

@bot.command(pass_context=True)
@commands.is_owner()
async def getid(ctx, user: User):
    await ctx.send("Id do usuário: {}".format(user.id))

#info commands
@bot.command(name='devinfo')
async def dev_info(ctx):
    await ctx.send('Todos os links relevantes em: https://linktr.ee/pedrodsz')

@bot.command(name='guildinfo')
async def guild_info(ctx):
    await ctx.send('Você pode criar uma guilda usando o comando ```$createguild <name>```')


#guild commands

@bot.command(name='createguild', pass_context=True)
async def create_guild(ctx, *name):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        name = ' '.join(name)
        new_guild = guild.Guild(name, ctx.author.id)
        new_guild.save()
        await ctx.send('Nova guilda criada: ' + name)
    else:
        await ctx.send('O usuário já possui uma guilda nesse servidor.')

@bot.command(name='levelup', pass_context=True)
async def level_up_building(ctx, building_name):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        w_guild = guild.Guild.load(str(ctx.author.id))
        await ctx.send(w_guild.level_up(w_guild.get_building(building_name)))
        w_guild.save()
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

@bot.command(name='myguild', pass_context=True)
async def guild_status(ctx):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        w_guild = guild.Guild.load(str(ctx.author.id))
        await ctx.send(w_guild.guild_status())
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

@bot.command(name='deleteguild', pass_context=True)
async def guild_status(ctx):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id))):
        os.remove(os.path.join(THIS_FOLDER, 'guildSystem', 'live_guilds', str(ctx.author.id)))
        await ctx.send('Guilda removida com sucesso.')
    else:
        await ctx.send('O usuário não possui guilda nesse servidor.')

#Run
with open('config.json') as json_file:
    config = json.load(json_file)
    bot.run(config['token'])

