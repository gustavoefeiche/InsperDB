from flask import Flask, request, jsonify, Response
from flask_mysqldb import MySQL
from DaoInsperdb import DaoInsperdb
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'insperdb'

mysql = MySQL(app)

@app.route('/add', methods = ['GET', 'POST'])
def add():

	js = request.get_json(force = True)

	email = js['email']
	nome =  js['nome']
	
	db = mysql.connection.cursor()
	obj = DaoInsperdb(db)
	return obj.insertValuesPerson(email, nome)

if __name__ == '__main__':
    app.run(debug=True)