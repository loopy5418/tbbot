import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(name="hello", description="Say hello to the bot!", guild_ids=None)
async def hello(ctx):
    await ctx.respond("Hello there!")

@bot.message_command(name="Inspect Message")
async def inspect_message(ctx, message: discord.Message):
    await ctx.respond(f"Message content: {message.content}")

bot.run(os.environ.get("DISCORD_BOT_TOKEN"))
