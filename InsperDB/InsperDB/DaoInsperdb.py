# The User Data Access Object handles all interactions with the User table.
class DaoInsperdb:
       
    def __init__(self, app):

        self.app = app

    def configApp(self):

        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = 'mariopalestra1'
        self.app.config['MYSQL_DB'] = 'insperdb'

        return "Done"

    def initializeCursor(self):
        self.db = self.mysql.connection.cursor()
        return "done"

    def initializeSQL(self, MySQL):

        self.mysql = MySQL(self.app)

        return "done"

    def insertValuesPerson(self, person_email, person_name):
   
        self.db.execute('''INSERT INTO Person (Person_email, Person_name) VALUES (%s, %s)''', (person_email, person_name))
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        return str(rv)
      