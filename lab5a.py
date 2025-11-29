#!/usr/bin/env python3
# Author ID: hkim352

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    return read_data

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    
    list_of_lines = []
    for line in lines:
        list_of_lines.append(line.rstrip('\n'))
    
    return list_of_lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
