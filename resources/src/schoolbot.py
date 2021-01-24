# coding=utf-8

#0 Documentation
#0.1 Threading usage
    # Only use threading.Thread, if time.sleep is in the code snippet to use less performance

#0.2 Variables
    #0.2.1 prefix
        #prefixfile: file the custom prefixes are stored in
        #custom_prefixes: dict of custom prefixes in relation to guild id
        #prefix: prefix for current message (gets updated on message)
    #0.2.2 language
        #lang: dict of messages in language for guild of current message (link to msg_ger / msg_eng)
        #!Wherever a message multi-language message is used, "lang" must be declared as global!!!
        #langfile: file the choice of language is stored in
        #langs: dict of choosen languages in relation to guild id
        #gerfile: file the messages in german language are stored in
        #engfile: file the messages in english language are stored in
        #msg_ger: dict of messages in german
        #msg_eng: dict of messages in english

#0.3 Messages
    #lang[0]: helpembed page "setup" title
    #lang[1]: helpembed page "assignments" title

#0.4 Cogs
    #Since I work with cogs now, this file has only 2 (main) purposes: loading/unloading/reloading single or grouped cogs and transmitting variables, which are all stored in this file as a central place.
    #Everything else is in subfolders of the src folder.



#1 imports
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
import json
import os



#2 settings
#2.1 Activate Intents from API
intents = discord.Intents.all()



#3 instance variables
prefix = ""
lang = {}
custom_prefixes = {}
langs = {}
msg_ger = {}
msg_eng = {}
setupchannels = {}



#4 initalizing
#4.1 prefix
with open("../data/usr/prefix.json") as prefixfile:
    custom_prefixes = json.load(prefixfile)
default_prefix = '§'

#4.2 language
with open("../data/usr/lang.json") as langfile:
    langs = json.load(langfile)

#4.3 multi-language messages
#4.3.1 german
with open("../data/lang/german.json") as gerfile:
    msg_ger = json.load(gerfile)
#4.3.2 english
with open("../data/lang/english.json") as engfile:
    msg_eng = json.load(engfile)

#4.4 setupchannel
with open("../data/usr/setupchannel.json") as setupchannelfile:
    setupchannels = json.load(setupchannelfile)



#5 create bot instance
client = commands.Bot(command_prefix = "§", intents = intents)
client.remove_command('help')



#6 Load specific cogs
@client.command()
async def load(ctx, extension):
    if ctx.message.author.id == 303166734557380608:
        if extension+".py" in os.listdir("./core"):
            client.load_extension(f"core.{extension}")
            await ctx.send(content=None, embed=discord.Embed(title="Command of core was loaded.", description=None, colour=discord.Colour.orange()))
        if extension+".py" in os.listdir("./events"):
            client.load_extension(f"events.{extension}")
            await ctx.send(content=None, embed=discord.Embed(title="Event was loaded.", description=None, colour=discord.Colour.orange()))
        if extension+".py" in os.listdir("./courses"):
            client.load_extension(f"courses.{extension}")
            await ctx.send(content=None, embed=discord.Embed(title="Command of courses was loaded.", description=None, colour=discord.Colour.orange()))



#7 unload specific cogs
@client.command()
async def unload(ctx, extension):
    if ctx.message.author.id == 303166734557380608:
        if extension+".py" in os.listdir("./core"):
            client.unload_extension(f"core.{extension}")
            await ctx.send(content=None, embed=discord.Embed(title="Command of core was unloaded.", description=None, colour=discord.Colour.orange()))
        if extension+".py" in os.listdir("./events"):
            client.unload_extension(f"events.{extension}")
            await ctx.send(content=None, embed=discord.Embed(title="Event was unloaded.", description=None, colour=discord.Colour.orange()))
        if extension+".py" in os.listdir("./courses"):
            client.unload_extension(f"courses.{extension}")
            await ctx.send(content=None, embed=discord.Embed(title="Command of courses was reloaded.", description=None, colour=discord.Colour.orange()))



#8 reload specific cogs
@client.command()
async def reload(ctx, extension):
    if ctx.message.author.id == 303166734557380608:
        if extension+".py" in os.listdir("./core"):
            await ctx.send(content=None, embed=discord.Embed(title="Command of core was reloaded.", description=None, colour=discord.Colour.orange()))
            client.unload_extension(f"core.{extension}")
            client.load_extension(f"core.{extension}")
        if extension+".py" in os.listdir("./events"):
            await ctx.send(content=None, embed=discord.Embed(title="Event was reloaded.", description=None, colour=discord.Colour.orange()))
            client.unload_extension(f"events.{extension}")
            client.load_extension(f"events.{extension}")
        if extension+".py" in os.listdir("./courses"):
            await ctx.send(content=None, embed=discord.Embed(title="Command of courses was reloaded.", description=None, colour=discord.Colour.orange()))
            client.unload_extension(f"courses.{extension}")
            client.load_extension(f"courses.{extension}")



#9 Activating/loading all cogs on startup
for filename in os.listdir("./core"):
    if filename.endswith(".py"):
        client.load_extension(f"core.{filename[:-3]}")
for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        client.load_extension(f"events.{filename[:-3]}")
for filename in os.listdir("./courses"):
    if filename.endswith(".py"):
        client.load_extension(f"courses.{filename[:-3]}")



#10 Token
client.run("Nzg5MTY3OTg1NDQ0NjUxMDA4.X9uH9Q.n3NL-EDNOmtRALd7JmObslLnj-o")
