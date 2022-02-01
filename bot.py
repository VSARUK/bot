import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv('secureCunt.env')
TOKEN = os.getenv("DISCORD_TOKEN")
#
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
@client.event
async def hello( ):
          await ctx.send("Hi")

client.run(TOKEN)
