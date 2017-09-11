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
        
        exists_flag = {}
        exists = self.db.execute('''SELECT * FROM person WHERE Person_email = %s''', [person_email])

        if exists:
            # 1 se ja existe na bae de dados
            exists_flag['flag'] = '1'
            return exists_flag

        self.db.execute('''INSERT INTO Person (Person_email, Person_Password, Valid) VALUES (%s, %s, 'T')''', (person_email, person_password))
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        #0 se não existe na base de dados
        exists_flag['flag'] = '0'
        return exists_flag

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

        userInfo = {}

        self.db.execute('''SELECT * FROM  person WHERE Person_email = %s ''', [email])
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        
        userInfo['info'] = str(rv)

        return userInfo

    def logicDelete(self, email):
        
        self.db.execute('''UPDATE person SET Valid = 'F' WHERE Person_email = %s ''', [email])
        self.mysql.connection.commit()
        return 'done'

    def showStudentOrgnizations(self, email):

        s_organization = {}

        self.db.execute('''SELECT DISTINCT(so.nome) FROM person p, student_organization so, student_has_organization sho WHERE p.ID = p.ID AND so.ID = so.ID AND p.ID = (SELECT ID FROM person WHERE Person_email = %s) ''', [email])
        rv = self.db.fetchall()
        self.mysql.connection.commit()
        
        s_organization['organization'] = str(rv)

        return s_organization

    def checkLogin(self, email):
        
        login_exists = {}
        self.db.execute('''SELECT * FROM  person WHERE Person_email = %s AND Valid = 'T' ''', [email])
    
        rv = self.db.fetchall()
        
        if not rv:
            login_exists['login_exists'] = '0'
            return login_exists
        
        login_exists['login_exists'] = '1'
        return login_exists
        