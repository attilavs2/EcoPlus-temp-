import sys
import random
import discord

import db

secrets_file = open(sys.argv[1], mode="rt")

secrets = secrets_file.read()

secrets = secrets.split(";")

token = secrets[0]

db.credentials = secrets[1]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents, activity=discord.Game(name='En train de niquer des mères'))

guilds = []

globals()["gmembers"] = {}

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  async for guild in client.fetch_guilds(limit=150):
    print(str(guild.id)+":")
    guilds.append(guild)
    sid = str(guild.id)
    globals()["gmembers"] |= {sid:[]}
    async for member in guild.fetch_members(limit=150):
      globals()["gmembers"][sid].append(member)
      print("  "+str(member))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  content = message.content

  if content == "!hello":
    await message.channel.send('henlo')
    return
  if content == "!pinguncon":
    #fcalva's server
    if message.guild.id == 750665878072328242:
      await message.channel.send("<@499533339468759052>")
    elif message.guild.id in [1008485562304450610, 1157767629738618941]:
      await message.channel.send("<@755081785393676328>")
    else:
      await message.channel.send("pas dispo ici")
  if content == "!pingrand":
    choice = random.choice(globals()["gmembers"][str(message.guild.id)])
    await message.channel.send("<@"+str(choice.id)+">")


client.run(token)
