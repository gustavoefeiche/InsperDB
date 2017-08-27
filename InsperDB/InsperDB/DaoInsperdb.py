# The User Data Access Object handles all interactions with the User table.
class DaoInsperdb:
       
    def __init__(self, db):
        self.db = db

    def insertValuesPerson(self, person_email, person_name):
        self.db.execute('''INSERT INTO Person (Person_email, Person_name) VALUES ('{}', '{}')'''.format(person_email, person_name))
        rv = self.db.fetchall()
        return 'ok'
      