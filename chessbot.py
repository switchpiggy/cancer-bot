import discord
import logging
import requests
from datetime import datetime

cli = discord.Client()
intents = discord.Intents.default()

command_key = ';'

key = 'Nzk3NjgzNjUzNjIyNjI4Mzcy.X_qCyw.EWgWJkNNF2vZoTMpOXXQ0mKvLNs'

logging.basicConfig(level=logging.INFO)

async def process_get_error(code, message):
    if code == 400:
        await message.channel.send("ERROR 400: Bad request.")
    if code == 401:
        await message.channel.send("ERROR 401: Authentication needed.")
    if code == 403:
        await message.channel.send("ERROR 403: Trying to access forbidden resource.")
    if code == 404:
        await message.channel.send("ERROR 404: Resource not found on server.")
    if code == 503:
        await message.channel.send("ERROR 503: Server not ready to handle request.")

    return

async def process_account(data, message):
    if data.status_code != 200:
        await process_get_error(data.status_code, message)
        return

    a = data.json()
    res = "User **" + a['username'] + "** found with name\n> " + a.get('name', "Unregistered") + '\n' + "> **Last Online:** " + str(datetime.fromtimestamp(a['last_online'])) + '\n> **FIDE Rating:** ' + str(a.get('fide', 'Unrated'))
    res2 = "\n> **Location: ** " + a.get('location', 'N/A')
    await message.channel.send(res + res2)
    

@cli.event
async def on_ready():
    print("Fuck python")

@cli.event
async def on_message(message):
    if not message.content.startswith(command_key):
        return

    if message.content.startswith(command_key + 'get'):
        args = message.content.split()
        for name in args:
            if name.startswith(command_key):
                continue

            data = requests.get('https://api.chess.com/pub/player/' + name)
            await process_account(data, message)

    
cli.run(key)