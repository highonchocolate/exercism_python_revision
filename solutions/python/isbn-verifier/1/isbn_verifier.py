def is_valid(isbn):
    index = 10
    sum = 0
    num_strings = ['0','1','2','3','4','5','6','7','8','9','X']
    rem_hyp = []
    for char in isbn:
        if char!= '-':
            if char in num_strings:
                rem_hyp.append(char)
            else: 
                return False
    if len(rem_hyp)!=10:
        return False
    for char in rem_hyp:
        if char == 'X':
            sum += index * 10
        else:
            sum += index * int(char)
            index -= 1

    if sum%11 == 0:
        return True
    else: 
        return False

    
            
        
                
            
    
