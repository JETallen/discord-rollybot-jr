import secrets
# Removing import in favour of randomdotorg for a more random random
#import randomdotorg
# This project was abandoned nearly 6 years ago and will no longer be used
import discord
#import random
#implimenting d4 rolling
class Roll4Sides(int):
    def __init__(self,numofd4):
        i = 0
        while i<numofd4:
            print(secrets.choice([1, 2, 3, 4]))
            i += 1
# Attempting to impliment the humble d6
class Roll6Sides(int):
    def __init__(self,numofd6):
        i = 0
        while i<numofd6:
            print(secrets.choice([1, 2, 3, 4, 5, 6]))
            i += 1

