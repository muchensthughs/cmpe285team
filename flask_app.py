from flask import Flask, render_template, request, session
import MySQLdb
from config import *
from utils import *

app = Flask(__name__)
app.secret_key = 'uihd3453'

db=MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DB)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return "test"

@app.route('/testmysql')
def testmysql():
    sql = "select * from user limit 1"
    res = executeSql(db, sql)
    return res[0][0]

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    sql = "select * from user where username = '%s' and password = '%s'" % (username, password)
    res = executeSql(db, sql)
    if len(res) < 1:
        return render_template('login_failed.html')
    else:
        # save username to session
        session['username'] = username
    return session.pop('username', None) # got to page that shows current plan etc.

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        sql = "insert into user values ('%s', '%s')" % (username, password)
        try:
            executeSql(db, sql) 
        except Exception as e:
            return render_template('signup.html', message = 'Sign up failed, please try a different combination')
        return render_template('index.html')