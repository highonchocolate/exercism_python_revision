def translate(text):
    word_list = text.split()
    new_word_list = []
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for word in word_list:
        new_word = ''
        if word[0] not in vowel_list and word[0:2] not in ['xr','yt']:
            suffix = ''
            if 'qu' in word and all(letter not in vowel_list for letter in word[0:word.find('qu')]):
                for letter in word[0:word.find('qu')]:
                    suffix+=letter
                new_word = word[word.find('qu')+2:]+suffix+'qu'+'ay'
            elif 'y' in word and word[0]!='y' and all(letter not in vowel_list for letter in word[0:word.find('y')]):
                for letter in word[0:word.find('y')]:
                    suffix+=letter
                new_word = word[word.find('y'):]+suffix+'ay'
            else:
                index = 0
                suffix = ''
                for letter in word:
                    if letter not in vowel_list:
                        suffix += letter
                        index += 1
                    else:
                        index += 1
                        break 
            
                new_word = word[index-1:] + suffix + 'ay'

        else:
            new_word = word + 'ay'
        new_word_list.append(new_word)

    return ' '.join(new_word_list)
 
        
            
    
    
