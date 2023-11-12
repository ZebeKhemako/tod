import discord
from discord.ext import commands
import os
import openai

# Inisialisasi bot
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# Masukkan API Key GPT-3 Anda
openai.api_key = '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'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def gpt3(ctx, *, input_text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=2000  # Jumlah token maksimal dalam respons GPT-3
    )
    bot_response = response.choices[0].text
    await ctx.send(bot_response)

# Token bot Discord Anda
bot_token = 'MTE3MTc0NTY3Njg0MTk3OTkyNA.G-I9o9.0emcXyTKRkp_F0tnjCqTvZ2iwv5f7Tqef0HMAI'

# Jalankan bot
bot.run(bot_token)

