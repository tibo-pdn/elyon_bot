from config.db import cursor, connection

async def listCommand(message, argv):
    print("List command")
    return 0