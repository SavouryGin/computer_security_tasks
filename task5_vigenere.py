# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:47:12 2019

@author: Surovyagin Dmitriy
"""

def encrypt(message, key):
    """ Функция шифрует сообщение методом Виженера. 
    У пользователя запрашивается текст сообщения и ключ. 
    Используется русский алфавит из 32 букв (исключая 'ё') """
    
    # Создаем словарь символов, участвующих в шифровании
    rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    D = {}
    for idx, letter in enumerate(rus):
        D[letter] = idx
    
    # Разбиваем сообщение на символы и заменяем буквы на коды
    L = []
    for symb in message.lower():
        if symb.isalpha():
            L.append(D[symb])
        else:
            L.append(symb)
    
    # Присваиваем коды символам ключа
    K = [D[symb] for symb in key.lower()]
     
    # Сопоставляем коды ключа с кодами сообщения
    C = []
    i = 0
    for idx, symb in enumerate(L):
        if isinstance(symb, int):
            C.append([L[idx], K[i]])
            i += 1
        else:
            C.append(symb)
        if i >= len(K):
            i = 0
    
    # Кодируем сообщение по формуле
    # c_i = (m_i + k_i) mod 32, где 32 - длина алфавита
    res = []
    for item in C:
        if isinstance(item, list):
            c_i = (item[0] + item[1]) % 32
            res.append(chr(c_i + 1072))
        else:
            res.append(item)
    
    # Собираем строку из списка res  
    return ''.join(res)

def decrypt(message, key):
    """ Функция дешифрует сообщение, зашифрованное методом Виженера. 
    У пользователя запрашивается текст сообщения и ключ. 
    Используется русский алфавит из 32 букв (исключая 'ё') """
    
    # Создаем словарь символов, участвующих в шифровании
    rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    D = {}
    for idx, letter in enumerate(rus):
        D[letter] = idx
    
    # Разбиваем сообщение на символы и заменяем буквы на коды
    L = []
    for symb in message.lower():
        if symb.isalpha():
            L.append(D[symb])
        else:
            L.append(symb)
    
    # Присваиваем коды символам ключа
    K = [D[symb] for symb in key.lower()]
     
    # Сопоставляем коды ключа с кодами сообщения
    C = []
    i = 0
    for idx, symb in enumerate(L):
        if isinstance(symb, int):
            C.append([L[idx], K[i]])
            i += 1
        else:
            C.append(symb)
        if i >= len(K):
            i = 0
    
    # Декодируем сообщение по формуле
    # c_i = (m_i - k_i + 32) mod 32, где 32 - длина алфавита
    res = []
    for item in C:
        if isinstance(item, list):
            c_i = (item[0] - item[1] + 32) % 32
            res.append(chr(c_i + 1072))
        else:
            res.append(item)

    # Собираем строку из списка res  
    return ''.join(res)
        
# Блок запуска (не выполняется, если файл импортируется как модуль)
if __name__ == "__main__":     
    user_text = input('Введите сообщение на русском языке: ')
    user_key = input('Введите слово-ключ: ')
    try:
        print('Зашифрованное сообщение: ', encrypt(user_text, user_key))
    except:
        print('Вы ввели неправильные данные')
    print('   *   '*10)
    user_text2 = input('Введите зашифрованное сообщение: ')
    user_key2 = input('Введите слово-ключ: ')
    try:
        print('Ваше сообщение: ', decrypt(user_text2, user_key2))
    except:
        print('Вы ввели неправильные данные')