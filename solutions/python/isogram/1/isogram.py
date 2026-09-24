def is_isogram(phrase):
    letters = []
    phrase_lower = phrase.lower()
    for letter in phrase_lower:
        if letter not in letters:
            if letter != '-' and letter != ' ' :
                letters.append(letter)
        else:
            return False
    return True
