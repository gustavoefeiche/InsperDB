class DaoInsperdb:
       
    def __init__(self, app):

        self.app = app

    def connect(self):
        text_file = open("input.txt", "r")
        lines = text_file.readlines()
        
        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = 'password'
        self.app.config['MYSQL_DB'] = 'insperdb'

        return "Done"

    def disconnect(self):
        self.mysql.connection.close()

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

    def insertValuesOrganization(self, Oname, Pname):

        self.db.execute('''INSERT INTO student_has_organization (ID_student, ID_organization) 
        VALUES (SELECT o.ID, p.ID FROM student_organization o, person p WHERE o.name = '%s' AND p.Person_name = '%s') ''', (Oname, Pname))
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        return str(rv)

    def ReturnOrganization_PersonInfo(self, Pname):

        return
      