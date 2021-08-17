from config.db import cursor, connection

async def addCommand(message, argv, client):
    cursor.execute("SELECT uuid FROM user WHERE uuid = '" + str(message.author.id) + "';")
    result = cursor.fetchone()
    print("Add command")

    if result is None :
        cursor.execute("INSERT INTO user (uuid,name, u_gear, u_level, u_skill, r_red, r_orange, r_yellow, r_blue, r_green, r_purple) VALUES ('" + str(message.author.id) + "','greg', 1, 2, 3, 4, 5, 6, 7, 8, 9);")
        connection.commit()
        await message.channel.send("User successfully registered")
        # return 0
    else :
        await message.channel.send("User registration failed : already registered")
        # return -1
