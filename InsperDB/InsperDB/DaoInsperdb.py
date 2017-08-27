# The User Data Access Object handles all interactions with the User table.
class DaoInsperdb:
       
    def __init__(self, db):
        self.db = db

                   
    def insertValuesPerson(self, person_email, person_name):
        self.db.execute("INSERT INTO person (Person_email, Person_name) VALUES (%s %s)",(person_email, person_name))
        rv = db.fetchall()
        return str(rv)
  
    #select all user from 'tb_user' table...    
    def select(self, table):
        select_tb_user = self.db.execute("select * from '{}'".format(table))
            
        for row in select_tb_user():
            print(row)


      