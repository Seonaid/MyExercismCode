def abbreviate(words):
    import re

    all_words = re.sub("[-_]", " ", words).split()
    acronym = ''.join(word[0].upper() for word in all_words)
    
    return acronym