def rotate(text, key):
    word_list = text.split()
    new_text=[]
    for word in word_list:
        new_word=''
        for letter in word:
            if letter.isupper():
                if ord(letter)+key > 90:
                    new_letter = chr((ord(letter)+key)-26)
                else:
                    new_letter = chr(ord(letter)+key)
            elif letter.islower():
                if ord(letter)+key > 122:
                    new_letter = chr((ord(letter)+key)-26)
                else:
                    new_letter = chr(ord(letter)+key)
            else:
                new_letter = letter
            new_word += new_letter
        new_text.append(new_word)
    return ' '.join(new_text)
  
