import discord
from discord.ext import commands
from core import Cog_Extension

class info(Cog_Extension):
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('{:.2f} ms'.format(self.bot.latency * 1000))

def setup(bot):
    bot.add_cog(info(bot))