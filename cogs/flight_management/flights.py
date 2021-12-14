# flights.py
# Used to list upcoming flights
# Author: wHo#6933

import discord
from discord.ext import commands

class Flights(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Flights(bot))
