import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from discord.ext.commands import MissingPermissions
import asyncio

intents = discord.Intents().all()
client = commands.Bot(command_prefix= 'V',case_insensitive=True, help_command=None, intents=intents)

@client.event
async def on_ready():
    print(f"Logged into bot")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="all Verifications"))

async def main():
    keep_alive()
    await client.load_extension('Cogs.verify')
    await client.start(os.getenv("BOT_TOKEN"))

asyncio.run(main())