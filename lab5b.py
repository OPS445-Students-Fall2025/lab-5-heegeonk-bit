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

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for item in list_of_lines:
        f.write(item + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f_read = open(file_name_read, 'r')
    lines = f_read.readlines()
    f_read.close()

    f_write = open(file_name_write, 'w')
    line_number = 1
    for line in lines:
        f_write.write(str(line_number) + ':' + line)
        line_number = line_number + 1
    f_write.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
