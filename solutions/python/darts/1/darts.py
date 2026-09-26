def score(x, y):
    if (x**2 + y**2) <= 100 and (x**2 + y**2) > 25:
        return 1
    elif (x**2 + y**2) <= 25 and (x**2 + y**2) > 1:
        return 5
    elif (x**2 + y**2) <= 1 :
        return 10
    else: 
        return 0
    
