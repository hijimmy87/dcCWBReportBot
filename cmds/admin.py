import discord
from discord.ext import commands
from core import Cog_Extension

import sys

class admin(Cog_Extension):

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, limit = 0):
        await ctx.channel.purge(limit = limit + 1)
        await ctx.send('`{}` message has been purged.'.format(limit))
    
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def moveto(self, ctx, to, limit = 0):
        print(to)
        print(type(to))
        # for i in range(limit + 1):
        #     msg = await ctx.channel.purge(limit = limit + 1)
        #     to.send(msg)
        # await ctx.send('`{}` message has been moved.'.format(limit))

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def say(self, ctx, *, args):
        await ctx.message.delete()
        await ctx.send(args)

    @commands.command()
    @commands.is_owner()
    async def stop(self, ctx):
        await ctx.send('`Bot is turning off.`')
        await self.bot.close()
        print('Bot is turning off.')
        sys.exit(0)
    

def setup(bot):
    bot.add_cog(admin(bot))