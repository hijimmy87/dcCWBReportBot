import discord
from discord.ext import commands
import asyncio, json, os
import keep_alive

with open('data/BotConfig.json', 'r', encoding = 'utf-8') as config:
    config = json.load(config)
with open('data/channel.json', 'r', encoding = 'utf-8') as channels:
    channels = json.load(channels)

bot = commands.Bot(command_prefix = config['prefix'], intents = discord.Intents.all())


async def status_task():
    i = True
    while not bot.is_closed():
        name = ['中央氣象局', '{}help 得不到幫助'.format(bot.command_prefix)][i]
        await bot.change_presence(activity = discord.Game(name))
        await asyncio.sleep(5)
        i = not i


@bot.event
async def on_ready():
    print('Bot Was Ready')
    print('Name: {}'.format(bot.user.name))
    print('ID:   {}'.format(bot.user.id))
    guilds = bot.guilds
    print("There are {} guilds".format(len(guilds) if guilds else 0))
    if guilds:
        for guild in guilds:
            print(guild.name)
    print('\n==================================================')
    bot.loop.create_task(status_task())


for file in os.listdir('./cmds'):
    if file.endswith('.py'):
        bot.load_extension('cmds.{}'.format(file[:-3]))

keep_alive.keep_alive()
if __name__ == '__main__':
    bot.run(config['token'])