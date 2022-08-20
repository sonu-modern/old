from cheggscraper import Downloader
import discord
import discord.ext
from discord.ext import commands
#import inviter
import asyncio
import os
import json

bot = discord.Client()
bot = commands.Bot(command_prefix='#')
#tracker = inviter.InviteTracker(bot)



@bot.event
async def on_member_join(member):
    pass


@bot.event
async def on_message(message):
      if message.channel.id == 1001772700294971392:
  
        
      

          
            arg = message.content
        
        
            path = Downloader.main(url=str(message.content))
        #await asyncio.wait(3) 
       # await message.channel.send(file=discord.File(path))
            embed = discord.Embed(
                  title="welcome",
                  description="solution in DM",
                  colour=discord.Colour(0xffff00))
                     
             
            await message.channel.send(message.author.mention)
            await message.channel.send(embed=embed)
        
        
            await message.author.send(file=discord.File(path))
        
            await message.author.send(embed=embed)
            await message.delete()
        #await asyncio.wait(3)
            os.remove(path=path)
bot.run('OTg1MzA1NTc4MTI3NjUwODc3.GdgCUf.AWbPeiD9c58EhKXnV_l6id3go89EpbOXDA2mWU')  

