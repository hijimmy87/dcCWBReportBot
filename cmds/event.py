import discord
from discord.ext import commands
from core import Cog_Extension

from datetime import datetime, timedelta

def now() -> tuple:
    nowUTC = datetime.utcnow()
    now = nowUTC + timedelta(hours=8)
    date = now.strftime('%Y/%m/%d 星期') + ['一', '二', '三', '四', '五', '六', '日'][now.weekday()]
    time = now.strftime('%H:%M:%S')
    return nowUTC, date, time

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.channels['member_join'])
        nowUTC, date, time = now()
        embed = discord.Embed(color = self.color(), timestamp = nowUTC)
        embed.description = '{} 加入伺服器!\n\n加入成員: {}\n加入日期: {}\n加入時間: {}'.format(member.mention, member, date, time)
        embed.set_footer(text = 'Powered by Jimmy')
        await channel.send(member.mention, embed = embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(self.channels['member_remove'])
        nowUTC, date, time = now()
        embed = discord.Embed(color = self.color(), timestamp = nowUTC)
        embed.description = '{} 離開了伺服器.\n\n離開成員: {}\n離開日期: {}\n離開時間: {}'.format(member.mention, member, date, time)
        embed.set_footer(text = 'Powered by Jimmy')
        await channel.send(embed = embed)

def setup(bot):
    bot.add_cog(event(bot))