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
            print('gs done!')
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character level?")
        u_level = await client.wait_for('message')
        if message.author == u_level.author :
            print('lvl done!')
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character number of skill points?")
        u_skill = await client.wait_for('message')
        if message.author == u_skill.author :
            print('sp done!')
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Assault rune number?")
        r_red = await client.wait_for('message')
        if message.author == r_red.author :
            print('red rune done')
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Control rune number?")
        r_orange = await client.wait_for('message')
        if message.author == r_orange.author :
            print('orange rune done')
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        await message.channel.send(f"{message.author.mention} What is your main character Fate rune number?")
        r_yellow = await client.wait_for('message')
        if message.author == r_yellow.author :
            print('yellow rune done')
        else :
            await message.channel.send('error wrong user aborting')
            return 0
    
        await message.channel.send(f"{message.author.mention} What is your main character Protection rune number?")
        r_blue = await client.wait_for('message')
        if message.author == r_blue.author :
            print('blue rune done')
        else :
            await message.channel.send('error wrong user aborting')
            return 0
    
        await message.channel.send(f"{message.author.mention} What is your main character Support rune number?")
        r_green = await client.wait_for('message')
        if message.author == r_green.author :
            print('green rune done')
        else :
            await message.channel.send('error wrong user aborting')
            return 0
    
        await message.channel.send(f"{message.author.mention} What is your main character Awakening rune number?")
        r_purple = await client.wait_for('message')
        if message.author == r_purple.author :
            print('purple rune done')
            await message.channel.send(f'{message.author.mention} Registration done')
        else :
            await message.channel.send('error wrong user aborting')
            return 0

        cursor.execute("INSERT INTO user (uuid, name, u_gear, u_level, u_skill, r_red, r_orange, r_yellow, r_blue, r_green, r_purple) VALUES ('" + str(message.author.id) + "', '" + name.content +"', " + u_gear.content + ", " + u_level.content + ", " + u_skill.content + ", " + r_red.content + ", " + r_orange.content + ", " + r_yellow.content + ", " + r_blue.content + "," + r_green.content + ", " + r_purple.content + ");")
        connection.commit()
        #await channel.send(channel.last_message_id)


        #return 0
    else :
        await message.channel.send("User registration failed : already registered")
        # return -1

