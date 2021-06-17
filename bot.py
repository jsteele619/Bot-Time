import os
from dotenv import load_dotenv
import discord
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}')

async def on_message(message):
    if message.author == client.user:
        return 

    if message.content == "python":
        response = "random python quote"
        await message.channel.send(response)



client.run(TOKEN)