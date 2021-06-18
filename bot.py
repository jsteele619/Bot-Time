import os
from dotenv import load_dotenv
import discord
import random

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.guilds}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content == "python":
        response = "random quote"
        await message.channel.send('Hello World!')

client.run(TOKEN)