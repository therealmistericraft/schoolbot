import discord
from discord.ext import commands
import json
import sys
sys.path.append("../")
import schoolbot as main

class Language(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['changelanguage', 'cl', 'language'])
    async def setlanguage(self, ctx, pLanguage):
        if pLanguage == "german" or pLanguage == "english":
            main.langs[str(ctx.guild.id)] = pLanguage
            with open("../data/usr/lang.json", "w") as langfile:
                json.dump(main.langs, langfile, indent=4)
            await ctx.send("Language has been set up successfully! Your language: `"+pLanguage+"`")
        else:
            await ctx.send("Your language is not available. Available languages are: `german`, `english`")

def setup(client):
    client.add_cog(Language(client))
