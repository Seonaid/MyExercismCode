def is_pangram(sentence):
    # # if(type(sentence) != str):
    #   raise Exception("Type Error: Sentence must be a string")
    #   return False

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    allFound = True

    if (len(sentence) < 26):
        return False
    elif (sentence == alphabet):
        return True
    else:
        for c in alphabet:
            if c not in sentence.lower():
                allFound = False
                break

    return allFound