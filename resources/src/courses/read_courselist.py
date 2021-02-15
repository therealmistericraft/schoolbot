# coding=utf-8

import discord
from discord.ext import commands
import json
import sys
sys.path.append("../")
import schoolbot as main

def read(message, list):
    try:
        file = open(f".../data/usr/courselists/{message.guild.id}.json", "x")
    else:
        #TODO: How to send File without await/async, file does not get overwritten if exists
        message.channel.send(content=None, embed=discord.Embed(title=main.lang["3"], colour=discord.Colour.red()))
        message.channel.send(discord.File(f".../data/usr/courselists/{message.guild.id}.json"))
    # IMPORTANT: no such file or directory (maybe, the folder has to exist)
    content = json.load(list)
    json.dump(content, file, indent=4)


# Because this is in courses folder, which contains discord cogs, we have to make it a cog even it isn´t
class Placeholder(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Placeholder(client))
