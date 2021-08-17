import discord
from config.db import cursor, connection

client = discord.Client()

async def helpCommand(message, argv, client):
    embed = discord.Embed(title="Help", description="Helping page", color=0x1D068F)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(name="&el help", value="shows this message", inline=False)
    embed.add_field(name="&el add", value="Creates a new user and will ask you all your information concerning your character", inline=False)
    embed.add_field(name="&el update [field] [value]", value="Updating one of your informations value", inline=False)
    embed.add_field(name="&el list", value="shows a list of all users and their informations", inline=False)
    embed.add_field(name="&el info", value="shows your informations only.", inline=False)
    embed.add_field(name="&el delete me", value="Removes your personnal information", inline=False)
    embed.add_field(name="&el delete [ID]", value="removes a user from the bot and database, *only available for admins*", inline=False)
    await message.channel.send(embed=embed)

    return
