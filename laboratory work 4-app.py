import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",                     
                        user="postgres",
                        password="4230",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/')
def link():
    return "http://127.0.0.1:5000/login/"


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')   
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            if records:
                return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
            elif username == "" or password == "":
                return render_template('account.html', error = "You did not enter your username or password! Try again or register.")
            else:
                return "Incorrect login or password! Try again or register."
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        try:
            if len(name)==0 or len(login)==0 or len(password)==0:
                return "You entered an empty value! Try again"
            else:
                cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);', (str(name), str(login), str(password)))
                conn.commit()
        except:
            conn.commit()
            return "User with this login already exists"
        return redirect('/login/')
    return render_template('registration.html')
