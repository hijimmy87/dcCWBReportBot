import discord
from discord.ext import commands
from core import Cog_Extension

class load(Cog_Extension):

    @commands.command()
    @commands.has_guild_permissions(administrator = True)
    async def load(self, ctx, extenson):
        self.bot.load_extension('cmds.{}'.format(extenson))
        await ctx.send('`{}` has been loaded'.format(extenson))

    @commands.command()
    @commands.has_guild_permissions(administrator = True)
    async def reload(self, ctx, extenson):
        self.bot.reload_extension('cmds.{}'.format(extenson))
        await ctx.send('`{}` has been reloaded'.format(extenson))

    @commands.command()
    @commands.has_guild_permissions(administrator = True)
    async def unload(self, ctx, extenson):
        self.bot.unload_extension('cmds.{}'.format(extenson))
        await ctx.send('`{}` has been unloaded'.format(extenson))

def setup(bot):
    bot.add_cog(load(bot))