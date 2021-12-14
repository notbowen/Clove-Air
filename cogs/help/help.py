# help.py
# Shows all the functions of the bot
# Author: wHo#6933

import discord
from discord.ext import commands

from functions import generateRandomColor

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help", color=await generateRandomColor())
        embed.set_footer(text="Clove Air", icon_url="https://cdn.discordapp.com/attachments/920180147850723339/920295776469528586/logo.jpg")
        embed.add_field(name="Help", value="Shows this embed.", inline=False)

        await ctx.send(embed=embed)

# Link cog to main bot
def setup(bot):
    bot.add_cog(HelpCommand(bot))