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
            #print(secrets.choice(range(1,(sides+1))))
            self.i += 1
    def __repr__(self):
        return str(self.result_list)
print(RollAnySides(2,20))

# msg = "Greetings fleshy beings. I am Rollybot jr./nType $help for a command list"
# help_msg = "To roll a number of dice of any sides senter $roll _d_. Eg 2d20"
# client = discord.Client()

# @client.event
# async def on_ready():
#     print('we have logged in as [0.user]'.format(client))
#     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='for the $help command'))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$logout'):
#         client.logout()

#     if message.content.startswith('$help'):
#         await message.channel.send(help_msg)

#     if message.content.startswith('$roll'):
#         m = message.content.replace('$roll ','')
#         m = m.replace('d',' ')
#         m_list = m.split()
#         m_map_object = map(int,m_list)
#         m_list_of_integers = list(m_map_object)
#         m_list_of_results = []
#         i = 0 
#         #die_roll = RollAnySides(m_list_of_integers[0],m_list_of_integers[1])
#         while i < m_list_of_integers[0]: #first number is the number of dice
#             await message.channel.send(secrets.choice(range(1,(m_list_of_integers[1]+1))))
#             i += 1
#        # await message.channel.send(die_roll.result_list)
#         #print(m_list_of_results)
#         #await message.channel.send(m_list_of_results)

# client.run('TOKEN')