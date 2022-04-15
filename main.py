import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from discord.ext.commands import MissingPermissions


intents = discord.Intents().all()
client = commands.Bot(command_prefix= 'V',case_insensitive=True, help_command=None, intents=intents)

@client.event
async def on_ready():
    print(f"Logged into bot")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="all Verifications"))
    await client.load_extension('Cogs.verify')


if __name__ == "__main__":
    keep_alive()
client.run(os.getenv("BOT_TOKEN"))