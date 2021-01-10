import discord
from discord.ext import commands

class On_ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready")

def setup(client):
    client.add_cog(On_ready(client))
