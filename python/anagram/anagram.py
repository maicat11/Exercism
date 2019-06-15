def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if candidate.lower() != word.lower() and sorted(word.lower()) == sorted(candidate.lower()):
            anagrams.append(candidate)
    return anagrams
