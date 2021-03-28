import os

import discord
from helpers import get_role_id
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()
client = discord.Client(prefix='', intents=intents)
guildId = 823925849925222450
channelId = 825076696926650368


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_raw_reaction_add(payload):
    guild = await client.fetch_guild(guildId)
    if client.user.id == payload.user_id:
        return
    if payload.channel_id != channelId:
        return

    role_id = get_role_id(payload.emoji)
    if role_id is None:
        return

    role = guild.get_role(role_id)
    members = await guild.query_members(user_ids=[payload.user_id])
    if len(members) == 1:
        member = members[0]
        await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    guild = await client.fetch_guild(guildId)
    if client.user.id == payload.user_id:
        return
    if payload.channel_id != channelId:
        return

    role_id = get_role_id(payload.emoji)
    if role_id is None:
        return

    role = guild.get_role(role_id)
    members = await guild.query_members(user_ids=[payload.user_id])
    if len(members) == 1:
        member = members[0]
        await member.remove_roles(role)


client.run(os.getenv('TOKEN'))
