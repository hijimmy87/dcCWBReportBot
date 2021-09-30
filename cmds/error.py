import discord
from discord.ext import commands
from core import Cog_Extension


class error(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send('```{}```'.format(error))
        print(type(error), '\n', error)

def setup(bot):
    bot.add_cog(error(bot))