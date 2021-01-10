# coding=utf-8

import discord
from discord.ext import commands



class On_guild_join(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        owner = guild.owner
        await owner.send(content=None, embed=discord.Embed(title="Thanks for adding schoolbot to your Server!", description="To get started, you have to set up your language. Before this, nothing will work.", colour=discord.Colour.orange()).add_field(name="Start", value="Type `§setlanguage` followed by your language in small letters (e.g. `§setlanguage german`) in a channel the Bot is allowed to read and write in.", inline=False).add_field(name="Troubleshooting", value="I am a junior developer and do not know everything, so the language choice is not reliable nor stable. Please contact me by sending a private message to the bot."))



def setup(client):
    client.add_cog(On_guild_join(client))
