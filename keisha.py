import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

@client.command()
async def play(ctx, choice):
    choices = ['batu', 'kertas', 'gunting']
    bot_choice = random.choice(choices)

    if choice.lower() in choices:
        if choice.lower() == bot_choice:
            result = f"It's a tie because the bot chose {bot_choice}."
        elif (
            (choice.lower() == 'batu' and bot_choice == 'gunting')
            or (choice.lower() == 'gunting' and bot_choice == 'kertas')
            or (choice.lower() == 'kertas' and bot_choice == 'batu')
        ):
            result = f"You win! Bot chose {bot_choice}."
        else:
            result = f"Bot wins! Bot chose {bot_choice}."
    else:
        result = "Invalid choice. Please choose 'batu', 'gunting', or 'kertas'."

    await ctx.send(result)

client.run('MTE3MTY5MjAxNzU5Njc4MDYxNQ.GpLDoJ.xqx2cPn7U14EkBROLOXcRFEPIs8Upm8-HIR-pY')


