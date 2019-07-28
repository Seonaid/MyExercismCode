def is_armstrong(number):
    str_number = str(number)
    number_length = len(str_number)
    sum_over_length = 0

    for i in str_number:
        sum_over_length = sum_over_length + int(i)**number_length

    return (sum_over_length == number)
