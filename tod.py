import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

truth_questions = [
    "If you could have any superpower, what would it be?",
    "What is the most embarrassing thing you've ever done?",
    "If you could be any animal, what would you be?",
    "If you could go anywhere in the world for free, where would you go?",
    "If you could meet any historical figure, who would it be?",
    "If you could be any character from a movie or TV show, who would you be?",
]

dare_questions = [
    "Act out the last scene of your favorite movie.",
    "Eat a raw piece of garlic.",
    "Dance with all the people around you, even if you don't know them.",
    "Shout the first word that comes to your mind.",
    "Yell out a random fact.",
    "Sing a song out loud, even if you're not singing well.",
]

questions = truth_questions + dare_questions

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def tod(ctx, choice):
    await ctx.send(random.choice(questions))

bot.run('MTE3MTgzNDMzNTQyNzU4MDEyNQ.GglG1u.t9-Ecg0qRpGj5zL5YTD4pOg93pTecvkQb5yhZA')