import secrets
# Removing import in favour of randomdotorg for a more random random
#import randomdotorg
# This project was abandoned nearly 6 years ago and will no longer be used
import discord
import os
''' #import random
#implimenting d4 rolling
class Roll4Sides:
    def __init__(self,numofd4):
        i = 0
        while i<numofd4:
            print(secrets.choice([1, 2, 3, 4]))
            i += 1
# Attempting to impliment the humble d6
class Roll6Sides:
    def __init__(self,numofd6):
        i = 0
        while i<numofd6:
            print(secrets.choice([1, 2, 3, 4, 5, 6]))
            i += 1
# Implimenting a d8
class Roll8Sides:
    def __init__(self,numofd8):
        i = 0
        while i<numofd8:
            print(secrets.choice([1, 2, 3, 4, 5, 6,7,8]))
            i += 1
#implimenting a d10
class Roll10Sides:
    def __init__(self,numofd10):
        i = 0
        while i<numofd10:
            print(secrets.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
            i += 1
#implimenting a d12
class Roll12Sides:
    def __init__(self,numofd12):
        i = 0
        while i<numofd12:
            print(secrets.choice(range(0,13)))
            i += 1
#implimenting a d20
class Roll20Sides:
    def __init__(self,numofd20):
        i = 0
        while i<numofd20:
            print(secrets.choice(range(0,21)))
            i += 1
#implimenting a d100
class Roll100Sides:
    def __init__(self,numofd100):
        i = 0
        while i<numofd100:
            print(secrets.choice(range(0,101)))
            i += 1
#implimenting a die I might just use this guy for the full implimentation. '''
class RollAnySides:
    def __init__(self,numofdice,sides):
        i = 0
        result_list = []
        while i < numofdice:
            result_list = result_list.append(secrets.choice(range(1,(sides+1))))
            i += 1
        return result_list

msg = "Greetings fleshy beings. I am Rollybot jr./nType $help for a command list"
help_msg = "To roll a number of dice of any sides senter $roll _d_. Eg 2d20"
client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as [0.user]'.format(client))
    channel = client.get_channel(833840635831648296)
    await client.channel.send(msg)
       
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$logout'):
        client.logout()

    if message.content.startswith('$help'):
        await message.channel.send(help_msg)

    if message.content.startswith('$roll'):
        m = message.content.replace('$roll ','')
        m = m.replace('d',' ')
        m_list = m.split()
        m_map_object = map(int,m_list)
        m_list_of_integers = list(m_map_object)
        i = 0 

        while i < m_list_of_integers[0]: #first number is the number of dice
            await message.channel.send(secrets.choice(range(0,(m_list_of_integers[1]+1))))
            i += 1
        #await message.channel.send(RollAnySides(m_list_of_
        # integers[0],m_list_of_integers[1]))
        #await message.channel.send(m_list_of_results)

client.run('ODMzODM4OTUwMzQxNjczMDQy.YH4LCQ.TF-oGmAeHfe2K6d3fsAx4v5LruU')