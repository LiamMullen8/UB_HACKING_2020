import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from CARDS import *

load_dotenv()
TOKEN = 'NzY5NTkxMTQ5Nzg1NTE0MDQ0.X5RPnA.9ehvy7B9UMJ7xd0sLnd4tPFqWy8'
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="+")


#### shell verification ####
@bot.event
async def on_ready():

    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!')

    print(f'{member} has joined a server.')


@bot.event
async def on_member_remove(ctx, member):
    await ctx.send(f'{member} has left a server.')
		


######################## COMMANDS ######################
#sanity check#
@bot.command()
async def ping(ctx):
    await ctx.send(f'```Pong! {round(bot.latency) * 1000}ms```')
##


@bot.command(aliases=['cum'])
async def butt_nut(ctx):
	await ctx.send(
		f'```Cum is the answer```')
	await ctx.send(f'```Poo is the answer```')
		
		
@bot.command(aliases=['RAGEQUIT'])
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)				



#the game

@bot.command(aliases=["newgame"])
async def _new_game(ctx):
  await ctx.send(resetCards(botCards(), playerCards()))
	
@bot.command(aliases=["flip"])
async def _flip(ctx):
  await ctx.send(flip())

@bot.command(aliases=["check"])
async def _check(ctx):
  await ctx.send(check())
	

###


bot.run(TOKEN)
####################################################################



