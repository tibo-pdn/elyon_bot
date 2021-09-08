from config.db import cursor, connection
from datetime import datetime
from .addCommand import USERINFOS_LIST

field_alias = {
    'name' : 'name',
    'gs' : 'u_gear',
    'lvl' : 'u_level',
    'level' : 'u_level',
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
        await message.channel.send("Not enough arguments : expected `&el update field1 value1 field2 value2 ...`")
        await message.channel.send("expected fields `" + '`, `'.join(field_alias) + "`")
        return -1
    
    updateMessage = ""
    for i in range(len(argv))[3::2]:
        key = argv[i - 1]
        if key in field_alias.keys():
            key = field_alias[key]
        else:
            await message.channel.send("Wrong keyword " + key)
            continue
        value = argv[i]

        if key == "name": # String value
            if not value.isalnum():
                await message.channel.send("Je ne negocie pas avec les teroristes")
                continue
            value = "'" + value + "'"
        else: # Int value
            try:
                value = str(int(value))
            except ValueError :
                await message.channel.send("Wrong input type, number expected. But got " + value)
                continue

        sqlReq = "UPDATE user SET " + key + " = " + value + " WHERE uuid = '" + str(message.author.id) + "';"
        if updateMessage == "":
            updateMessage = f"Updated values for {message.author.mention}:\n```"
        updateMessage += f"{argv[i - 1]} = {value}\n"
        print("SQL: " + sqlReq)
        
        cursor.execute(sqlReq)
        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(value) + "> : name updated!")
    
    if updateMessage != "":
        updateMessage += "```"
        connection.commit()
        await message.channel.send(updateMessage)

    # for key, value in update.items():
    #     if argv[2] == key :
    #         attribute = update[key]
    #         updated_value = argv[3]
    #         if key == 'name':
    #             cursor.execute("UPDATE user SET " + str(attribute) + " = '" + str(updated_value) + "' WHERE uuid = '" + str(message.author.id) + "';")
    #             print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(updated_value) + "> : name updated!")
    #         else:
    #             tmp = updated_value
    #             try :
    #                 updated_value = int(updated_value)
    #             except ValueError :
    #                 await message.channel.send("Wrong input type, number expected.")
    #                 return -1
    #             cursor.execute("UPDATE user SET " + str(attribute) + " = " + str(updated_value) + " WHERE uuid = '" + str(message.author.id) + "';")
    #             print("Update command")
    #             print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(attribute) + "> : <" + str(updated_value) + "> : updated!")
    #         connection.commit()
    #         return 0
    # await message.channel.send("Wrong keyword")
    # print("Update command")
    # return 0
