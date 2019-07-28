import random

def roll_dice(num_dice, sides, discards=0):
    all_dice=[random.randint(1,sides) for dice in range(num_dice)]
    for i in range(discards):
        all_dice.remove(min(all_dice))
    
    return sum(all_dice)