import discord
from discord.ext import commands
import re

Cheese = 'Cheese'
client = commands.Bot(command_prefix = "")
@client.event
async def on_ready():
    print('Its working')

@client.event
async def on_message(message):
    channel = client.get_channel(Token)
    if message.author.id != Token:
        await channel.send(Cheese)
           
client.run('Token')
