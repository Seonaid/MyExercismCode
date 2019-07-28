def slices(series, length):
    all_slices =[]
    
    if len(series)==0:
        raise ValueError('Series is empty')
    elif len(series) < length :
        raise ValueError('Span must be shorter than length of series')
    elif length <= 0:
        raise ValueError('Span must be a positive integer')

    for i in range(len(series)-length+1):
        all_slices.append(series[i:i+length])
    
    return all_slices