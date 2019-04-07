import random
from string import ascii_uppercase, digits

class Robot(object):
    def __init__(self):
        self.name = ''
        self.reset()

    def reset(self):
        temp_name = (''.join(random.choices(ascii_uppercase, k=2)
                             + random.choices(digits, k=3)))
        if temp_name != self.name:
            self.name = temp_name
        else:
            self.reset()
