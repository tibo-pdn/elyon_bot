import os
import discord

from src.split import split_args
from dotenv import load_dotenv

load_dotenv('config/.env')
token = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready !")

@client.event
async def on_message(message):
    if (message.channel.name == 'elyon_bot'):
        message.content = ' '.join(message.content.split())
        argv = message.content.split(' ')
        if argv[0] == '&el':

            await split_args(message, argv)

client.run(token)