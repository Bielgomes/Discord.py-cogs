# IMPORTES
import discord
from discord.ext import commands

# CLASSE HELLO
class Hello(commands.Cog):

    # INICIALIZA O COG
    def __init__(self, client):
        self.client = client

    # EVENTOS
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot online")

    # COMANDOS
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Olá, Cogs funcionando!")

# ADICIONA O COG
def setup(client):
    client.add_cog(Hello(client))