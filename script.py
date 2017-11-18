import discord
import asyncio
import random
import pickle
import os
import codecs

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
        if message.content.startswith('.rhelp'):
                await client.send_message(message.channel, 'Commands work inside DMs.\n\n**.rot text** to rot13 the given *text*.\n**.rl** to rot13 the last message in the channel.\n**.rl n** to rot13 the last *n* messages in the channel, up to 50.\n\nOnly able to translate up to 2000 characters.')
                await client.delete_message(message)

        if message.content == '.rl' or message.content == '.Rl':
                async for msg in client.logs_from(message.channel, limit=1, before=message):
                        await client.send_message(message.author, codecs.encode(msg.content, 'rot_13'))
                await client.delete_message(message)

        if message.content.startswith('.rl ') or message.content.startswith('.Rl '):
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

        if message.content == '.rot' or message.content == '.Rot':
                await client.send_message(message.channel, 'No argument given.')
                await client.delete_message(message)

        if message.content.startswith('.rot ') or message.content.startswith('.Rot '):
                await client.send_message(message.author, codecs.encode(message.content[5: ], 'rot_13'))
                await client.delete_message(message)

client.run('MzgxMTU3NjkxNTQxODE1MzQx.DPDEYA.lsJVmi7Mb2IZQbnzJV0ReISPzn4')
