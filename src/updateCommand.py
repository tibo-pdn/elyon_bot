from config.db import cursor, connection

async def updateCommand(message, argv, client):
    if len(argv) < 4:
        await message.channel.send("Not enough arguments : expected `&el update [gs, sp] value`")
        return -1
    if len(argv) > 4:
        await message.channel.send("Too many arguments : expected `&el update [gs, sp] value`")
        return -1
    print("Update command")
    return 0
