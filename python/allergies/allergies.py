ALLERGIES = {1: 'eggs', 2: 'peanuts', 4: 'shellfish', 8: 'strawberries',
             16: 'tomatoes', 32: 'chocolate', 64: 'pollen', 128: 'cats'}

class Allergies(object):

    def __init__(self, score):
        self.score = bin(score)[2:][::-1]
        # self.allergies = [ALLERGIES[2**i] for i, val in enumerate(self.score) if val == '1' and 2**i<=128]

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return [ALLERGIES[2**i] for i, val in enumerate(self.score) if val == '1' and 2**i<=128]
