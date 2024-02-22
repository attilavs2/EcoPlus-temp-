import sys
import discord

import db

secrets_file = open(sys.argv[1], mode="rt")

secrets = secrets_file.read()

secrets = secrets.split(";")

token = secrets[0]

db.credentials = secrets[1]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  content = message.content

  if content == "!hello":
    await message.channel.send('henlo')
    return
  if content == "!pinguncon":
    await message.channel.send("<499533339468759052>")

client.run(token)
