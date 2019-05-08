def hey(phrase):
    phrase = phrase.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
    if not phrase:
        return "Fine. Be that way!"
    if phrase[-1] == '?':
        if phrase.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if phrase.isupper():
        return "Whoa, chill out!"
    return "Whatever."
