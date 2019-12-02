# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:47:12 2019

@author: Surovyagin Dmitiry
"""

def encode_into_bits(message: str) -> str:
    ''' The function accepts a message as input 
    and returns its bit encoding (koi8-r encoding is used) '''
    byte_repr = message.encode('koi8-r')
    bit_repr = ''
    for byte in byte_repr:
        i = bin(byte)[2:]                 # cut off '0b' characters 
        if len(i) < 8:        
            i = ('0' * (8 - len(i))) + i  # add zeros up to 8 characters
        bit_repr += str(i)
    return bit_repr

def decode_from_bits(bit_repr: str) -> str:
    ''' The function accepts a string consisting of zeros and ones, 
    and returns a message encrypted in it (koi8-r encoding is used).'''
    message = ''
    L = []
    w = ''
    for symbol in bit_repr:
        w += symbol
        if len(w) == 8:
            if w == '00000000':
                break
            else:
                L.append(w)
                w = ''
    for item in L:
        x = int(item, base=2)             # convert binary to integer
        byte = bytes([x])                 # get byte from x
        message += byte.decode('koi8-r')  # decode byte to character
    return message

def hide_with_end_spaces(path: str , bit_repr: str) -> None:
    ''' The function hides the bit representation of the message, 
    adding a space to the end of each line if the representation bit is one. 
    If the bit is zero, nothing is added to the string.'''
    try:
        file = open(path,'r')
    except:
        return 'Unable to open file'
    # Create a container file in which the message will be hidden
    output = open('secret_spaces.txt','w')
    idx = 0     # counter for characters in bit_repr
    for line in file:
        if idx < len(bit_repr):
            new_line = ''
            if bit_repr[idx] == '1':
                new_line = line[:-1] + ' ' + '\n'
                output.write(new_line)
                idx += 1
            else:
                output.write(line)
                idx += 1
        else:
            output.write(line)
    file.close()
    output.close()

def find_with_end_spaces(path: str) -> str:
    ''' The function retrieves the bit representation of the message 
    hidden by the function hide_with_end_spaces().'''
    try:
        file = open(path,'r')
    except:
        return 'Unable to open file'
    L = []
    item = ''
    for line in file:
        if line[-2] == ' ':
            item += '1'
        else:
            item += '0'
        if len(item) == 8:
            L.append(item)
            item = ''
    bit_repr = ''
    for i in L:
        if i == '00000000':
            break
        else:
            bit_repr += i
    file.close()
    return bit_repr

if __name__ == "__main__": 
    message = input("Enter your message: ")
    path1 = input("Enter the relative path to the container file: ")
    try:
        to_hide = encode_into_bits(message)
        hide_with_end_spaces(path1, to_hide)
        print('Your message is hidden!')
    except:
        print('Error!')
    ans = input("Do you want to find a message? Type 'yes' or 'no': ")
    if ans == 'yes' or ans == 'y':
        path2 = input("Enter the relative path to the container file: ")
        try:
            founded = find_with_end_spaces(path2)
            m = decode_from_bits(founded)
            print("Your message: ", m)
        except:
            print('Error!')
    else:
        print("Bye!")