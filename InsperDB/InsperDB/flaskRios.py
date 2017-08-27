from flask import Flask, request
from flask_mysqldb import MySQL
from DaoInsperdb import DaoInsperdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Insperdb'

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def imprimi():
	identification = request.json['id']
	nome = request.json['nome']
	db = mysql.connection.cursor()
	obj = DaoInsperdb(db)
	obj.insertValuesPerson(str(identification), str(nome))


if __name__ == '__main__':
    app.run(debug=True)