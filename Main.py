
import nextcord
from nextcord.ext import commands
import DataHandler
import GlobalFunctions
import logging
import Admin
import TaskMasterGui
import random
from nextcord.ui import TextInput
import json
import datetime

with open('Swears.txt', 'r') as f:
    words = f.read()
    badwords = words.split()


# Settings
with open("token.txt", 'r') as fp:
    gTOKEN = fp.readline()

gPREFIX = "!"   


# Bot
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

description = '''Discord osrs bot'''
bot = commands.Bot(intents=intents, command_prefix=gPREFIX, description='SkillMaster',  case_insensitive=True)





@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#@bot.event
#async def on_message(message):
#    for i in range(len(badwords)):
#        if badwords[i] in message.content:
#            for j in range(1):
#                await message.channel.send("nono")
#                return


#Admin stuff
@bot.command()
async def Startgame(ctx):
    await Admin.startgame(ctx)




#User stuff
@bot.command()
async def join(ctx):
    await GlobalFunctions.joingame(ctx)
    




#Test stuff
@bot.command()
async def ping(ctx):
    Chance = random.randint(1,10)
    if Chance < 10:
        await ctx.send("Pong")
    else:
        await ctx.send("!PING !PING !PING !PING How does it feel human!")



@bot.command()
async def Game(ctx):
    await TaskMasterGui.show_embed_gui(ctx, bot)



@bot.command()
async def Score(ctx):
    json_file = "SkillMasters/Database.json"  # Replace with the path to your JSON file

    with open(json_file, "r") as file:
        data = json.load(file)

    embed = DataHandler.generate_leaderboard_embed(data)
    channel = ctx.bot.get_channel(1141005342914924694)
    await channel.send(embed=embed)


@bot.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 100):
    if ctx.author.id == 631886189493747723:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("no :)")


@bot.command()
async def reduce_xp(ctx, person, amount: int):
    if ctx.author.id == 368690612754448386 or 631886189493747723:
        person = person.strip("<@!>")
        user = await bot.fetch_user(person)
        # Open the JSON file and load the data
        with open("SkillMasters/Database.json", "r") as file:
            data = json.load(file)
    
        # Check if the person's ID is in the data
        if str(person) in data:
            # Reduce the XP by the specified amount
            data[str(person)]["xp"] -= amount
        
            # Write the updated data back to the JSON file
            with open("SkillMasters/Database.json", "w") as file:
                json.dump(data, file, indent=4)
        
            await ctx.send(f"Reduced {amount} XP from {user.name}'s account.")
        else:
            await ctx.send("Person not found in the database.")
    else:
        await ctx.send("na :)")



logging.basicConfig(level=logging.ERROR)
bot.run(gTOKEN)
