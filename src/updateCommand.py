from config.db import cursor, connection
from datetime import datetime
from .addCommand import USERINFOS_LIST, sanitizeUserInfo
from .infoCommand import infoCommand

# 0 name
# 1 u_gear
# 2 u_level
# 3 u_skill
# 4 u_class
# 5 r_red
# 6 r_orange
# 7 r_yellow
# 8 r_green
# 9 r_blue
# 10 r_purple

FIELD_ALIAS = {
    'name' : 0,
    'gs' : 1,
    'lvl' : 2,
    'level' : 2,
    'sp' : 3,
    #'klass' : 4,
    'red' : 5,
    'orange' : 6,
    'yellow' : 7,
    'green' : 8,
    'blue' : 9,
    'purple' : 10
}

async def updateCommand(message, argv, client):
    if len(argv) < 4:
        await message.channel.send("Not enough arguments : expected `&el update field1 value1 field2 value2 ...`")
        await message.channel.send("expected fields `" + '`, `'.join(FIELD_ALIAS) + "`")
        return -1
    
    updateMessage = ""
    for i in range(len(argv))[3::2]:
        key = argv[i - 1]
        if not key in FIELD_ALIAS.keys():
            await message.channel.send("Wrong keyword " + key)
            continue

        info = USERINFOS_LIST[FIELD_ALIAS[key]]
        sanitized, error = sanitizeUserInfo(info, argv[i])

        if error != None:
            await message.channel.send(error)
            continue

        sqlReq = "UPDATE user SET " + info[0] + " = " + sanitized + " WHERE uuid = '" + str(message.author.id) + "';"
        if updateMessage == "":
            updateMessage = f"Updated values for {message.author.mention}:\n```"
        updateMessage += f"{argv[i - 1]} = {sanitized}\n"
        #print("SQL: " + sqlReq)
        
        cursor.execute(sqlReq)
        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(sanitized) + "> : " + info[0] + " updated!")
    
    if updateMessage != "":
        updateMessage += "```"
        connection.commit()
        await message.channel.send(updateMessage)
        await infoCommand(message, ["&el", "info"], client)
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
