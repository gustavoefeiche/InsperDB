import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return render_template('signup.html')

# --------------------------------------------------- #
if __name__ == '__main__':
    app.run(port = 8080)
