class DaoInsperdb:
       
    def __init__(self, app):

        self.app = app

    def connect(self):

        file = open("file.txt","r")
        lines = []

        for i in file:

            lines.append(i)
        
        
        self.app.config['MYSQL_HOST'] = lines[0][:-1]
        self.app.config['MYSQL_USER'] = lines[1][:-1]
        self.app.config['MYSQL_PASSWORD'] = lines[2][:-1]
        self.app.config['MYSQL_DB'] = lines[3]


        return "done"

    def disconnect(self):
        self.mysql.connection.close()
        return "done"

    def initializeCursor(self):
        self.db = self.mysql.connection.cursor()
        return "done"

    def initializeSQL(self, MySQL):

        self.mysql = MySQL(self.app)

        return "done"

    def insertValuesPerson(self, person_email, person_password):
        
            exists = False

            try:
                self.db.execute('''SET TRANSACTION ISOLATION LEVEL SERIALIZABLE ''')
                print(person_password)

                exists = self.db.execute('''SELECT * FROM person WHERE Person_email = %s''', [person_email])
            except:

                print ("Erro ao inserir os dados")
                self.mysql.connection.rollback()
                return 'fail'
                
            if exists:
                return '1'

            self.db.execute('''INSERT INTO Person (Person_email, Person_Password, Valid) VALUES (%s, %s, 'T')''', (person_email, person_password))
            rv = self.db.fetchall()
            self.mysql.connection.commit()
            return '0'

    def insertValuesStudent_Organization(self, Oname, Pemail):

        self.db.execute('''INSERT INTO student_has_organization (ID_student, ID_organization) VALUES ((SELECT ID FROM person WHERE Person_email = %s),(SELECT ID FROM student_organization WHERE nome = %s)) ''', (Pemail, Oname))
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        return "done"

    def changePersonEmail(self, NewEmail, Password):

        self.db.execute('''UPDATE person SET Person_email = %s WHERE Person_password = %s ''',(NewEmail, Password))
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        return 'done'

    def showUserInfo(self, email):

    
        self.db.execute('''SELECT * FROM  person WHERE Person_email = %s ''', [email])
        #senha_hash = self.db.execute('''SELECT Person_Password FROM  person WHERE Person_email = %s AND Valid = 'T' ''', [email])

        rv = self.db.fetchall()
        self.mysql.connection.commit()

        return str(rv)

    def logicDelete(self, email):
        
        self.db.execute('''UPDATE person SET Valid = 'F' WHERE Person_email = %s ''', [email])
        self.mysql.connection.commit()
        return 'done'

    def showStudentOrganizations(self, email):

        try:

            self.db.execute('''SET TRANSACTION ISOLATION LEVEL SERIALIZABLE ''')

            self.db.execute('''SELECT DISTINCT(so.nome) FROM person p, student_organization so, student_has_organization sho WHERE p.ID = sho.ID_student AND so.ID = sho.ID_organization AND p.ID = (SELECT ID FROM person WHERE Person_email = %s) ''', [email])
            
        except:
            
            print ("Erro ao inserir os dados")
            self.mysql.connection.rollback()
            return 'fail'

        rv = self.db.fetchall()
        self.mysql.connection.commit()
        
        return str(rv)

    def checkLogin(self, email):
        
        try:
            self.db.execute('''SET TRANSACTION ISOLATION LEVEL SERIALIZABLE ''')

            self.db.execute('''SELECT * FROM  person WHERE Person_email = %s AND Valid = 'T' ''', [email])        
        except:
            print ("Erro ao inserir os dados")
            self.mysql.connection.rollback()
            return 'fail'


        rv = self.db.fetchall()
        
        if not rv:
            return '0'
        
        return rv
        