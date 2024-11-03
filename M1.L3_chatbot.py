import discord
from discord.ext import commands
from coin import flip_coin

intents = discord.Intents.default()
intents.message_content = True

bsolange = commands.Bot(command_prefix='/', intents=intents)

@bsolange.event
async def on_ready():
    print(f"¡Qué tal! {bsolange.user} ya está en línea!")

@bsolange.command()
async def hola(ctx):
    await ctx.send(f"¡Hola, mucho gusto!, soy {bsolange.user}")

@bsolange.command()
async def bye(ctx):
    await ctx.send("¡Cuídate! 🫶")

@bsolange.command()
async def coin(ctx):
    await ctx.send(flip_coin())
