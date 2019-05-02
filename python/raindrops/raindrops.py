def raindrops(number):
    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    response = ''.join([sound for factor, sound in sounds.items() if number % factor == 0])
    return response or str(number)
