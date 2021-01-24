# coding=utf-8

import discord
from discord.ext import commands
import json

def read(message, list):
    file = open(f".../data/usr/courselists/{message.guild.id}.json", "w+")
    # IMPORTANT: no such file or directory (maybe, the folder has to exist)
    content = json.load(list)
    json.dump(content, file, indent=4)


# Because this is in courses folder, which contains discord cogs, we have to make it a cog even it isn´t
class Placeholder(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Placeholder(client))
