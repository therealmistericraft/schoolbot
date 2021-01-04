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
        #langfile: file the choice of language is stored in
        #langs: dict of choosen languages in relation to guild id
        #gerfile: file the messages in german language are stored in
        #engfile: file the messages in english language are stored in
        #msg_ger: dict of messages in german
        #msg_eng: dict of messages in english

#0.3 Messages
    #lang[0]: helpembed page "setup" title
    #lang[1]: helpembed page "assignments" title


#1 imports
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from time import sleep
import threading
import json
import ast

#2 settings

#2.1 Activate Intents from API
intents = discord.Intents.all()

#3 instance variables
prefix = ""
lang = ""
custom_prefixes = {}

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
@client.event
async def on_message(message):
    global default_prefix
    global prefix
    global custom_prefixes
    global client
    if message.guild:
        if not message.content == '§setlanguage':
            if langs.get(message.guild.id):
                if langs.get(message.guild.id) == "german":
                    lang = msg_ger
                if langs.get(message.guild.id) == "english":
                    lang = msg_eng
            elif message.content.startswith == prefix:
                await message.channel.send(content=None, embed=discord.Embed(title='Error 001', description='There is no language set up for this guild/server. Please contact server owner, which can set up the language with `*setlanguage`.', colour=discord.Colour.red()))
        if custom_prefixes.get(message.guild.id):
            prefix = custom_prefixes.get(message.guild.id)
        else:
            prefix = default_prefix
    else:
        await message.channel.send(content=None, embed=discord.Embed(title='Error 002', description='This Bot is not avaiable in direct chats or an unexpected error occured. Please try again on a guild/server.', colour=discord.Colour.red()))
    client.command_prefix = prefix
    if message.content == "prefix":
        embed = discord.Embed(title="Das Prefix dieses Servers ist ``"+prefix+"``.", colour=discord.Colour.blue())
        await message.channel.send(content=None, embed=embed)
    await client.process_commands(message)

#6.2 on_guild_join: Send tutorial to guild owner how to set up the bot
@client.event
async def on_guild_join(guild):
    owner = guild.owner
    await owner.send(content=None, embed=discord.Embed(title="Thanks for adding schoolbot to your Server!", description="To get started, you have to set up your language. Before this, nothing will work.", colour=discord.Colour.orange()).addfield(name="Start", value="Type `§setlanguage` followed by your language in small letters (e.g. `§setlanguage german`) in a channel the Bot is allowed to read and write in.", inline=False).addfield(name="Trubleshooting", value="I am a junior developer and do not know everything, so the language choice is not reliable nor stable. Please contact me by sending a private message to the bot."))
    #TODO: Send guild owner message which tells him how to set up the language




#7 Command methods

#7.





#8 Commands

#8.1 setlanguage
@client.command()
async def setlanguage(ctx, pLanguage):
    if pLanguage == "german" or pLanguage == "english":
        langs[ctx.guild.id] = pLanguage
        await ctx.send("Language has been set up successfully!")
    else:
        await ctx.send("Your language is not available. Availavle languages are: `german`, `english`")

@client.command()
async def test(ctx):
    await ctx.send(lang[0])





#9 Token

client.run("YOUR TOKEN HERE")
