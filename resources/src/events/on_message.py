# coding=utf-8

import discord
from discord.ext import commands
import json
import sys
import aiohttp
sys.path.append("../")
import schoolbot as main
from courses import read_courselist



class On_message(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild:
            if not message.content == '§setlanguage':
                if main.langs[str(message.guild.id)]:
                    if main.langs[str(message.guild.id)] == "german":
                        main.lang = main.msg_ger
                    if main.langs[str(message.guild.id)] == "english":
                        main.lang = main.msg_eng
                elif message.content.startswith == main.prefix:
                    await message.channel.send(content=None, embed=discord.Embed(title='Error 001', description='There is no language set up for this guild/server. Please contact the owner of the server, which can set up the language with `*setlanguage`.', colour=discord.Colour.red()))
            if main.custom_prefixes[str(message.guild.id)]:
                main.prefix = main.custom_prefixes[str(message.guild.id)]
            else:
                main.prefix = main.default_prefix
        else:
            await message.channel.send(content=None, embed=discord.Embed(title='Error 002', description='This Bot is not avaiable in direct chats or an unexpected error occured. Please try again on a guild/server.', colour=discord.Colour.red()))
        main.client.command_prefix = main.prefix
        if message.content == "prefix":
            embed = discord.Embed(title="The prefix of this server is ``"+prefix+"``.", colour=discord.Colour.blue())
            await message.channel.send(content=None, embed=embed)
        if message.channel.id == main.setupchannels[str(message.guild.id)]:
            # IMPORTANT: if is ignored
            print(message.channel.id)
            if message.attachments:
                if "courselist.json" == message.attachments[0].filename:
                    print(2)
                    async with aiohttp.ClientSession() as session:
                        async with session.get(message.attachments[0].url) as r:
                            file = await r.json()
                            read_courselist.read(message, file)



def setup(client):
    client.add_cog(On_message(client))
