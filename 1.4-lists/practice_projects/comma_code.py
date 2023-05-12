spam = ['apples', 'bananas', 'tofu', 'cats']

def getstrfromlist(list):
    ret = ""
    for i in range(len(list)):
        if i > 0:
            if (i == len(list) - 1):
                ret += " and "
            else:
                ret += ", "

        ret += list[i]

    return ret

print(getstrfromlist(spam))
print(getstrfromlist(['apples']))
print(getstrfromlist(['apples', 'bananas']))
print(getstrfromlist(['apples', 'bananas', 'tofu']))
