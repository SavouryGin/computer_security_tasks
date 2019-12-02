# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:33:10 2019

@author: Surovyagin Dmitriy
"""

import os
all_files = [] # Global variable for writing file paths

def pars_folder(folder: str) -> None:
    ''' The function defines all subfolders and files of the specified folder
    and puts them into the list.
    os.path.isfile(path) - whether the path is a file;
    os.path.isdir(path) - whether the path is a directory;
    os.path.join(path1[, path2[, …]]) - connects the paths taking into account 
                                        the features of the OS;
    os.listdir(path=".") - list of files and directories in a folder.'''
    for name in os.listdir(folder):
        if  os.path.isfile(os.path.join(folder,name)):
            all_files.append(os.path.join(folder,name))
        else:
            pars_folder(os.path.join(folder,name))

def scan_folder(files_list: list, byte_sign: list) -> list:
    ''' The function scans each file in the file list and looks 
    for the sequence of bytes passed to it. At the output we have 
    a list of paths in which this signature is present.'''
    res = []
    for path in files_list:
        f = open(path,'rb')
        for idx, line in enumerate(f):
            byte_list = list(line)
            # if the set of bytes of the signature is a subset 
            # of the bytes of the string, then check:
            if set(byte_list) > set(byte_sign): 
                s_list = ''; s_sign = ''
                for i in byte_list:
                    s_list += str(i)
                for j in byte_sign:
                    s_sign += str(j)
                if s_sign in s_list:
                    res.append(path)
        f.close() 
    return res       

if __name__ == "__main__":
    signature = input('Enter your signature: ')
    # signature = "By the strong curse which is upon my soul"
    byte_sign = list(signature.encode()[:16]) # Take the first 16 bytes of the signature
    
    folder = input('Enter the path to the folder you wish to scan: ')
    pars_folder(folder)
    res = scan_folder(all_files, byte_sign)
    
    print('Your signature was: \n', byte_sign)
    print('The following files were scanned:')
    for i in all_files:
        print(i)
    print('=='*10)
    if res == []:
        print('No files with this signature were found.')
    else:
        print('The signature was found in the following files of the specified folder: ')
        for j in res:
            print(j)