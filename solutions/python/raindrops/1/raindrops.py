def convert(number):
    result = ''
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result!="Pling" and result!="Plong" and result!="Plang" and result!="PlingPlang" and result!="PlangPlong" and result!="PlingPlong" and result!="PlingPlangPlong":
        result = str(number)
    return result
