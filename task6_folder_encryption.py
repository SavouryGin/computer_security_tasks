# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:43:09 2019

@author: Surovyagin Dmitriy
"""

import os, zipfile, pyAesCrypt, shutil

def encrypt_walk(folder: str) -> None:
    ''' The function encrypts all files in a folder using the AES algorithm 
    and the specified password. About pyAesCrypt module:
    https://pypi.org/project/pyAesCrypt/ '''
    for name in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,name)):
            file = os.path.join(folder,name)
            try:
                pyAesCrypt.encryptFile(file, file+'.aes', password, bufferSize=64*1024)
                print ('file: '+ file + ' --> successfully encrypted!')
                os.remove(file)
            except:
                print('Something went wrong. Check the data entry is correct.')
        else:
            if os.path.isdir(os.path.join(folder,name)):
                encrypt_walk(os.path.join(folder,name))

def decrypt_walk(folder: str) -> None:
    ''' The function decrypts all files in a folder encrypted 
    using the AES algorithm and the specified password. 
    About pyAesCrypt module: https://pypi.org/project/pyAesCrypt/'''
    for name in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,name)):
            file = os.path.join(folder,name)
            try:
                pyAesCrypt.decryptFile(file, file[:-4], password, bufferSize=64*1024)
                print ('file: '+ file + ' --> successfully decrypted!')
                os.remove(file) 
            except:
                print('Something went wrong. Check the data entry is correct.')
        else:
            if os.path.isdir(os.path.join(folder,name)):
                decrypt_walk(os.path.join(folder,name))

def zip_folder(folder: str) -> None:
    ''' The function packs all subfolders and files of the specified 
    directory into an archive.
    https://docs.python.org/3/library/zipfile.html
    '''
    arch = zipfile.ZipFile('%s.zip' % folder, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(folder):
        for tarfile in files:
            if tarfile != '':
                arch.write(root+'\\'+tarfile)
    arch.close()

def unzip_folder(folder: str) -> None:
    '''  The function unpacks all subfolders and files from the archive.
    https://docs.python.org/3/library/zipfile.html
    '''
    with zipfile.ZipFile(folder,'r') as zip_ref:
        zip_ref.extractall()

def pars_folder(folder: str) -> None:
    ''' The function defines all subfolders and files of the specified folder
    os.path.isfile(path) - whether the path is a file
    os.path.isdir(path) - whether the path is a directory
    os.path.join(path1[, path2[, …]]) - connects the paths taking into account 
                                        the features of the OS
    os.listdir(path=".") - list of files and directories in a folder
    '''
    for name in os.listdir(folder):
        if  os.path.isfile(os.path.join(folder,name)):
            print('file: '+ os.path.join(folder,name))
        else:
            if os.path.isdir(os.path.join(folder,name)):
                pars_folder(os.path.join(folder,name))


if __name__ == "__main__":
    path = input('Enter directory path: ')
    password = input('Enter password: ')
    try:
        encrypt_walk(path)
        zip_folder(path)
        shutil.rmtree(path)
        pyAesCrypt.encryptFile(path+'.zip', path+'.aes', password, bufferSize=64*1024)
        os.remove(path+'.zip')
        password = ''; path = ''
        print('All is ready!')
    except:
        print('Error!')
    print('=='*10)
    ans = input("Do you want to decrypt your folder? Type 'yes' or 'no': ")
    if ans == 'yes' or ans == 'y':
        path = input('Enter the path to the encrypted file: ')
        password = input('Enter password: ')
        try:
            pyAesCrypt.decryptFile(path, path[:-4]+'.zip', password, bufferSize=64*1024)
            unzip_folder(path[:-4]+'.zip')
            os.remove(path[:-4]+'.zip')
            decrypt_walk(path[:-4])
            os.remove(path)
            password = ''; path = ''
            print('All is ready!')
        except:
            print('Error!')