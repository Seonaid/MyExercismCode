import random

all_rolls = [random.randint(3,18) for dice in range(1000)]

print(max(all_rolls))
