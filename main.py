# loading file

import discord
from discord.ext import commands
from discord_components import DiscordComponents

from keep_alive import keep_alive

import os
import termcolor
import json

#bot init and prefixes
def get_prefix(client, ctx):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(ctx.guild.id)]

bot = commands.Bot(
    command_prefix=get_prefix,
    case_insensitive=True
)
bot.remove_command("help")

@bot.event
async def on_ready():
    DiscordComponents(bot)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=";help"))
    print("Bot Initalised :D")

@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = ";"

    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

# Load cogs recursively
# File Structure should follow the form of: ./cogs/folder/code.py
# Where folder is the category of the script
print(termcolor.colored("Loading cogs...", "yellow"))
for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension(f"cogs.{f[:-3]}")
        print(termcolor.colored("Loaded cog: " + f[:-3], "yellow"))
    else:
        for x in os.listdir(f"./cogs/{f}"):
            if x.endswith(".py"):
                bot.load_extension(f"cogs.{f}.{x[:-3]}")
                print(termcolor.colored("Loaded cog: " + x[:-3], "yellow"))
print(termcolor.colored("Cogs loaded :D", "yellow"))

keep_alive()

token = os.getenv("Clove Air Bot Token")
bot.run(token)