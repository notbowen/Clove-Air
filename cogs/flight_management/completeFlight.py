# completeFlight.py
# Used to delete flight from upcoming flights list
# Author: wHo#6933

import discord
from discord.ext import commands

class Completeflight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Completeflight(bot))
