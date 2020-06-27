import discord
from discord.ext import commands
import requests
import setup
import json
import asyncio
import random
import sys

TOKEN = setup.TOK
client = commands.Bot(command_prefix='!', self_bot=True, fetch_offline_members=False)
client.remove_command('help')
PREFIX = setup.PREFIX
DELAY = setup.DELAY
SELFBOT_UID = setup.SELFBOT_UID
OWNER_UID = setup.OWNER_UID
BALL_TYPE = setup.BALL_TYPE
client.MONEY = 0
client.last_catch_attempt = ""
client.captured = []
client.escape = []


@client.event
async def on_ready():
    print("we made it here")
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("azunyan <3")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.author == client.user:   
        return
    
    if message.author.id != 627952266455941121:
        if message.author.id != OWNER_UID:
            return

    try:
        if message.author.id == 627952266455941121 and len(message.embeds) > 0 and "A wild Pokémon has appeared!" in message.embeds[0].title:
            await asyncio.sleep(DELAY)
            name = message.embeds[0].image.url.split('/')[5][:-4]
            if "-" in name:
                split = name.split('-')
                name = split[0]
                if split[1] == "alola":
                    name = "alolan " + name
                if split[1] == "galar":
                    name = "galarian " + name
            if name == "flabebe":
                name = "flabébé"
            await message.channel.send(PREFIX + "catch " + name)
            client.last_catch_attempt = PREFIX + "catch " + name
            return
    except Exception as ex:
            pass

    if message.author.id == 627952266455941121 and "Congratulations" in message.embeds[0].description and "You caught a" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
        msg = message.embeds[0].description
        words = msg.split(' ')
        client.MONEY = client.MONEY + int(words[len(words)-2])
        print("Total Pokedollers Gained This Run: " + str(client.MONEY))
        print("Captured a " + words[len(words)-5] + "!")
        client.captured.append(words[len(words)-5])
        if random.randint(0,100) < 10:
            await message.channel.send("yess I wanted to catch it so bad")
        updateWebpage()
        return

    if message.author.id == 627952266455941121 and "pokemon has escaped from" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
        arr = client.last_catch_attempt.split(' ')
        escaped = ""
        for i in range(1, len(arr)):
            escaped = escaped + arr[i]
        print("Attemped to catch " + escaped.capitalize() + " but it escaped...")
        client.last_catch_attempt = ""
        client.escape.append(escaped.capitalize())
        if random.randint(0,100) < 10:
            await message.channel.send("damnit i really wanted that one")
        updateWebpage()
        return

    if message.author.id == 627952266455941121 and "like this is the wrong pokemon!" in message.embeds[0].description and str(SELFBOT_UID) in message.embeds[0].description:
        bug = client.last_catch_attempt.split(' ')[1]
        print("Attemped to catch " + bug + " but the name was incorrect.")
        client.last_catch_attempt = ""
        if random.randint(0,100) < 10:
            await message.channel.send("wtf how")
        return



    await client.process_commands(message)

@client.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Latency is {:.2f}ms'.format(duration))

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


    
if BALL_TYPE != "POKEBALL" and BALL_TYPE != "GREATBALL" and BALL_TYPE != "ULTRABALL":
    sys.exit("Pokeball Type Not Configured or Incorrectly Configured")  
print("logging in")
client.run(TOKEN, bot=False)