from flask import Flask, jsonify
from flask_mysqldb import MySQL
from DaoInsperdb import DaoInsperdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mariopalestra1'
app.config['MYSQL_DB'] = 'Insperdb'

mysql = MySQL(app)

@app.route('/')
def imprimi():
	data = request.get_json()

	db = mysql.connection.cursor()
	obj = DaoInsperdb(db)
	obj.insertValuesPerson(1, gabriel)


if __name__ == '__main__':
    app.run(debug=True)