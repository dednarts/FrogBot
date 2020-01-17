import discord
from discord.ext import commands
import random
import os


TOKEN = "token"

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx, number):                                                  #this function will respond pong with however many times you tell it to
    print(f'someone has pinged {number}')
    if number == None:
        number = 1
    await ctx.send('pong ' * int(number))

@bot.command()
async def ding(ctx):
    await ctx.send('dong ')


@bot.command()
async def pepeLINK(channel):                                                   #this function sends the link of the picture
    file_path = 'path to picture folder'
    picture_names = os.listdir(file_path)                                      #here we create a list containing all the names of the pictures
    selected_picture = 'https://i.imgur.com/' + random.choice(picture_names)   #python is a language of LOGIC
    await channel.send(selected_picture)

@bot.command()
async def pepe(ctx):                                                           #this function
    file_path = 'path to picture folder'
    picture_names = os.listdir(file_path)
    await ctx.send(file=discord.File(file_path + random.choice(picture_names)))


@bot.command()
async def be(ctx):
    await ctx.send(">me")

@bot.event
async def on_ready():
    print('%s %s is online' % (bot.user.name,bot.user.id))  



bot.run(TOKEN)
