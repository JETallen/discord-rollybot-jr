import secrets
import discord
import os

#implimenting a die I might just use this guy for the full implimentation. 
class RollAnySides:
    def __init__(self,numofdice,sides):
        self.result_list = []
        self.roll_result = 0
        self.i = 0
        while self.i < numofdice:
            self.roll_result = secrets.choice(range(1,sides+1))
            self.result_list.append(self.roll_result)
            self.i += 1
        self.sum_dice = sum(self.result_list)
    def __repr__(self):
        output = (str(self.result_list)+ ": " + str(self.sum_dice))
        return output

msg = "Greetings fleshy beings. I am Rollybot jr./nType $help for a command list"
help_msg = "To roll a number of dice of any sides senter $roll _d_ or $r _d_. Eg $roll 2d20 or $r 3d6"
die_fumble = ["Landed on a corner: Rolling again", "Fell off the table gotta roll again", "Cat got a hold of it. Grabbing a new die"]
client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as [0.user]'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='for the $help command'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send(help_msg)

    if message.content.startswith('$roll '):
        m = message.content.replace('$roll ','')
        m = m.replace('d',' ')
        m_list = m.split()
        m_map_object = map(int,m_list)
        m_list_of_integers = list(m_map_object)
        die_roll = RollAnySides(m_list_of_integers[0],m_list_of_integers[1])
        await message.channel.send(die_roll.result_list)
    
    if message.content.startswith('$r '):
        m = message.content.replace('$r ','')
        m = m.replace('d',' ')
        m_list = m.split()
        m_map_object = map(int,m_list)
        m_list_of_integers = list(m_map_object)
        die_roll = RollAnySides(m_list_of_integers[0],m_list_of_integers[1])
        await message.channel.send(die_roll)
    
client.run('TOKEN')