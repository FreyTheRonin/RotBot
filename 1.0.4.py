import discord
import asyncio
import random
import pickle
import os
import codecs
import string

client = discord.Client()

#Copy your bot user's token here.
token = ''

hp = discord.Embed(title='How To Use', description='**Commands**\n        ' +
                   'These commands DM the user the resultant encoded or decoded message.\n        ' +
                   '**.rl** to translate the last message in the channel (that is not a .rl command).\n        ' +
                   '**.rl n** to translate the last n messages in the channel, up to fifty.\n\n' +
                   'If somebody posts a rot\'d message in chat and you want to know what it says, use **.rl** to get a decoded version DM\'d to you. ' +
                   'If other people have talked since the message was posted,' +
                   ' use .**rl n** with a high enough value to reach the message you want to decode.\n\nIf you want to encode a message yourself,' +
                   ' simply DM me anything and I\'ll reply with an encoded version which you can copy and paste into the channel.\n\n' +
                   'If you want to reduce chat clutter, give me Manage Messages permissions and I\'ll delete any **.rl** commands issued in text channels.\n\n' +
                   'If anything is working incorrectly, DM Frey#1251.', colour=0xFF0022)

	
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name = '.rhelp for help'))
	
@client.event
async def on_message(message):
        if not message.author.bot:
                if message.channel.is_private:
                        if not message.content.lower().startswith('.rhelp'):
                                await client.send_message(message.author, codecs.encode(message.content, 'rot_13'))

                        else:
                                await client.send_message(message.channel, embed=hp)
                else:
                        if message.content.lower().startswith('.rhelp'):
                                await client.send_message(message.channel, embed=hp)
                        
                        if message.content.lower() == '.rl':
                                flag = False
                                async for msg in client.logs_from(message.channel, limit=100, before=message):
                                        if not (msg.content.lower().startswith('.rl')) and not flag:
                                                await client.send_message(message.author, codecs.encode(msg.content, 'rot_13'))
                                                flag = True
                                await client.delete_message(message)
                
                        if message.content.lower().startswith('.rl '):
                                rot = ''
                                n = 1;
                                t, i = message.content.split(' ')
                                n = int(float(i))
                                if n > 50:
                                        await client.send_message(message.channel, 'Limit of 50 Messages')
                                        n = 50
                                async for msg in client.logs_from(message.channel, limit=n, before=message, reverse=True):
                                        rot += codecs.encode(msg.content, 'rot_13') + '\n\n'
                                await client.send_message(message.author, rot)
                                await client.delete_message(message)

                        if message.content.lower() == '.rot':
                                await client.send_message(message.channel, 'No argument given.')
                                await client.delete_message(message)

                        if message.content.lower().startswith('.rot '):
                                await client.send_message(message.author, codecs.encode(message.content[5: ], 'rot_13'))
                                await client.delete_message(message)

client.run(token)