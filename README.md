# Python Computer Security Exercises
Tasks completed during the course "Mathematical Foundations of Computer Security".

## Task 1
There is a text and in it it is necessary to hide some phrase consisting of letters. The letters of this phrase are represented as bytes. These bytes must be broken into bits.
The text in which the message will be hidden should have many lines (like a poem). We have to break the hidden text into bits. And if the next bit of information to be hidden is equal to one, then a space must be added to the end of the next line of the text container. If the bit is zero, then no space is needed at the end of the line.
After encryption, the text must be decoded back.

## Task 2
There is text in which you need to hide another text. As in task 1, the hidden text is broken into bits. If the next bit of the secret message is equal to one, then in the text container double the space. If the next bit of the text to be hidden is zero, then the space remains one. Regular letters are skipped in the text container. That is, in order to hide the word "ball" (4 letters, 4 bytes or 32 bits), we need a text container with at least 32 spaces. After encryption, the text must be decoded back.

## Task 3.
The preparation is the same as in task 2 and 1. Only if the bit of the secret message is equal to one, then in the container text we change the Russian letter to the English analogue. If the bit is equal to zero, then leave the next letter-analog in the text-container unchanged. Analog letters are letters of the Russian language that have a similar style in English.
Thus, it is necessary to have auxiliary arrays of information in which a one-to-one correspondence of Russian and English letters of a similar style is specified.
After encryption, the text must be decoded back.

## Task 4. Search by signature of the specified file in the specified directory.
First, the signature of the given file is taken, i.e. the program should select a sequence of characters of at least 16 bytes from the portion of the file, which presumably cannot be repeated in files other than it.
Next, the directory for the search is indicated and all copies of the source file are found by signature. Search is performed in the entire directory, i.e. for all files and directories that are stored in it. The output of the program displays a list of paths to the found files.

## Task 5. Viginer encryption scheme.
The task is to write a program for encrypting text according to the Viginer scheme. The text for encryption and the key must be in Russian encoding and entered in the dialogue mode.

## Task 6. Directory encryption.
Write a directory encryption program that does the following:
A) encryption:
* the program asks for a directory for encryption,
* the program asks for a key,
* the program collapses the directory into an encrypted file,
* the program deletes the directory.
B) decryption:
* the program asks for a directory to decrypt,
* the program asks for a key,
* the program expands the encrypted file into a directory,
* the program deletes the file,
It is allowed to use any encryption algorithm with a key.
