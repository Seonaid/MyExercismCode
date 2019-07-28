
# Score categories
# Change the values as you see fit
YACHT = 'YT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FH'
FOUR_OF_A_KIND = 'FK'
LITTLE_STRAIGHT = 'LS'
BIG_STRAIGHT = 'BS'
CHOICE = 'CH'


def score(dice, category):
    if category in [1, 2, 3, 4, 5, 6]:
        return category*dice.count(category)

    if category=='YT':
        if dice[1]*5 == sum(dice):
            return 50
        else:
            return 0

    if category=='CH':
        return sum(dice)

    dice = sorted(dice)

    if category=='FH':
        if (dice.count(dice[1])==2 and dice.count(dice[-1])==3) or (dice.count(dice[1])==3 and dice.count(dice[-1])==2):
            return sum(dice)
        else:
            return 0

    if category=='FK':
        if dice.count(dice[1])>=4:
            return 4*dice[1]
        elif dice.count(dice[-1])>=4:
            return 4*dice[-1]
        else:
            return 0

    if category=='LS':
        if sum(dice)==15:
            return 30   
        else:
            return 0

    if category=='BS':
        if sum(dice)==20:
            return 30
        else:
            return 0

