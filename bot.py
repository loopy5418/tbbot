import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.sync_commands()  # Global sync

# SLASH COMMAND
@bot.slash_command(name="hello", description="Say hello to the bot!")
async def hello(ctx):
    await ctx.respond("Hello there!")

# MESSAGE CONTEXT MENU COMMAND
@bot.user_command(name="Inspect Message")
async def inspect_message(ctx, message: discord.Message):
    # Button definition
    class InspectButton(discord.ui.View):
        @discord.ui.button(label="Details", style=discord.ButtonStyle.primary)
        async def button_callback(self, button, interaction):
            await interaction.response.send_message(f"Message content: `{message.content}`", ephemeral=True)

    await ctx.respond("Choose an action:", view=InspectButton(), ephemeral=True)

bot.run(os.environ.get("DISCORD_BOT_TOKEN"))
