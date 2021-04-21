# IMPORTES
import discord
import os
from discord.ext import commands

# DEFINE O PREFIXO DO BOT E PERMITE ESCREVER OS COMANDOS COM MAIUSCULAS E MINUSCULAS
client = commands.Bot(command_prefix = '*', case_insensitive=True)

# CARREGA UM COG DA PASTA
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

# DESCAREGA UM COG DA PASTA
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

# CARREGA TODOS OS COGS DENTRO DA PASTA
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# BOT TOKEN
client.run('TOKEN')