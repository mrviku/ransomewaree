from  caesarCipher import *
from reverseCipher import *
from vigenereCipher import *
#take input from the user: msg, key mode
msg = 'hello' #raw_input('input a sentence to encrypt: ')
key = 3 #raw_input('input key: ')
mode = 'encrypt' #raw_input('input operation mode - encrypted/decrypted: ')

c = caesartranslate(msg, key, mode)
print 'Output from Caesar Cipher\t%s' %c
c1 = reverse(c)
print 'Output from Reverse Cipher\t%s' % c1
c2 = vtranslate(c1,c, mode)
print 'Output from Vigenere Cipher\t%s' % c2