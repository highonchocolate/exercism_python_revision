def is_pangram(sentence):
    letters = []
    lower_sentence = sentence.lower()
    lower_sentence = lower_sentence.split()
    only_letters=[]
    
    for word in lower_sentence:
        for letter in word:
            if letter not in letters:
                letters.append(letter)
    unique_letters = list(set(letters))
    for letter in unique_letters:
        if ord(letter)>=97 and ord(letter)<=122:
            only_letters.append(letter)
    if len(only_letters) == 26:
        return True
    else:
        return False

