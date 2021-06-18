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
    print('hello world')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if 'python' in message.content:
        response = random_function()
        await message.channel.send(f"Your random python function --> {response}" )

client.run(TOKEN)

