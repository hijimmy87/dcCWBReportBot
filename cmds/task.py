import discord
from discord.ext import commands
from core import Cog_Extension
from api.weather import getCWB

import asyncio, json
from datetime import datetime, timedelta


class task(Cog_Extension):
    def __init__(self, bot):
        super().__init__(bot)
        
        async def weather():
            await self.bot.wait_until_ready()
            with open('time.json', 'r', encoding = 'utf-8') as time:
                time = json.load(time)
            channel = bot.get_channel(self.channels['weather'])
            
            while not bot.is_closed():
                for datail in ['E-A0015-001', 'E-A0016-001']:
                    data = getCWB(datail)
                    if data is not None and data['time'] != time[datail]:
                        time[datail] = data['time']
                        
                        content = data['content']
                        embed = discord.Embed(color = self.color())
                        embed.title = data['title']
                        embed.set_image(url = data['image'])
                        embed.set_footer(**data['footer'])
                        for field in data['field']:
                            embed.add_field(**field)
                        await channel.send(content, embed=embed)
                    await asyncio.sleep(1)
                
                for datail in ['W-C0033-002']:
                    data = getCWB(datail)
                    if data is not None and data['time'] != time[datail]:
                        time[datail] = data['time']
                        
                        embed = discord.Embed(
                            title = data['title'],
                            description = data['description'],
                            timestamp = data['timestamp'],
                            color = self.color()
                        )
                        embed.set_footer(**data['footer'])
                        for field in data['field']:
                            embed.add_field(**field)
                        await channel.send(embed=embed)
                    await asyncio.sleep(1)
                
                with open('time.json', 'w', encoding = 'utf-8') as file:
                    json.dump(time, file, indent = 4)
        
        async def tellTime():
            def is_me(m):
                return m.author == bot.user
            
            await self.bot.wait_until_ready()
            while not bot.is_closed():
                now = datetime.utcnow() + timedelta(hours = 8)
                if now.minute % 5 == 0 and now.second <= 5:
                    channel = bot.get_channel(self.channels["time"])
                    await channel.purge(limit = 1, check = is_me)
                    await channel.send(now.strftime('%H 時 %M 分 %S 秒'))
                    await asyncio.sleep(5)
                await asyncio.sleep(1)
        
        async def morning():
            await self.bot.wait_until_ready()
            while not bot.is_closed():
                now = datetime.utcnow() + timedelta(hours = 8)
                if now.hour == 6 and now.minute == 0 and now.second <= 5:
                    channel = bot.get_channel(self.channels["morning"])
                    await channel.send('おはよう世界\nGood Morning World!')
                    await asyncio.sleep(5)
                await asyncio.sleep(1)
        
        self.bot.loop.create_task(weather())
        # self.bot.loop.create_task(tellTime())
        self.bot.loop.create_task(morning())
    

def setup(bot):
    bot.add_cog(task(bot))