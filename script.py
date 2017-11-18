import discord
import asyncio
import random
import pickle
import os
import codecs
import string

client = discord.Client()
        
@client.event
async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        await client.change_presence(game=discord.Game(name = '.rhelp for help'))
        
@client.event
async def on_message(message):
        if message.content.lower().startswith('.rhelp'):
                await client.send_message(message.channel, 'Commands work inside DMs.\n\n**.rot text** to rot13 the given text and get a DM with the result.\n**.rl** to rot13 the last message in the channel (that is not a .rl command) and get a DM with the result.\n**.rl n** to rot13 the last n messages in the channel, up to 50, and get a DM with the result.\n\n**How to Use:** If somebody posts an encoded message in chat, use .rl or .rl n to get a decoded version DM\'d to you. You can also DM me the encoded message and use .rl.\n\nIf you want to encode a message yourself, DM me with a .rot text command or send me a message to encode and .rl it, then paste it on the text chat.\n\nIf you want .rl and .rot messages to not clutter the chat, give me Manage Messages permissions so I can delete the commands.\n\nOnly able to translate up to 2000 characters.')
                await client.delete_message(message)

        if message.content.lower() == '.rl':
                flag = False
                async for msg in client.logs_from(message.channel, limit=15, before=message):
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
				
        if message.content.lower().startswith('i love you eurasia'):
                await client.send_message(message.channel, 'Fuck you Eurasia')

client.run('token')
