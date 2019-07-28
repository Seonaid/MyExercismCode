import random
from roll_dice import roll_dice

def modifier(stat):
    return (stat-10)//2


# def roll_dice(num_dice, sides, discards=0):
#     all_dice=[random.randint(1,sides) for dice in range(num_dice)]
#     for i in range(discards):
#         all_dice.remove(min(all_dice))
    
#     return sum(all_dice)

class Character:
    def __init__(self):
        self.all_stats = self.generate_stats()
        self.strength = self.all_stats['strength']
        self.dexterity = self.all_stats['dexterity']
        self.constitution = self.all_stats['constitution']
        self.intelligence = self.all_stats['intelligence']
        self.wisdom = self.all_stats['wisdom']
        self.charisma = self.all_stats['charisma']
        self.hitpoints = 10+modifier(self.constitution)

    def inspect(self):
        print(self.all_stats)

    def generate_stats(self):
        all_stats={'strength': roll_dice(4,6,1),
        'dexterity':roll_dice(4,6,1),
        'constitution':roll_dice(4,6,1),
        'intelligence':roll_dice(4,6,1),
        'wisdom':roll_dice(4,6,1),
        'charisma':roll_dice(4,6,1),
        'hitpoints':roll_dice(4,6,1)}
        return all_stats

    def ability(self):
        return self.all_stats[random.choice(list(self.all_stats.keys()))]


Char = Character()
print(Char.inspect())

#print(roll_dice(4,6,1))