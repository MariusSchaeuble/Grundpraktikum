import string


def identifier(string1):
    res = []
    i = 0
    while i < len(string1):
        if isCharacter(string1[i]):
            # start of id
            str1 = string1[i]
            l = 1
            while l + i < len(string1) and (isCharacter(string1[i + l]) or string1[i + l] in ["_", "[", "]"] or isNumber(string1[i + l])):
                str1 += string1[i + l]
                l = l + 1
            i = i + l
            res.append(str1)
        i = i+1
    res = filterVec(res, ["sin", "cos", "tan", "asin", "acos", "exp", "log", "sqrt", "atan", "sinh", "cosh", "tanh"])
    res = list(dict.fromkeys(res)) #duplikate entfernen
    #i = i+1
    return res


def filterVec(list1, targets):
    for target in targets:
        for elem in list1:
            if elem == target:
                list1.remove(elem)
    return list1


def isCharacter(string1):
    if len(string1) != 1:
        return False
    if string1[0] in list(string.ascii_lowercase + string.ascii_uppercase):
        return True
    return False


def isNumber(string1):
    if len(string1) != 1:
        return False
    if string1[0] in list(string.digits):
        return True
    return False


def roundUP(zahl):
    r = round(zahl)
    if r > zahl:
        return r
    else:
        return r+1



