from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from DaoInsperdb import DaoInsperdb
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mariopalestra1'
app.config['MYSQL_DB'] = 'Insperdb'

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def imprimi():

	js = request.get_json(force = True)

	email = js['email']
	nome = js['nome']

	db = mysql.connection.cursor()
	obj = DaoInsperdb(db)
	obj.insertValuesPerson(str(email), str(nome))

	return nome

if __name__ == '__main__':
    app.run(debug=True)