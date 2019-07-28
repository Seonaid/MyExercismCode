import random
import string

class Robot(object):
    def __init__(self):
        self.reset()

    def randomString(self, stringLength=2):
        """Generate a random string of fixed length """
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def randomDigits(self, stringLength=3):
        numbers = string.digits
        return ''.join(random.choice(numbers) for i in range(stringLength))   
    
    def reset(self):
        random.seed()
        self.name = self.randomString(2) + self.randomDigits(3)