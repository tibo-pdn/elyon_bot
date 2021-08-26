import discord

from config.db import cursor, connection

def formatString(string):
    string = str(string)
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.replace("'", "")
    string = string.split(", ")
    for i in range(len(string)):
        if i > 1:
            string[i] = int(string[i])
    return string

async def printMessage(message, array):
    embed = discord.Embed(title = "Stats", description = f"{array[1]}'s Stats.", color = 0x1D068F) #replace message.author by sql name in descritpion
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    embed.set_thumbnail(url = message.author.avatar_url)
    embed.add_field(name = "\u200B", value = "\u200B", inline = False)
    embed.add_field(name = ":trophy: Gearscore<:blank:877523987142438922><:blank:877523987142438922><:blank:877523987142438922>", value = array[2], inline = True)
    embed.add_field(name = ":crossed_swords: level<:blank:877523987142438922><:blank:877523987142438922><:blank:877523987142438922><:blank:877523987142438922>", value = array[3], inline = True)
    embed.add_field(name = ":medal: SP", value = array[4], inline = True)
    embed.add_field(name = "<:red_rune:880086179968581632> Assault", value = array[5], inline = True)
    embed.add_field(name = "<:orange_rune:880086179746291743> Control", value = array[6], inline = True)
    embed.add_field(name = "<:yellow_rune:880086180132184064> Fate", value = array[7], inline = True)
    embed.add_field(name = "<:blue_rune:880086179695976479> Protection", value = array[8], inline = True)
    embed.add_field(name = "<:green_rune:880086179901480970> Support", value = array[9], inline = True)
    embed.add_field(name = "<:purple_rune:880086179951833088> Awakening", value = array[10], inline = True)
    await message.channel.send(embed = embed)
    return 0

async def infoCommand(message, argv, client):
    print("Info command")
    cursor.execute("SELECT uuid FROM user WHERE uuid = '" + str(message.author.id) + "';")
    result = cursor.fetchone()

    if result is None :
        await message.channel.send("No account registered")
        return -1
    else :
        cursor.execute("SELECT uuid, name, u_gear, u_level, u_skill, r_red, r_orange, r_yellow, r_blue, r_green, r_purple FROM user WHERE uuid = '" + str(message.author.id) + "';")
        result2 = formatString(cursor.fetchone())
        print("-->", result2)
        await printMessage(message, result2)
        return 0
