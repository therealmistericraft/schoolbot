# coding=utf-8

import discord
from discord.ext import commands
import json
import sys
sys.path.append("../")
import schoolbot as main



class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['changeprefix', 'cp', 'prefix'])
    async def setprefix(self, ctx, pPrefix):
        main.custom_prefixes[str(ctx.guild.id)] = pPrefix
        with open("../data/usr/prefix.json", "w") as prefixfile:
            json.dump(main.custom_prefixes, prefixfile, indent=4)
        await ctx.send("Your prefix is now `"+main.custom_prefixes[str(ctx.guild.id)]+"`")



def setup(client):
    client.add_cog(Prefix(client))
