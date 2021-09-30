import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('data/channel.json', 'r', encoding='utf-8') as channels:
            self.channels = eval(channels.read())
    
    def color(self):
        return discord.Color.random()