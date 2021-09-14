import discord
from datetime import datetime
from config.db import cursor, connection
import asyncio

async def listCommand(message, argv, client):
    if len(argv) < 3:
        await message.channel.send("Not enough arguments : expected `&el list` `gs` / `name` / `class`")
        return -1
    if len(argv) > 3:
        await message.channel.send("Too many arguments : expected `&el list` `gs` / `name` / `class`")
        return -1

    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(message.content) + "> : List command")
    if argv[2] == 'gs' :
        cursor.execute("SELECT name, u_class, u_level, u_gear FROM user ORDER BY u_gear DESC")
    if argv[2] == 'name' :
        cursor.execute("SELECT name, u_class, u_level, u_gear FROM user ORDER BY name ASC")
    if argv[2] == 'class' :
        cursor.execute("SELECT name, u_class, u_level, u_gear FROM user ORDER BY u_class ASC")
    fetched_values = cursor.fetchall()
    fetched_values.insert(0, ["name", "class", "level", "gs"])
    column_sizes= [0] * len(fetched_values[0])
    for i in range(len(fetched_values)):
        for j in range(len(column_sizes)):
            column_sizes[j] = max(column_sizes[j], len(str(fetched_values[i][j])))
    msgStr = "```"
    # first line
    for j in range(len(fetched_values[0])):
        msgStr += str(fetched_values[0][j])
        for k in range(column_sizes[j] - len(str(fetched_values[0][j]))):
            msgStr += " "
        msgStr += "\n" if j == len(fetched_values[0]) - 1 else " - "
    msgStr += "\n"

    fetched_values.pop(0)
    for i in range(len(fetched_values)):
        for j in range(len(fetched_values[i])):
            msgStr += str(fetched_values[i][j])
            for k in range(column_sizes[j] - len(str(fetched_values[i][j]))):
                msgStr += " "
            msgStr += "\n" if j == len(fetched_values[i]) - 1 else " - "
    msgStr += "```"
    embed = discord.Embed(title="", description="", color=0x1D068F)
    embed.set_author(name="List by GS", icon_url=client.user.avatar_url)
    embed.add_field(name="\u200B", value=msgStr, inline=False)
    await message.channel.send(embed = embed)
    return 0


