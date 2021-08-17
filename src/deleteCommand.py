from config.db import cursor, connection

async def deleteCommand(message, argv, client):
    print("Delete command")

    
    if len(argv) < 3:
        await message.channel.send("Not enough arguments : expected `&el delete id`")
        return -1
    if len(argv) > 3:
        await message.channel.send("Too many arguments : expected `&el delete id`")
        return -1

    if argv[2] == 'me' :
        id = str(message.author.id)
    else:
        id = argv[2]

    cursor.execute("SELECT uuid FROM user WHERE uuid = '" + id + "';")
    result = cursor.fetchone()

    if result is None :
        await message.channel.send("No user registered")
        return -1
    else :
        cursor.execute("DELETE FROM user WHERE uuid = '" + id + "';")
        connection.commit()
        await message.channel.send("User deleted")
        return 0
