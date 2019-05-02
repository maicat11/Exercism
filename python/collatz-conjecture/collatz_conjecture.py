def collatz_steps(number):

    if number < 1:
        raise ValueError('Number must be greater than 1.')

    counter = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        elif number % 2 == 1:
            number = 3 * number + 1
        counter += 1
    return counter
