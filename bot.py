import discord
import logging

logging.basicConfig(level=logging.INFO)

cli = discord.Client()
intents = discord.Intents.default()

p_channels = [797634311905738783, 797634937594708038, 797635544255168522, 797635705755926538, 
797636051836993546, 797637409458094140, 797637561992085514, 797637707597742095,
797637802182574110, 797637926397673472, 797688928865091625]

new_messages = []

key = 'foobar' 

#async def process_command(command):


@cli.event
async def on_ready():
    print('Fuck python {0.user}'.format(cli))

@cli.event
async def on_message(message):
    if message.author == cli.user:
        return
    if message.channel.id == 796911223668998144 && message.content.startswith("> "):
            await message.add_reaction('\U0001F595')
            await message.add_reaction('\u2611')
    if message.channel.id == 796911223668998144 && message.content.startswith("sendit"):
        for i in new_messages:
            await cli.get_channel(796911346817957939).send(i)
        new_messages = []
    if message.channel.id == 796911223668998144 && message.content.startswith("clear"):
        new_message = []
    
    if message.content.startswith("miku"):
        await message.channel.send('kawaiiiiiiiiiii')
    new_message = '> ' + message.content + '\n -' + message.author.mention
    for i in p_channels:
        if i == message.channel.id:
            await cli.get_channel(796911223668998144).send(new_message)
            #await message.delete()
            return

@cli.event
async def on_reaction_add(reaction, user):
    if user == cli.user:
        return
    
    message = reaction.message
    roles = user.roles
    if message.channel.id != 796911223668998144:
        return
    
    ok = 0
    for i in roles:
        if i.name == 'Officer':
            ok = 1
            break
    if ok == 0: 
        return

    #new_message = message.author.display_name + ' said:\n' + message.content

    if(reaction.emoji == '\u2611'):
        new_messages.append(message.content)
        await cli.get_channel(796911223668998144).send("Current Queue:")
        for i in new_messages:
            await cli.get_channel(796911223668998144).send(i)
         #copy this to the send messages function
         #await message.delete()
    elif (reaction.emoji == '\U0001F595'): 
        await message.delete()


    
    
    


cli.run(key)
