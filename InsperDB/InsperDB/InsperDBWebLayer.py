import os
import json
import requests
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

class User():
    def __init__(self):
        self.properties = {
            'email': None,
            'password': None
        }

    def get_all_props(self):
        return self.properties

    def get_prop(self, _prop=None):
        if self.properties[_prop]:
            return self.properties[_prop]
        return None

    def set_prop(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.properties:
                self.properties[k] = v
            else:
                return False

    def __str__(self):
        return "User({})".format(self.properties)

@app.route('/', methods=['GET'])
def root():
    return render_template('signup.html')

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':

        user = User()
        user.set_prop(
            email = request.form['email'],
            password = request.form['password']
        )

        data = json.dumps(user.get_all_props())
        r = requests.post('127.0.0.1:5000/add', json = data)

    return redirect('/')
# --------------------------------------------------- #
if __name__ == '__main__':
    app.run(port = 8080)
