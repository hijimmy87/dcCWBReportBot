import discord
from discord.ext import commands
from core import Cog_Extension

from typing import Union
import requests as req


class mc(Cog_Extension):
    
    def __getInfo(self, User) -> Union[dict, None]:
        url = 'https://api.ashcon.app/mojang/v2/user/{}'.format(User)
        result = req.get(url)
        return result.json()
    
    def __getUUID(Username: str, timestamp: int = None) -> Union[str, None]:
        url = 'https://api.mojang.com/users/profiles/minecraft/{}'.format(Username)
        if timestamp:
            url = url + '?at={}'.format(timestamp)
        result = req.get(url)
        return result.json()['id'] if result.status_code == 200 else None
    
    
    @commands.command()
    async def skin(self, ctx, User):
        info = self.__getInfo(User)
        if 'textures' in info.keys():
            userneame = info['username']
            id = info['uuid']
            skinURL = info['textures']['skin']['url']
            skinViewURL = 'https://mc-heads.net/body/{}'.format(id)
            embed = discord.Embed(color = self.color())
            embed.title = userneame
            embed.set_thumbnail(url = skinURL)
            embed.set_image(url = skinViewURL)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(color = self.color())
            embed.title = info['error']
            embed.description = info['reason']
            await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(mc(bot))