from config.db import cursor, connection

update = {
    'name' : 'name',
    'gs' : 'u_gear',
    'lvl' : 'u_level',
    'sp' : 'u_skill',
    'red' : 'r_red',
    'orange' : 'r_orange',
    'yellow' : 'r_yellow',
    'blue' : 'r_blue',
    'green' : 'r_green',
    'purple' : 'r_purple'
}

async def updateCommand(message, argv, client):
    if len(argv) < 4:
        await message.channel.send("Not enough arguments : expected `&el update [gs, sp] value`")
        return -1
    if len(argv) > 4:
        await message.channel.send("Too many arguments : expected `&el update [gs, sp] value`")
        return -1
    for key, value in update.items() :
        if argv[2] == key :
            attribute = update[key]
            updated_value = argv[3]
            if key == 'name':
                cursor.execute("UPDATE user SET " + str(attribute) + " = '" + str(updated_value) + "' WHERE uuid = '" + str(message.author.id) + "';")
            else:
                tmp = updated_value
                try :
                    updated_value = int(updated_value)
                except ValueError :
                    await message.channel.send("Wrong input type, number expected.")
                    return -1
                cursor.execute("UPDATE user SET " + str(attribute) + " = " + str(updated_value) + " WHERE uuid = '" + str(message.author.id) + "';")
                connection.commit()
            return 0
    await message.channel.send("Wrong keyword")
    print("Update command")
    return 0
