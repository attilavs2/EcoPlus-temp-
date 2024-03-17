import sys
import random
import discord
import datetime

import db

secrets_file = open(sys.argv[1], mode="rt")

secrets = secrets_file.read()

secrets = secrets.split(";")

token = secrets[0]

db.credentials = secrets[1]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.moderation = True

client = discord.Client(intents=intents, activity=discord.Game(name='En train de niquer des mères'))

guilds = []

globals()["gmembers"] = {}

async def pinguncon(message):
  #fcalva's server
  if message.guild.id == 750665878072328242:
    await message.channel.send("<@499533339468759052>")
  elif message.guild.id in [1008485562304450610, 1157767629738618941]:
    await message.channel.send("<@755081785393676328>")
  else:
    await message.channel.send("pas dispo ici")

async def pingrand(message):
  choice = random.choice(globals()["gmembers"][str(message.guild.id)])
  await message.channel.send("<@"+str(choice.id)+">")

async def roulette(message):
  roll = random.random()
  if roll < 0.16666666666:
    tdelt = datetime.timedelta(minutes=5)
    try:
      await message.author.timeout(tdelt, reason="Vous avez perdu à la roulette...")
    except:
      await message.channel.send("Une erreur s'est produite ! (Je ne peux probablement pas vous timeout)")
  else:
    await message.channel.send("Ouf ! Il n'y avait pas de cartouche dans la chambre...")

async def ecohelp(message):
  await message.channel.send("Eco+, un bot Eco plus pour faire des conneries\n"\
                              "?pinguncon : ping le con local\n"\
                              "?pingrand : ping un membre aléatoire du serveur\n"
                              "?roulette : Prennez une chance sur six de vous faire timeout")

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

  if content == "?hello":
    await message.channel.send('henlo')
    return
  if content == "?pinguncon":
    await pinguncon(message)
  if content == "?pingrand":
    await pingrand(message)
  if content == "?roulette":
    await roulette(message)
  if content == "?help":
    await ecohelp(message )

client.run(token)
