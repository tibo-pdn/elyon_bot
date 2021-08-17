from src.addCommand import addCommand
from src.deleteCommand import deleteCommand
from src.listCommand import listCommand
from src.updateCommand import updateCommand
from src.infoCommand import infoCommand
from src.helpCommand import helpCommand

commands = {
    'add' : addCommand,
    'delete' : deleteCommand,
    'list' : listCommand,
    'info' : infoCommand,
    'update' : updateCommand,
    'help' : helpCommand,
    '-h' : helpCommand,
    '--help' : helpCommand
}

async def split_args(message, argv, client) :
    if len(argv) < 2:
        await message.channel.send("No command")
        return -1
    for key, value in commands.items():
        if argv[1] == key:
            await commands[key](message, argv, client)
            return 0
    await message.channel.send("Wrong command")
    return -1
