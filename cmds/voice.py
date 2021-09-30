import discord
from discord.ext import commands
from core import Cog_Extension


class voice(Cog_Extension):

    def __inVoiceCategory(self, channel):
        voiceCategory = self.bot.get_channel(self.channels['voice']).category
        return False if channel == None else channel.category == voiceCategory and channel.id != self.channels['voice']
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        voiceCategory = self.bot.get_channel(self.channels['voice']).category
        if after.channel and after.channel.id == self.channels['voice']:
            guild = voiceCategory.guild
            channel = await guild.create_voice_channel(name = '{}\'s channel'.format(member.display_name), category = voiceCategory)
            await channel.set_permissions(member, connect = True)
            await member.move_to(channel)
        
        if self.__inVoiceCategory(before.channel):
            if len(before.channel.members) == 0:
                await before.channel.delete()
    
    @commands.group(name = 'voice')
    async def voice(self, ctx):
        pass
    
    @voice.command(help = 'Rename your voice channel')
    async def rename(self, ctx, *, new_name = None):
        if (channel := ctx.author.voice.channel) and self.__inVoiceCategory(channel):
            await channel.edit(name = new_name)
            await ctx.send('Channel name has been renamed.')
        else:
            await ctx.send('You aren\'t in the specific channel.')

    @voice.command(help = 'Setting the user limit of your voice channel.')
    async def user_limit(self, ctx, limit = 1):
        if (channel := ctx.author.voice.channel) and self.__inVoiceCategory(channel):
            await channel.edit(user_limit = limit)
            await ctx.send('User limit has been set up.')
        else:
            await ctx.send('You aren\'t in the specific channel.')

def setup(bot):
    bot.add_cog(voice(bot))