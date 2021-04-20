import discord
import os

msg = "Greetings Fleshy Beings I am Rollybot jr."
#print ("\n"+msg+"\n")
client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as [0.user]'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(msg)

client.run('ODMzODM4OTUwMzQxNjczMDQy.YH4LCQ.Vq2zxm-s8BP818PQzhTBBDWveew')