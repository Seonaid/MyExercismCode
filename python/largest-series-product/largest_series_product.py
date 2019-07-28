def largest_product(series, size):
    current_largest = 0
    if len(series) ==0 and size==0:
        return 1
    elif size==0:
        return 1
    elif len(series)==0:
        raise ValueError('Series is empty')
    elif len(series) < size :
        raise ValueError('Span must be shorter than length of series')
    elif size < 0:
        raise ValueError('Span must be a positive integer')
    
    for i in range(len(series)-size+1):
        new_product=int(series[i])
        for j in range(i+1, i+size):
            new_product = new_product*int(series[j])
        if new_product > current_largest:
            current_largest = new_product

    return current_largest