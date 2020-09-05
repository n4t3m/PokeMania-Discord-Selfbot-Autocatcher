import discord
from discord.ext import commands
import requests
import setup
import json
import asyncio
import random
import sys
import guilds
import checks

TOKEN = setup.TOK
client = commands.Bot(command_prefix='sb!', self_bot=True, fetch_offline_members=False)
client.remove_command('help')
PREFIXES = guilds.prefixes
DELAY = setup.DELAY
SELFBOT_UID = setup.SELFBOT_UID
OWNER_UID = setup.OWNER_UID
BALL_TYPE = setup.BALL_TYPE
BUY_BALL_AMOUNT = setup.BUY_BALL_AMOUNT
client.MONEY = 0
client.last_catch_attempt = {}
client.captured = []
client.escape = []
client.catch_type = ""
BOT_PREFIX = "sb!"
CAPTURE_CHANCE = setup.CAPTURE_CHANCE





@client.event
async def on_ready():
    client.catch_type = determinePokeball()
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("azusa thumb war me")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.author == client.user:   
        return

    if message.content == BOT_PREFIX + "ping" and message.author.id == OWNER_UID:
        await ping(message)
        return

    if BOT_PREFIX + "eval" in message.content and message.author.id == OWNER_UID:
        await eval(message)
        return

    if message.content == BOT_PREFIX + "toggle":
        channel = message.channel
        await asyncio.sleep(1)
        await channel.send("You want to toggle the autocatcher. Type 'YES' to continue.")

        def check(m):
            return m.content == 'YES' and m.channel == channel

        msg = await client.wait_for('message', check=check, timeout=30.0)
        await asyncio.sleep(2)
        await channel.send('Autocatcher has been switched from NONE to NONE')
        return
    
    if  message.author.id == 627952266455941121 and message.guild.id not in PREFIXES:
        print(str(message.guild.id) + " is not configured.")
        return
        
    
    if message.author.id != 627952266455941121:
        if message.author.id != OWNER_UID:
            return
    
    if not len(message.embeds) > 0:
        return

    try:
        if message.author.id == 627952266455941121 and len(message.embeds) > 0 and "A wild Pokémon has appeared!" in message.embeds[0].to_dict()['author']['name']:
            #print('yo')
            await asyncio.sleep(DELAY)
            name = message.embeds[0].image.url.split('/')[5][:-4]
            shiny = False
            if "-shiny" in message.embeds[0].image.url.split('/')[4]:
                print("Shiny Pokemon Has Spawned!")
                shiny = True
            if "-" in name:
                split = name.split('-')
                name = split[0]
                if split[1] == "alola":
                    name = "alolan " + name
                if split[1] == "galar":
                    name = "galarian " + name
            if name == "flabebe":
                name = "flabébé"
            await message.channel.send(PREFIXES[message.guild.id] + client.catch_type + " " + name)
            if shiny:
                print("Shiny Pokemon Captured!!! Shiny " + name)
            client.last_catch_attempt[message.guild.id] = PREFIXES[message.guild.id] + client.catch_type + " " + name
            return
    except Exception as ex:
            pass
    try:
        if message.author.id == 627952266455941121 and len(message.embeds) > 0 and "don't have any ultra balls!" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
            await asyncio.sleep(2)
            await message.channel.send(PREFIXES[message.guild.id] + "buy ball ultraball " + str(BUY_BALL_AMOUNT))
            await asyncio.sleep(2)
            await message.channel.send(client.last_catch_attempt[message.guild.id])

        if message.author.id == 627952266455941121 and len(message.embeds) > 0 and "don't have any great balls!" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
            await asyncio.sleep(2)
            await message.channel.send(PREFIXES[message.guild.id] + "buy ball greatball " + str(BUY_BALL_AMOUNT))
            await asyncio.sleep(2)
            await message.channel.send(client.last_catch_attempt[message.guild.id])

        if message.author.id == 627952266455941121 and len(message.embeds) > 0 and "don't have any pokeballs!!" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
            await asyncio.sleep(2)
            await message.channel.send(PREFIXES[message.guild.id] + "buy ball pokeball " + str(BUY_BALL_AMOUNT))
            await asyncio.sleep(2)
            await message.channel.send(client.last_catch_attempt[message.guild.id])
    except Exception as ex:
        pass

    #alola/galar can be caught but won't show properly
    if message.author.id == 627952266455941121 and len(message.embeds) > 0 and  "Congratulations" in message.embeds[0].description and "You caught a" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
        msg = message.embeds[0].description
        words = msg.split(' ')
        # client.MONEY = client.MONEY + int(words[len(words)-2])
        # print("Total Pokedollers Gained This Run: " + str(client.MONEY))
        print(msg[40:])
        client.captured.append(words[len(words)-5])
        if random.randint(0,100) < 10:
            await message.channel.send("yess I wanted to catch it so bad")
        updateWebpage()
        return

    if message.author.id == 627952266455941121 and len(message.embeds) > 0 and "pokemon has escaped from" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
        arr = client.last_catch_attempt[message.guild.id].split(' ')
        escaped = ""
        for i in range(1, len(arr)):
            escaped = escaped + arr[i]
        print("Attemped to catch " + escaped.capitalize() + " but it escaped...")
        client.last_catch_attempt[message.guild.id] = ""
        client.escape.append(escaped.capitalize())
        if random.randint(0,100) < 10:
            await message.channel.send("damnit i really wanted that one")
        updateWebpage()
        return

    if message.author.id == 627952266455941121 and len(message.embeds) > 0 and "like this is the wrong pokemon!" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
        bug = client.last_catch_attempt[message.guild.id].split(' ')[1]
        print("Attemped to catch " + bug + " but the name was incorrect.")
        client.last_catch_attempt[message.guild.id] = ""
        if random.randint(0,100) < 10:
            await message.channel.send("wtf how")
        return



    await client.process_commands(message)

@client.command()
async def ping(self, ctx):
    print("invoked")
    await ctx.send('pong')

async def ping(message):
    await message.channel.send('Pong! {0}'.format(round(client.latency, 1)))
    return

async def eval(message):
    m = message.content
    prefix = BOT_PREFIX + "eval "
    cmd = m[m.startswith(prefix) and len(prefix):]
    await message.channel.send(PREFIXES[message.guild.id] + cmd)
    return

#Needs to be fixed
def updateWebpage():
    w = open("status.html", "w")
    w.write("<!DOCTYPE html>" + "\n" + "<html>" + "\n" + "<head>" + "\n" + "<title>Autocatcher Summary</title>" + "\n" + "</head>" + "\n" + "<body>" + "\n" + "\n" + "<h1>Autocatcher Summary</h1>" + "\n")
    w.write("<p>" + "Total Money this run: " + str(client.MONEY) + "</p>" + "\n")
    st = "<p>Captured Pokemon: "
    for p in client.captured:
        st = st + p + ", "
    st = st[:-2] + "</p>"
    w.write(st)
    w.write("\n")
    st = "<p>Escaped Pokemon: "
    for p in client.escape:
        st = st + p + ", "
    st = st[:-2] + "</p>"
    w.write(st)
    w.close()

def determinePokeball():
    if BALL_TYPE == "POKEBALL":
        return "catch"
    if BALL_TYPE == "GREATBALL":
        return "gcatch"
    if BALL_TYPE == "ULTRABALL":
        return "ucatch"


    
c = checks.Checker()
c.verifyVals()  
print("Logging in...")
client.run(TOKEN, bot=False)