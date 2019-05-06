class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')[::-1]

    def is_valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        card_sum = 0
        for i, num in enumerate(list(map(int, self.card_num))):
            if i % 2 == 0:
                card_sum += num
            else:
                if num == 9:
                    card_sum += 9
                else:
                    card_sum += (num*2) % 9
        return card_sum % 10 == 0
