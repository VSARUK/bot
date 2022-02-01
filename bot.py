import discord
import os
from dotenv import load_dotenv

load_dotenv('secureCunt.env')
TOKEN = os.getenv("DISCORD_TOKEN")
##TOKEN = "OTM4MTcwNTU0NDMzODI2ODQ2.YfmZag.RNoQVZU2HN4p7g2rHQ7an6o5IZ0"
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
