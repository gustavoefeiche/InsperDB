from flask import Flask, request, jsonify, Response, url_for
from flask_mysqldb import MySQL
from DaoInsperdb import DaoInsperdb
import json

app = Flask(__name__)

obj = DaoInsperdb(app)
obj.connect()
obj.initializeSQL(MySQL)

@app.route('/add', methods = ['POST'])

def add():

	if request.method == 'POST':

		obj.initializeCursor()

		js = json.loads(request.get_json(force = True))
		email = js['email']
		pw =  js['password']
		obj.insertValuesPerson(email, pw)
		return "Done"

@app.route('/registerorganization', methods = ['POST'])

def addorganization():

	if request.method == 'POST':

		obj.initializeCursor()

		#js = json.loads(request.get_json(force = True))
		js = request.get_json(force = True)
		email = js['email']
		organization =  js['organization']
		obj.insertValuesStudent_Organization(organization, email)
		return "Done"

@app.route('/email', methods = ['POST'])

def changeEmail():

	if request.method == 'POST':

		obj.initializeCursor()

		#js = json.loads(request.get_json(force = True))
		js = request.get_json(force = True)
		NewEmail=  js['email']
		pw = js['password']
		obj.changePersonEmail(NewEmail, pw)
		
		return "Done"

@app.route('/user/<email>', methods = ['GET'])

def readUser(email):

	if request.method == 'GET':

		obj.initializeCursor()
		r = obj.showUserInfo(email)

		return r

@app.route('/delete', methods = ['POST'])
def deleteUser():

	if request.method == 'POST':

		obj.initializeCursor()

		#js = json.loads(request.get_json(force = True))
		js = request.get_json(force = True)
		email =  js['email']
		obj.logicDelete(email)
		
		return "Done"


@app.route('/studentOrganization/<email>', methods = ['GET'])
def showUserOrganizations(email):

	if request.method == 'GET':

		obj.initializeCursor()

		r = obj.showStudentOrgnizations(email)
		
		return r	



if __name__ == '__main__':
    app.run(host = '0.0.0.0')