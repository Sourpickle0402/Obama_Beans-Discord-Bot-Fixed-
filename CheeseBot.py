import discord
from discord.ext import commands
import random
import time

Cheeses = [
    discord.File(r"FileAddress"),
    discord.File(r"FileAddress"),
    discord.File(r"FileAddress"),
    discord.File(r"FileAddress"),
    discord.File(r"FileAddress"),   
]

CheeseFacts = [
    'The first cheese was made in 1615BC, roughly 3600 years ago in China',
    'Cheese started getting industrially produced in 1815 in Switzerland',
    'r/cheese is an actual, popular subreddit',
    'Cheese is a loaf of milk',
    'Do not consume cheese if lactose intolerant',
]

client = commands.Bot(command_prefix = "c.")
@client.event
async def on_ready():
    print('Its working')

@client.event
async def on_message(message):
    if "https://discord.gg/" in message.content:
        await message.delete()

@client.command()
async def cheesefact(message):
    MessageLocation = message.channel.id
    channel = client.get_channel(MessageLocation)
    await channel.send('Here is a random cheese fact:')
    RNGFACT = random.randint(0, 4)
    await channel.send(CheeseFacts[RNGFACT])

@client.command() #I'm putting this command here to inform the users what commands are available to them
async def commands(message):
    MessageLocation = message.channel.id
    channel = client.get_channel(MessageLocation)
    await channel.send(r'my prefix is c. I have a lot of commands, being updated daily! First is cheese, it sends a picture of cheese. Next up is rollthecheese, it sends a random picture of cheese. We also have Cheesefact, which tells you a random fact about cheese. We also have a secret command ;)')

@client.command()
async def rollthecheese(message):
    MessageLocation = message.channel.id
    channel = client.get_channel(MessageLocation)
    await channel.send('You are about to roll the cheese')
    RNG = random.randint(0, 4)
    await channel.send(file=Cheeses[RNG])

@client.command()
async def whatischeese(message):
    MessageLocation = message.channel.id
    channel = client.get_channel(MessageLocation)
    await channel.send('cheese')

client.run('Token')
