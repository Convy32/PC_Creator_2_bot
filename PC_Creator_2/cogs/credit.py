import discord
from discord.ext import commands

class credit(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="credits")
    async def credit(self, ctx):
        embed = discord.Embed(title="Credits", color=13565696)
        embed.add_field(name="Bot Owner/Developer", value="<@695229647021015040>", inline=False)
        embed.add_field(name="Bot Developer", value="<@713696771188195368>", inline=False)
        embed.add_field(name=",scores sheets", value="<@695229647021015040>, \n<@713696771188195368>")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(credit(client))