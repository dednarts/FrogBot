import discord
import os 
import random

TOKEN = 'your token'

client = discord.Client()



@client.event
async def on_message(message):  #the functions that we make
    
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!gibPepeAlbum'):
        await message.channel.send('https://imgur.com/gallery/SU4Qa') #the gift that keeps on giving

    if message.content.startswith('!reeee'):
        await message.channel.send('REEEEEEEEEEEEEEEEEEEEEEEEEE')

    if message.content.startswith('!pepe'):
        file_path = 'path to folder'
        picture_names = os.listdir(file_path)
        selected_picture = 'https://i.imgur.com/' + random.choice(picture_names)   #python is a language of LOGIC
        await message.channel.send(selected_picture)



@client.event 
async def on_ready():
    print('Bot')
    print(client.user.name)
    print(client.user.id)
    print('Is Active')

client.run(TOKEN)
