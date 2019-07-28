def filterNumbers(number):
    return number.isdigit()

def invalidCharacters(number):
    if number.isdigit():
        return False
    elif (number in ['(', ')', '+', '-', ' ', '.']):
        return False
    return True

class Phone(object):
    
    def __init__(self, phone_number):
        chars = list(filter(invalidCharacters, phone_number))
        
        if len(chars) != 0:
            raise ValueError('Phone number contains invalid character(s)')

        raw_number = list(filter(filterNumbers, phone_number))
        
        if len(raw_number) != 10:
            if len(raw_number) == 11:
                if raw_number[0] == '1':
                    del(raw_number[0])
                else:
                    raise ValueError('country code must be 1')
            else:
                raise ValueError('Wrong number of digits')

        self.number = ''.join(raw_number)
        
        self.area_code = self.number[0:3]
        if self.area_code[0] in ['0', '1']:
            raise ValueError('area_code cannot begin with 0 or 1')

        self.exchange = self.number[3:6]
        if self.exchange[0] in ['0', '1']:
            raise ValueError('exchange cannot begin with 0 or 1')

    def pretty(self):
        return '(' + self.area_code + ') ' + self.exchange + '-' + self.number[6:]

