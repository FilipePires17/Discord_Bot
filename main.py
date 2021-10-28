import discord
import os
import requests
import json
from keep_alive import keep_alive

bot_token = os.environ['BOT_TOKEN']
tenor_key = os.environ['TENOR_API']

# set the apikey and limit
apikey = tenor_key  # test value
lmt = 1

# our test search
search_term_dia         = 'bom dia valtatui'
search_term_noite       = 'boa noite valtatui'
search_term_valtatui    = 'valtatui'
search_term_gretchen    = 'gretchen'
search_term_yours       = 'myme yours'
search_term_hikaru      = 'ezaki hikaru'

gif_list = []

# get random results using default locale of EN_US
def gets_gif_url(search_term):
    r = requests.get(
        "https://g.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        gifs = json.loads(r.content)
        gif_url  = gifs['results'][0]['media'][0]['gif']['url']
        return gif_url
    else:
        gifs = None

class MyClient(discord.Client):
    async def on_ready(self):
        print('Hello world {0.user}'.format(client))

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content.startswith('buenos'):
            gif_url = gets_gif_url(search_term_dia)
            await message.channel.send(gif_url)
        
        if message.content.startswith('buenas'):
            gif_url = gets_gif_url(search_term_noite)
            await message.channel.send(gif_url)

        if message.content.startswith('valtatui'):
            gif_url = gets_gif_url(search_term_valtatui)
            await message.channel.send(gif_url)

        if message.content.startswith('gretchen'):
            gif_url = gets_gif_url(search_term_gretchen)
            await message.channel.send(gif_url)
        
        if message.content.startswith('yours'):
            gif_url = gets_gif_url(search_term_yours)
            await message.channel.send(gif_url)

        if message.content.startswith('hikaru'):
            gif_url = gets_gif_url(search_term_hikaru)
            await message.channel.send(gif_url)
        
        if message.content.startswith('?'):
            search_aux = message.content.split(' ')
            search_term = search_aux[0][1:]
            search_aux.pop(0)
            for term in search_aux:
                search_term += ' ' + term
            gif_url = gets_gif_url(search_term) #search_term)
            await message.channel.send(gif_url)

client = MyClient()
keep_alive()
client.run(bot_token)