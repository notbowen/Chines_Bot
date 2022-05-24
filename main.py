# Bot that sends chinese words in a predefined channel
# Per 1 hour?

# Libraries
import discord
from discord.ext import commands

import os

from keep_alive import keep_alive

# Bot setup
bot = commands.Bot(command_prefix=["c"], case_insensitive=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name="chelp"))
    print("Bot initialised :D")

# Start the "server"
keep_alive()

# Run the bot
token = os.getenv("BOT_TOKEN")
bot.run(token)
