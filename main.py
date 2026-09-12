import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

async def load():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"commands.{filename[:-3]}")
    for filename in os.listdir("./events"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"events.{filename[:-3]}")

@bot.event
async def setup_hook():
    await load()

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("DISCORD_TOKEN not found in .env!")
    else:
        bot.run(token)
