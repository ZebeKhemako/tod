import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Apasih sok asik lu")

client.run('MTE3MTY2Mjk0MzA3NTcxNzIyMQ.GUTurA.ZPEskjS4VfmyVoNriCRHgpehfIgCGQdemSNSQw')
