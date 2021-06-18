import os
from dotenv import load_dotenv
from list_time import python_functions
import discord
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

def random_function():
    return random.choice(python_functions)

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content == "python":
        response = random_function()
        await message.channel.send(response)

client.run(TOKEN)
