def validateType(type):
    index = -1
    try:
        index = int(type)
    except ValueError:
        return False
    if index < 1 or index > 3:
        return False
    else:
        return True

def validateNumber(number):
    try:
        int(number)
    except ValueError:
        return False
    return int(number) > 0

def validateString(string):
    return len(string) > 0