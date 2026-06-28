import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import botcontroller
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def initialise(ctx, user_id: str):
    botcontroller.add_member(user_id, "unknown")










bot.run(os.getenv('DISCORD_TOKEN'))