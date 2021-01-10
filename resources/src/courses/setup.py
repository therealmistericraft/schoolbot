# coding=utf-8

import discord
from discord.ext import commands
import json
import sys
sys.path.append("../")
import schoolbot as main



class Setup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setup(self, ctx):
        channel = await ctx.message.guild.create_text_channel("schoolbot-setup")
        await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
        await channel.set_permissions(ctx.message.author, attach_files=True, send_messages=True, read_messages=True)
        await channel.set_permissions(ctx.guild.me, read_messages=True)
        embed = discord.Embed(title = main.lang["2"],
            description = main.lang["3"]+"\n"+main.lang["4"],
            colour = discord.Colour.orange())
        await ctx.send(content=None, embed=embed)
        embed2 = discord.Embed(title = None,
            description = main.lang["5"]+"\n"+main.lang["6"]+"\n"+main.lang["7"],
            colour = discord.Colour.orange())
        await ctx.send(content=None, embed=embed2)



def setup(client):
    client.add_cog(Setup(client))
