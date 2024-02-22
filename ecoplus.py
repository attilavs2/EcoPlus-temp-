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

gmembers = []

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  gid = 750665878072328242
  guild = client.get_guild(gid)

  async for member in guild.fetch_members(limit=150):
    gmembers.append(member)
    print(member)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  content = message.content

  if content == "!hello":
    await message.channel.send('henlo')
    return
  if content == "!pinguncon":
    await message.channel.send("<@499533339468759052>")
  if content == "!pingrand":
    choice = random.choice(gmembers)
    await message.channel.send("<@"+str(choice.id)+">")


client.run(token)
