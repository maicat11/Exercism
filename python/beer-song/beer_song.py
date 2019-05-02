def recite(start, take=1):
    verses = []
    t = take
    for n in range(1, take+1):
        if start > 1:
            verses.append(f"{start} bottles of beer on the wall, {start} bottles of beer.")
        if start > 2:
            verses.append(f"Take one down and pass it around, {start-1} bottles of beer on the wall.")
            if t > 1:
                verses.append("")
        if start == 2:
            verses.append(f"Take one down and pass it around, {start-1} bottle of beer on the wall.")
            if t > 1:
                verses.append("")
        if start == 1:
            verses.append(f"{start} bottle of beer on the wall, {start} bottle of beer.")
            verses.append(("Take it down and pass it around, no more bottles of beer on the wall."))
            if t > 1:
                verses.append("")
        if start == 0:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.")
            verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        start -= 1
        t -= 1
    return verses
