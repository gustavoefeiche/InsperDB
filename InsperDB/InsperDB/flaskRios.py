from flask import Flask, request, jsonify, Response
from flask_mysqldb import MySQL
from DaoInsperdb import DaoInsperdb
import json

app = Flask(__name__)

obj = DaoInsperdb(app)
obj.configApp()
obj.initializeSQL(MySQL)

@app.route('/add', methods = ['GET', 'POST'])
def add():

	if request.method == 'POST':

		obj.initializeCursor()

		js = json.loads(request.get_json(force = True))
		email = js['email']
		pw =  js['password']
		obj.insertValuesPerson(email, pw)
		return "Done"

if __name__ == '__main__':
    app.run(debug=True)