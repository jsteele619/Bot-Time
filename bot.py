import os
from dotenv import load_dotenv
import discord
import random

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content == "python":
        response = "random quote"
        await message.channel.send('Hello World!')

client.run(TOKEN)