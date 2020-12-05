import discord
from discord.ext import commands
from guildSystem import guild, building

bot = commands.Bot(command_prefix='$')


@bot.command(name='guildinfo')
async def guild_info(ctx):
    await ctx.send('You can create your guild by using ```$createguild <name>```')

@bot.command(name='createguild')
async def create_guild(ctx, name):
    new_guild = guild.Guild(name, ctx.author.id)
    new_guild.save()
    await ctx.send('Created guild: ' + name)

@bot.command(name='levelup')
async def level_up(ctx, building):
    


bot.run('NzY3ODYwMTE5MjQ5MDkyNjM4.X44Ddg.24yEBav5xKcOeAraqXckj1n_tXo')