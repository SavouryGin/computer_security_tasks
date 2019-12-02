# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:37:33 2019

@author: Surovyagin Dmitriy
"""

rus = 'АаВЕеКМНОоРрСсТуХх'    
en =  'AaBEeKMHOoPpCcTyXx'    

rus_to_en = dict(zip(rus,en))
en_to_rus = dict(zip(en,rus))

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

def hide_with_translit(path: str , bit_repr: str) -> None:
    '''
    The function accepts the file path and a string of zeros and ones 
    encoding some message. If the bit of the secret message is equal to one, 
    then in the container text we change the Russian letter to the English 
    analogue. If the bit is equal to zero, then leave the next letter-analog 
    in the text-container unchanged. Analog letters are letters of the Russian 
    language that have a similar style in English.
    '''
    try:
        file = open(path,'r', encoding="utf8")
    except:
        return 'Unable to open file'
    # Create a container file in which the message will be hidden
    output = open('secret_translit.txt','w')
    idx = 0  # counter for characters in bit_repr
    for line in file:
        if idx > len(bit_repr):
            output.write(line)
        else:
            for char in line:
                new_line = ''
                if char in rus_to_en and idx < len(bit_repr):
                    if bit_repr[idx] == '1':
                        new_line += rus_to_en[char]
                        idx += 1
                    else:
                        new_line += char
                        idx += 1
                else:
                    new_line += char
                output.write(new_line)
    file.close()
    output.close()

def find_with_translit(path: str) -> str:
    '''
    The function takes the input path to a file with a secret message hidden 
    by hide_with_translit() function. The output is a string of zeros and ones.
    '''
    try:
        file = open(path,'r')
    except:
        return 'Unable to open file'
    L =[]
    item = ''
    for line in file:
        for char in line:
            if char in rus_to_en:
                item += '0'
            elif char in en_to_rus:
                item += '1'
            else:
                continue
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
        hide_with_translit(path1, to_hide)
        print('Your message is hidden!')
    except:
        print('Error!')
    ans = input("Do you want to find a message? Type 'yes' or 'no': ")
    if ans == 'yes' or ans == 'y':
        path2 = input("Enter the relative path to the container file: ")
        try:
            founded = find_with_translit(path2)
            m = decode_from_bits(founded)
            print("Your message: ", m)
        except:
            print('Error!')
    else:
        print("Bye!")