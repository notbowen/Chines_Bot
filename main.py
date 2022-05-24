# Bot that sends chinese words in a predefined channel
# Per 1 hour?

# Libraries
import random

import discord
from discord.ext import commands
from discord.ext import tasks

import os
import io

from keep_alive import keep_alive

# Variables
channel_id = 978653634487275530
minutes = 5

api_url = "https://m.dict.cn/hanyu/search.php?q="

# Bot setup
bot = commands.Bot(command_prefix=["c"], case_insensitive=True)
bot.remove_command("help")

# Load chinese words
with io.open("word_list.txt", encoding="utf-8") as f:
    words_unclean = f.readlines()
    f.close()

# Clean up wordlist
words_unclean = [x.replace("\n", "") for x in words_unclean]
words_unclean = [x.split(",") for x in words_unclean]

words = []
for lst in words_unclean:
    for word in lst:
        words.append(word)


# Send a random word per n minutes
# tasks.loop(minutes=minutes)
@tasks.loop(minutes=minutes)
async def send_word():
    channel = bot.get_channel(channel_id)
    word_chosen = random.choice(words)
    await channel.send(f"Word: {word_chosen}\nMeaning n stuff: {api_url + word_chosen}")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="chelp"))
    print("Bot initialised :D")

    send_word.start()


# Start the "server"
keep_alive()

# Run the bot
# token = os.getenv("BOT_TOKEN")
token = "OTc4NjQ1OTM3NTU3NzM3NTAy.GPr0ux.qXnQt4qImCrt8FrK7_iLCZk_oUQJvR9vee1NfA"
bot.run(token)
