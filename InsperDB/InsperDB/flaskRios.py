from flask import Flask, request, jsonify
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

		#js = json.loads(request.get_json(force = True))
		js = request.get_json(force = True)
		email = js['email']
		pw =  js['password']
		r = obj.insertValuesPerson(email, pw)

		exists_flag = {}

		if r == '1':
			#1 se ja existe na base de dados
			exists_flag['flag'] = '1'
			exists_flag['url'] = '/add'

			return jsonify(exists_flag)

		elif r == '0': 
			#0 se não existe na base de dados
			exists_flag['flag'] = '0'
			exists_flag['url'] = '/add'

			return jsonify(exists_flag)

		else:
			return r

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

		userInfo = {}

		userInfo['info'] = r 
		userInfo['url'] = '/user/<email>'

		return jsonify(userInfo)

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

		r = obj.showStudentOrganizations(email)
		
		if r == 'fail':
			return 'fail'

		s_organization = {}

		s_organization['organization'] = r
		s_organization['url'] = '/studentOrganization/<email>'

		return jsonify(s_organization)

@app.route('/login', methods = ['POST'])
def login():

	if request.method == 'POST':

		obj.initializeCursor()

		#js = json.loads(request.get_json(force = True))
		js = request.get_json(force = True)
		email=  js['email']

		r = obj.checkLogin(email)

		if r == 'fail':
			return 'fail'

		login_exists = {}

		if r == '0':
			login_exists['login_exists'] = '0'
			login_exists['url'] = '/login'

			return jsonify(login_exists)
		
		login_exists['login_exists'] = '1'
		login_exists['url'] = '/login'

		return jsonify(login_exists)	

if __name__ == '__main__':
    app.run(host = '0.0.0.0')