POINTS = {'AEIOULNRST': 1,
          'DG': 2,
          'BCMP': 3,
          'FHVWY': 4,
          'K': 5,
          'JX': 8,
          'QZ': 10
          }
def score(word):
    return sum([v for k, v in POINTS.items() for l in word if l.upper() in k])
