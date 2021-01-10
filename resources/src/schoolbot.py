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


#5 create bot instance
client = commands.Bot(command_prefix = "§", intents = intents)
client.remove_command('help')





#6 Events

#6.1 on_message
"""
@client.event
async def on_message(message):
    global default_prefix
    global prefix
    global custom_prefixes
    global client
    global lang
    global langs
    global msg_ger
    global msg_eng
    if message.guild:
        if not message.content == '§setlanguage':
            if langs[str(message.guild.id)]:
                if langs[str(message.guild.id)] == "german":
                    lang = msg_ger
                if langs[str(message.guild.id)] == "english":
                    lang = msg_eng
            elif message.content.startswith == prefix:
                await message.channel.send(content=None, embed=discord.Embed(title='Error 001', description='There is no language set up for this guild/server. Please contact the owner of the server, which can set up the language with `*setlanguage`.', colour=discord.Colour.red()))
            else:
                print("Es wird nicht erkannt, dass eine sprache aufgesetzt wurde")
        if custom_prefixes[str(message.guild.id)]:
            prefix = custom_prefixes[str(message.guild.id)]
        else:
            prefix = default_prefix
    else:
        await message.channel.send(content=None, embed=discord.Embed(title='Error 002', description='This Bot is not avaiable in direct chats or an unexpected error occured. Please try again on a guild/server.', colour=discord.Colour.red()))
    client.command_prefix = prefix
    if message.content == "prefix":
        embed = discord.Embed(title="Das Prefix dieses Servers ist ``"+prefix+"``.", colour=discord.Colour.blue())
        await message.channel.send(content=None, embed=embed)
    await client.process_commands(message)
"""



# Load specific cogs
@client.command()
async def load(ctx, extension):
    if extension+".py" in os.listdir("./core"):
        client.load_extension(f"core.{extension}")
    if extension+".py" in os.listdir("./events"):
        client.load_extension(f"events.{extension}")

# Unload specific cogs
@client.command()
async def unload(ctx, extension):
    if extension+".py" in os.listdir("./core"):
        client.unload_extension(f"core.{extension}")
    if extension+".py" in os.listdir("./events"):
        client.unload_extension(f"events.{extension}")


# Activating/loading all cogs on startup
for filename in os.listdir("./core"):
    if filename.endswith(".py"):
        client.load_extension(f"core.{filename[:-3]}")
for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        client.load_extension(f"events.{filename[:-3]}")


#9 Token

client.run("Nzg5MTY3OTg1NDQ0NjUxMDA4.X9uH9Q.R9ESlVGDymMgGCr1kLLsVY8jeik")
