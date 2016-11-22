# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# the string to be encrypted/decrypted


def caesar(mode,message,key):
# tells the program to encrypt or decrypt
 mode = mode

# every possible symbol that can be encrypted
 LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# stores the encrypted/decrypted form of the message
 translated = ''
 for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# print the encrypted/decrypted string to the screen 

 return translated

# copy the encrypted/decrypted string to the clipboard
