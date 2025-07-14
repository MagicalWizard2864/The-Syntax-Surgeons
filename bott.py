import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

# Example command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run('MTM4MjA1MDE2OTEzODQ0NjM0Ng.GFAIgp.9FMGfrRkfuAXFfCNdYUdPE67HshXw7xnwcYL6E')  # Replace with your own token
