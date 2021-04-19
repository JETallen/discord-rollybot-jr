import secrets
# Removing import in favour of randomdotorg for a more random random
#import randomdotorg
# This project was abandoned nearly 6 years ago and will no longer be used
import discord
#import random
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
            print(secrets.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
            i += 1
#implimenting a d100
class Roll100Sides:
    def __init__(self,numofd100):
        i = 0
        while i<numofd100:
            print(secrets.choice(range(0,101)))
            i += 1
#implimenting a die
class RollAnySides:
    def __init__(self,numofdice,sides):
        i = 0
        while i<numofdice:
            print(secrets.choice(range(0,(sides+1))))
            i += 1
RollAnySides(5,11)