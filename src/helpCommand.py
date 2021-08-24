import discord
from config.db import cursor, connection

client = discord.Client()

async def helpCommand(message, argv, client):
    embed = discord.Embed(title="Help", description="Helping page", color=0x1D068F)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(name=":white_small_square:&el help", value=":heavy_minus_sign:shows this message", inline=False)
    embed.add_field(name=":white_small_square:&el add", value=":heavy_minus_sign:Creates a new user and will ask you all your information concerning your character", inline=False)
    embed.add_field(name=":white_small_square:&el update [field] [value]", value=":heavy_minus_sign:Updating one of your informations value", inline=False)
    embed.add_field(name=":white_small_square:&el list", value=":heavy_minus_sign:shows a list of all users and their informations", inline=False)
    embed.add_field(name=":white_small_square:&el info", value=":heavy_minus_sign:shows your informations only.", inline=False)
    embed.add_field(name=":white_small_square:&el delete me", value=":heavy_minus_sign:Removes your personnal information", inline=False)
    embed.add_field(name=":white_small_square:&el delete [ID]", value=":heavy_minus_sign:removes a user from the bot and database, *only available for admins*", inline=False)
    await message.channel.send(embed=embed)

    return
