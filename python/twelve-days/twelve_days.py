def recite(start_verse, end_verse):

    lyrics = {1: ["first", "a Partridge in a Pear Tree."],
              2: ["second", "two Turtle Doves, and "],
              3: ["third", "three French Hens, "],
              4: ["fourth", "four Calling Birds, "],
              5: ["fifth", "five Gold Rings, "],
              6: ["sixth", "six Geese-a-Laying, "],
              7: ["seventh", "seven Swans-a-Swimming, "],
              8: ["eighth", "eight Maids-a-Milking, "],
              9: ["ninth", "nine Ladies Dancing, "],
              10: ["tenth", "ten Lords-a-Leaping, "],
              11: ["eleventh", "eleven Pipers Piping, "],
              12: ["twelfth", "twelve Drummers Drumming, "]
              }

    song = f"On the {lyrics[end_verse][0]} day of Christmas my true love gave to me: "
    for i in reversed(range(1, end_verse+1)):
        song += lyrics[i][1]

    if start_verse != end_verse:
        return [recite(n, n)[0] for n in range(start_verse, end_verse+1)]
    else:
        return [song]
