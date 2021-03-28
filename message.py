import os

import discord

from emoji import emoji
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()
client = discord.Client(prefix='', intents=intents)
guildId = 823925849925222450
channelId = 825076696926650368

title = 'Choose your role'
description = 'Having the game specific role will allow you to see its category\'s chat and announcements. ' \
              'React for roles!\n\n'

for name, emote in emoji.items():
    description += '{}: {}\n'.format(emote, name)


async def send_new_message(channel, text):
    message = await channel.send(text)
    for _, _emote in emoji.items():
        await message.add_reaction(_emote)


@client.event
async def on_ready():
    print('Updating message')
    channel = client.get_channel(channelId)
    messages = await channel.history(limit=1).flatten()
    messages_count = len(messages)
    embed = discord.Embed(title=title, description=description)
    if messages_count == 0:
        await send_new_message(channel, embed)
        print('Sent new message')
        return
    elif messages_count > 1:
        await channel.purge()
        await send_new_message(channel, embed)
        print('Purged and sent new message')
        return
    else:
        message = messages[0]
        await message.edit(embed=embed)
        print('Edited message')
        return


client.run(os.getenv('TOKEN'))
