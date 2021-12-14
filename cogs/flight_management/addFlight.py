# addFlight.py
# Used to add to the upcoming flights
# Author: wHo#6933

import discord
from discord.ext import commands

class AddFlight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["add_flight"])
    @commands.has_role(920289488616448021)
    async def addFlight(self, ctx):
        await ctx.send("Setup Flight")

# Link cog to main bot
def setup(bot):
    bot.add_cog(AddFlight(bot))