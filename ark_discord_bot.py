import subprocess
import discord
from discord.ext import commands

TOKEN = '$YOURSERVERTOKEN'
## Channel ID des Command Channels
cmd_channel = 493025939375259650
## Role ID of Bot Moderator
mod_roleid = 467951488442957825

client = discord.Client()

@client.event
async def on_message(message):
    author = message.author
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        if (message.channel.id == cmd_channel):
            await message.channel.send('```css\n I heard you! {0.name}```\n'.format(author))

## Send available Commands
    if message.content.startswith('!help'):
        if (message.channel.id == cmd_channel):
            await message.channel.send('Type:\n**!roles** - zeigt deine Discord Rollen an\n**!arkstatus** - zeigt den Status des vdvnet ARK Servers an\n**!arkrestart** - fuehrt einen FAST Restart des Servers durch\n**!arkmsg [Nachricht]** - Schickt den Text direkt als Servernachricht an den vdvnet ARK Server\n**!arkchat [Nachricht]** - Schickt den Text direkt in den ARK Global Ingame Chat'.format(author))

## Was just a Test
#    if message.content.startswith('!roles'):
#        role_id = [role.id for role in author.roles]
#        role_name = [role.name for role in author.roles]
#        await message.channel.send('Rollen:' + str(role_id))
#        await message.channel.send('Rollen:' + str(role_name))

## Sending Message into ARK Ingame Chat

    if message.content.startswith('!arkchat'):
        if (message.channel.id == cmd_channel):
            role_id = [role.id for role in author.roles]
            if mod_roleid in role_id:
                usr_msg = message.content
                formated_usr_msg = "vdvnet Discord: " + usr_msg[8:]
                print(usr_msg[8:])

                result = subprocess.run(['/usr/local/bin/arkmanager', 'rconcmd', 'serverchat', formated_usr_msg], stdout=subprocess.PIPE)
                formated_result = result.stdout.decode('utf-8').replace('[0;39m','')
                formated_result = formated_result.replace('[1;32m','')
                formated_result = formated_result.replace('','')
                print(formated_result)
                await message.channel.send(formated_result)
            else:
                await message.channel.send('You dont have permission to do that {0.name}'.format(author))

## Sending Message as ARK Servermessage
    if message.content.startswith('!arkmsg'):
        if (message.channel.id == cmd_channel):
            role_id = [role.id for role in author.roles]
            if mod_roleid in role_id:
                usr_msg = message.content
                formated_usr_msg = "vdvnet Discord: " + usr_msg[8:]
                print(usr_msg[8:])

                result = subprocess.run(['/usr/local/bin/arkmanager', 'broadcast', formated_usr_msg], stdout=subprocess.PIPE)
                formated_result = result.stdout.decode('utf-8').replace('[0;39m','')
                formated_result = formated_result.replace('[1;32m','')
                formated_result = formated_result.replace('','')
                print(formated_result)
                await message.channel.send(formated_result)
            else:
                await message.channel.send('You dont have permission to do that {0.name}'.format(author))


## Getting ARK Server Status
    if message.content.startswith('!arkstatus'):
        if (message.channel.id == cmd_channel):
            role_id = [role.id for role in author.roles]
            if mod_roleid in role_id:

                result = subprocess.run(['/usr/local/bin/arkmanager', 'status'], stdout=subprocess.PIPE)
                formated_result = result.stdout.decode('utf-8').replace('[0;39m','')
                formated_result = formated_result.replace('[1;32m','')
                formated_result = formated_result.replace('','')
                print(formated_result)
                await message.channel.send(formated_result)
            else:
                await message.channel.send('You dont have permission to do that {0.name}'.format(author))

## Trigger ARK Restart Script 
    if message.content.startswith('!arkrestart'):
        if (message.channel.id == cmd_channel):
            role_id = [role.id for role in author.roles]
            if mod_roleid in role_id:

                result = subprocess.run(['/home/steam/ARKFiles/scripte/fast-restart.sh'], stdout=subprocess.PIPE)
                formated_result = result.stdout.decode('utf-8').replace('[0;39m','')
                formated_result = formated_result.replace('[1m;32m','')
                formated_result = formated_result.replace('','')
                print(formated_result)
                await message.channel.send(formated_result)
            else:
                await message.channel.send('You dont have permission to do that {0.name}'.format(author))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
