from config.db import cursor, connection

async def infoCommand(message, array):
    print("Info command")
    cursor.execute("SELECT uuid FROM user WHERE uuid = '" + str(message.author.id) + "';")
    result = cursor.fetchone()

    if result is None :
        await message.channel.send("No account registered")
        return -1
    else :
        cursor.execute("SELECT uuid, u_gear, u_level, u_skill, r_red, r_orange, r_yellow, r_blue, r_green, r_purple FROM user WHERE uuid = '" + str(message.author.id) + "';")
        result2 = cursor.fetchone()
        print(result2)
        return 0