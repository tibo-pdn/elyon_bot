from config.db import cursor, connection

async def addCommand(message, argv, client):
    cursor.execute("SELECT uuid FROM user WHERE uuid = '" + str(message.author.id) + "';")
    result = cursor.fetchone()
    print("Add command")

    if result is None :
        print(message.author)
        await message.channel.send(f"{message.author.mention} What is your main character name?")
        name = await client.wait_for('message')
        if message.author == name.author :
            print("name done!")
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character gearscore?")
        u_gear = await client.wait_for('message')
        if message.author == u_gear.author :
            tmp = u_gear
            while not isinstance(u_gear, int) :
                if message.author == u_gear.author :
                    try :
                        u_gear = int(u_gear.content)
                        if u_gear == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        u_gear = await client.wait_for('message')
                        tmp = u_gear
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('gs done!')
            u_gear = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character level?")
        u_level = await client.wait_for('message')
        if message.author == u_level.author :
            tmp= u_level
            while not isinstance(u_level, int) :
                if message.author == u_level.author :
                    try :
                        u_level = int(u_level.content)
                        if u_level == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        u_level = await client.wait_for('message')
                        tmp = u_level
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('lvl done!')
            u_level = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character number of skill points?")
        u_skill = await client.wait_for('message')
        if message.author == u_skill.author :
            tmp = u_skill
            while not isinstance(u_skill, int) :
                if message.author == u_skill.author :
                    try :
                        u_skill = int(u_skill.content)
                        if u_skill == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        u_skill = await client.wait_for('message')
                        tmp = u_skill
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('SP done!')
            u_skill = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Assault rune number?")
        r_red = await client.wait_for('message')
        if message.author == r_red.author :
            tmp = r_red
            while not isinstance(r_red, int) :
                if message.author == r_red.author :
                    try :
                        r_red = int(r_red.content)
                        if r_red == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        r_red = await client.wait_for('message')
                        tmp = r_red
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('Assault done!')
            r_red = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Control rune number?")
        r_orange = await client.wait_for('message')
        if message.author == r_orange.author :
            tmp = r_orange
            while not isinstance(r_orange, int) :
                if message.author == r_orange.author :
                    try :
                        r_orange = int(r_orange.content)
                        if r_orange == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        r_orange = await client.wait_for('message')
                        tmp = r_orange
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('Control done!')
            r_orange = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Fate rune number?")
        r_yellow = await client.wait_for('message')
        if message.author == r_yellow.author :
            tmp = r_yellow
            while not isinstance(r_yellow, int) :
                if message.author == r_yellow.author :
                    try :
                        r_yellow = int(r_yellow.content)
                        if r_yellow == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        r_yellow = await client.wait_for('message')
                        tmp = r_yellow
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('fate done!')
            r_yellow = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Support rune number?")
        r_green = await client.wait_for('message')
        if message.author == r_green.author :
            tmp = r_green
            while not isinstance(r_green, int) :
                if message.author == r_green.author :
                    try :
                        r_green = int(r_green.content)
                        if r_green == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        r_green = await client.wait_for('message')
                        tmp = r_green
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('support done!')
            r_green = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Protection rune number?")
        r_blue = await client.wait_for('message')
        if message.author == r_blue.author :
            tmp = r_blue
            while not isinstance(r_blue, int) :
                if message.author == r_blue.author :
                    try :
                        r_blue = int(r_blue.content)
                        if r_blue == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        r_blue = await client.wait_for('message')
                        tmp = r_blue
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('protection done!')
            r_blue = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Awakening rune number?")
        r_purple = await client.wait_for('message')
        if message.author == r_purple.author :
            tmp = r_purple
            while not isinstance(r_purple, int) :
                if message.author == r_purple.author :
                    try :
                        r_purple = int(r_purple.content)
                        if r_purple == int :
                            print('ok')
                    except ValueError :
                        await message.channel.send('error wrong input retry')
                        r_purple = await client.wait_for('message')
                        tmp = r_purple
                else :
                    await message.channel.send('error wrong user aborting')
                    return 0
            print('Awakening done!')
            r_purple = tmp
        else :
            await message.channel.send('error wrong user aborting')
            return 0
        tmp = 0
        await message.channel.send(f'{message.author.mention} Registration done')
        cursor.execute("INSERT INTO user (uuid, name, u_gear, u_level, u_skill, r_red, r_orange, r_yellow, r_blue, r_green, r_purple) VALUES ('" + str(message.author.id) + "', '" + name.content +"', " + u_gear.content + ", " + u_level.content + ", " + u_skill.content + ", " + r_red.content + ", " + r_orange.content + ", " + r_yellow.content + ", " + r_blue.content + "," + r_green.content + ", " + r_purple.content + ");")
        connection.commit()
        #await channel.send(channel.last_message_id)


        #return 0
    else :
        await message.channel.send("User registration failed : already registered")
        # return -1

