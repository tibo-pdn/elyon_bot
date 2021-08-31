from config.db import cursor, connection
from datetime import datetime

async def addCommand(message, argv, client):
    cursor.execute("SELECT uuid FROM user WHERE uuid = '" + str(message.author.id) + "';")
    result = cursor.fetchone()

    if result is None :
        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(message.content) + "> : Add Command")
        await message.channel.send(f"{message.author.mention} What is your main character name?")
        name = await client.wait_for('message')
        if message.author == name.author :
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(name.content) + "> : name done!")
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(name.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character class? (slayer, elem, gunner, mystic, warlord, assa)")
        u_class = await client.wait_for('message')
        if message.author == u_class.author :
            while u_class.content != 'slayer' and u_class.content != 'elem' and u_class.content != 'gunner' and u_class.content != 'mystic' and u_class.content != 'warlord' and u_class.content != 'assa' :
                if message.author == u_class.author :
                    await message.channel.send(':x:error wrong input retry')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_class.content) + "> : input error!")
                    u_class = await client.wait_for('message')
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_class.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(u_class.content) + "> : class done!")
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_class.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character gearscore?")
        u_gear = await client.wait_for('message')
        if message.author == u_gear.author :
            tmp = u_gear
            while not isinstance(u_gear, int) :
                if message.author == u_gear.author :
                    try :
                        u_gear = int(u_gear.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_gear.content) + "> : input error!")
                        u_gear = await client.wait_for('message')
                        tmp = u_gear
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_gear.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(u_gear) + "> : gs done!")
            u_gear = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_gear.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character level?")
        u_level = await client.wait_for('message')
        if message.author == u_level.author :
            tmp= u_level
            while not isinstance(u_level, int) :
                if message.author == u_level.author :
                    try :
                        u_level = int(u_level.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(u_level.content) + "> : input error!")
                        u_level = await client.wait_for('message')
                        tmp = u_level
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_level.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(u_level) + "> : lvl done!")
            u_level = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_level.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character number of skill points?")
        u_skill = await client.wait_for('message')
        if message.author == u_skill.author :
            tmp = u_skill
            while not isinstance(u_skill, int) :
                if message.author == u_skill.author :
                    try :
                        u_skill = int(u_skill.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(u_skill.content) + "> : input error!")
                        u_skill = await client.wait_for('message')
                        tmp = u_skill
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_skill.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(u_skill) + "> : SP done!")
            u_skill = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(u_skill.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Assault rune number?")
        r_red = await client.wait_for('message')
        if message.author == r_red.author :
            tmp = r_red
            while not isinstance(r_red, int) :
                if message.author == r_red.author :
                    try :
                        r_red = int(r_red.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_red.content) + "> : input error!")
                        r_red = await client.wait_for('message')
                        tmp = r_red
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_red.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_red) + "> : Assault done!")
            r_red = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_red.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Control rune number?")
        r_orange = await client.wait_for('message')
        if message.author == r_orange.author :
            tmp = r_orange
            while not isinstance(r_orange, int) :
                if message.author == r_orange.author :
                    try :
                        r_orange = int(r_orange.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_orange.content) + "> : input error!")
                        r_orange = await client.wait_for('message')
                        tmp = r_orange
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_orange.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_orange) + "> : Control done!")
            r_orange = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_orange.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Fate rune number?")
        r_yellow = await client.wait_for('message')
        if message.author == r_yellow.author :
            tmp = r_yellow
            while not isinstance(r_yellow, int) :
                if message.author == r_yellow.author :
                    try :
                        r_yellow = int(r_yellow.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_yellow.content) + "> : input error!")
                        r_yellow = await client.wait_for('message')
                        tmp = r_yellow
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_yellow.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_yellow) + "> : fate done!")
            r_yellow = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_yellow.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Support rune number?")
        r_green = await client.wait_for('message')
        if message.author == r_green.author :
            tmp = r_green
            while not isinstance(r_green, int) :
                if message.author == r_green.author :
                    try :
                        r_green = int(r_green.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_green.content) + "> : input error!")
                        r_green = await client.wait_for('message')
                        tmp = r_green
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_green.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_green) + "> : support done!")
            r_green = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_green.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Protection rune number?")
        r_blue = await client.wait_for('message')
        if message.author == r_blue.author :
            tmp = r_blue
            while not isinstance(r_blue, int) :
                if message.author == r_blue.author :
                    try :
                        r_blue = int(r_blue.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_blue.content) + "> : input error!")
                        r_blue = await client.wait_for('message')
                        tmp = r_blue
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_blue.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_blue) + "> : protection done!")
            r_blue = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_blue.author) + "> : user error!")
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Awakening rune number?")
        r_purple = await client.wait_for('message')
        if message.author == r_purple.author :
            tmp = r_purple
            while not isinstance(r_purple, int) :
                if message.author == r_purple.author :
                    try :
                        r_purple = int(r_purple.content)
                    except ValueError :
                        await message.channel.send(':x:error wrong input retry')
                        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_purple.content) + "> : input error!")
                        r_purple = await client.wait_for('message')
                        tmp = r_purple
                else :
                    await message.channel.send(':x:error wrong user aborting')
                    print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_purple.author) + "> : user error!")
                    return 0
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> :  <" + str(r_purple) + "> : Awakening done!")
            r_purple = tmp
        else :
            await message.channel.send(':x:error wrong user aborting')
            print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : <" + str(r_purple.author) + "> : user error!")
            return 0
        tmp = 0
        await message.channel.send(f'{message.author.mention} Registration done')
        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : Registration done!")
        cursor.execute("INSERT INTO user (uuid, name, u_gear, u_level, u_skill, u_class, r_red, r_orange, r_yellow, r_blue, r_green, r_purple) VALUES ('" + str(message.author.id) + "', '" + name.content +"', " + u_gear.content + ", " + u_level.content + ", " + u_skill.content + ", '" + u_class.content + "' , " + r_red.content + ", " + r_orange.content + ", " + r_yellow.content + ", " + r_blue.content + "," + r_green.content + ", " + r_purple.content + ");")
        connection.commit()
        #await channel.send(channel.last_message_id)


        #return 0
    else :
        await message.channel.send(":x:User registration failed : already registered")
        print("[" + str(datetime.now()) + "] : <" + str(message.author) + "> : error user already exists!")

        # return -1

