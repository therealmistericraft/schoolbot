# coding=utf-8

#0 Documentation
#0.1 Threading usage
# Only use threading.Thread, if time.sleep is in the code snippet to use less performance

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
intents = discord.Intent.defaults()
intents.members = True
intents.reactions = True

#3 instance variables
prefix = ""
lang = ""

#4 initalizing

#4.1 prefix
prefixfile = open('prefix.txt', 'r')
data = prefixfile.read()
data = data.split('\n')
custom_prefixes = data[0]
custom_prefixes = ast.literal_eval(custom_prefixes)
default_prefix = '%'
prefixfile.close()

#5 create bot instance
client = commands.Bot(command_prefix = "%")
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
        if not message.content == '*setlanguage'
            if language.get(message.guild.id):
                lang = language.get(message.guild.id)
            elif message.content.startswith == prefix:
                await message.channel.send(content=None, embed=discord.Embed(title='Error 002', description='There is no language set up for this guild/server. Please contact server owner, which can set up the language with `*setlanguage`.', colour=discord.Colour.red()))
        if custom_prefixes.get(message.guild.id):
            prefix = custom_prefixes.get(message.guild.id)
        else:
            prefix = default_prefix
    else:
        await message.channel.send(content=None, embed=discord.Embed(title='Error 003', description='This Bot is not avaiable in direct chats or an unexpected error occured. Please try again on a guild/server.', colour=discord.Colour.red()))
    client.command_prefix = prefix
    if message.content == "prefix":
        embed = discord.Embed(title="Das Prefix dieses Servers ist ``"+prefix+"``.", colour=discord.Colour.blue())
        await message.channel.send(content=None, embed=embed)
    await client.process_commands(message)

#6.2 on_guild_join: Send tutorial to guild owner how to set up the bot
@client.event
async def on_guild_join(guild):
    owner = guild.owner
    await owner.send(content=None, embed=discord.Embed(title="Thanks for adding schoolbot to your Server!", description="To get started, you have to set up your language. Before this, nothing will work.", colour=discord.Colour.orange()).addfield(name="1. Start", value="Type `*setlanguage` in a channel the Bot is allowed to read and write in.", inline=False).addfield(name="2. Choose your language", value="You see every language the bot can speak. React with the language you want by clicking on the flag.", inline=False).addfield(name="Trubleshooting", value="I am a junior developer and do not know everything, so the language choice is not reliable nor stable. Please contact me by sending a private message to the bot."))
    #TODO: Send guild owner message which tells him how to set up the language




#7 Command methods

#7.1 set language
def mSetlanguage(ctx, language):
    successful = False
    if language == german:
        file = open("german.txt", "r")
        successful = True
    elif language == english:
        file = open("english.txt", "r")
        successful = True
    else:
        await ctx.send("Your language is not available. Availavle languages are: `german`, `english`")
    if successful == True:
        data = file.read()
        data = data.split("\n")
        for i in data:
            while "//n" in i:
                i.replace("//n", "\n")

                #TODO: This belongs to on_message





#8 Commands

#8.1 setlanguage
@client.command()
async def setlanguage(ctx, language):
    t = threading.Thread(target = mSetlanguage, args = (ctx, language))
    t.start()
    #TODO: Do not use threading here
