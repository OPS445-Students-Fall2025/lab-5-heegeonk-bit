#!/usr/bin/env python3
# Author ID: hkim352

def add(number1, number2):
    def is_number(value):
        if type(value) in [int, float]:
            return True
        if type(value) == str:
            value = value.strip()
            if value.isdigit() or (value.replace('.', '', 1).isdigit() and value.count('.') < 2):
                return True
            if value.startswith('-') and (value[1:].isdigit() or (value[1:].replace('.', '', 1).isdigit() and value[1:].count('.') < 2)):
                return True
        return False
    
    if is_number(number1) and is_number(number2):
        result = float(number1) + float(number2)
        if result.is_integer():
            return int(result)
        else:
            return result
    else:
        return 'error: could not add numbers'

def read_file(filename): 
    import os
    if os.path.exists(filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    else:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works  
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
