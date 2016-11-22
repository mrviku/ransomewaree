import web, random, string, DataBase
from random import randint, choice
from string import ascii_uppercase
from _sqlite3 import connect



urls = ('/', 'index')

class index:
    
    def GET(self):
        
        return 'hello World'
    
    def POST(self):
       form = web.input()
       
       userID = form.userID
       print 'form is', form.userID
       CaesarK = randint(11,44)
       
 
       VigienerK = ''.join(choice(ascii_uppercase) for i in range(5))
       SubK = 'AOKPDBXLJNMHCETZSYGFQVRIWU'
       
       
       DataBase.addTodatabase(userID, VigienerK, CaesarK, SubK)
       
       rand =  VigienerK +',' + str(CaesarK) + ',' + SubK
       
       print rand
       
       return rand
   
   

   
if __name__ == '__main__':
    
   
   app = web.application(urls, globals())
   app.run()