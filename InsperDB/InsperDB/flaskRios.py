from flask import Flask, request, jsonify, Response
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

@app.route('/registerorganization', methods = ['GET', 'POST'])
def addorganization():

	if request.method == 'POST':

		obj.initializeCursor()

		#js = json.loads(request.get_json(force = True))
		js = request.get_json(force = True)
		name = js['name']
		organization =  js['organization']
		obj.insertValuesStudent_Organization(organization, name)
		return "Done"
"""
@app.route('/studentorganization', methods = ['GET'])
def readInfo:

	a = obj.readStudentOrgInfo()

	data = json.dumps(a)
	r = requests.post('http://127.0.0.1:8080/add', json = data)
"""
if __name__ == '__main__':
    app.run(debug=True)