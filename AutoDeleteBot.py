import discord
from discord.ext import commands
import re

client = commands.Bot(command_prefix = "") 
@client.event
async def on_ready():
    print('Its working')

@client.event
async def on_message(message):
    channel = client.get_channel(ChannelID)
    if message.author.id == AuthorID:
        await channel.send('You are not allowed to send a message :)')
        await message.delete()
           
client.run('Token')
