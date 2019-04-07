def is_armstrong(number):
    power_digits = [int(x)**len(str(number)) for x in list(str(number))]
    return sum(power_digits) == number
