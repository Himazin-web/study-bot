import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"起動しました: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(os.environ["DISCORD_TOKEN"])
