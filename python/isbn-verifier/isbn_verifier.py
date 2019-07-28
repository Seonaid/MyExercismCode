def filterNumbers(character):
    return character.isdigit()

def makeNumbers(character):
    if character == 'X':
        return 10
    else:
        return int(character)

def is_valid(isbn):
    # check length and format
    raw_isbn = list(filter(filterNumbers, isbn[0:-1]))

    if (len(raw_isbn) != 9):
        return False
    if (isbn[-1].isdigit()) or (isbn[-1]=='X'):
        raw_isbn.append(isbn[-1])
        digits = list(map(makeNumbers, raw_isbn))
    else:
        return False

    n = 10
    digit_sum = 0

    for number in digits:
        digit_sum += n*number
        n -= 1

    return (digit_sum%11 == 0)


# print(is_valid('359821507X'))