class DaoInsperdb:
       
    def __init__(self, app):

        self.app = app

    def connect(self):

        file = open("file.txt","r")
        lines = []

        for i in file:

            lines.append(i)
        print(lines)
            
        self.app.config['MYSQL_HOST'] = '%s',((lines[0])[:-1])
        self.app.config['MYSQL_USER'] = '%s',((lines[1])[:-1])
        self.app.config['MYSQL_PASSWORD'] = '%s',((lines[2])[:-1])
        self.app.config['MYSQL_DB'] = '%s',(lines[0])

        return "done"

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

    def insertValuesStudent_Organization(self, Oname, Pname):
        print(Oname)
        self.db.execute('''INSERT INTO student_has_organization (ID_student, ID_organization) VALUES ((SELECT ID FROM person WHERE Person_name = %s),(SELECT ID FROM student_organization WHERE nome = %s)) ''', (Pname, Oname))
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        return str(rv)
"""
    def ReturnOrganization_PersonInfo(self, Pname):

        return
"""   