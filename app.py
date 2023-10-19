import requests
from flask import Flask, render_template, request,  redirect
import psycopg2
import traceback

app = Flask(__name__)

#set FLASK_RUN_PORT=8000
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="service_db2",
    user="postgres",
    password="187211"
                        )
cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service_it.users WHERE login=%s AND password=%s ;", (str(username), str(password)))
            records = list(cursor.fetchall())
            if len(records) == 0 :
                return render_template('login.html', error="no such user")
            return render_template('account.html', full_name=records[0][1], login=records[0][2],password=records[0][3])
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')

@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        login = str(request.form.get('login'))
        password = str(request.form.get('password'))
        cursor.execute(f"SELECT * FROM service_it.users WHERE login= \'{login}\' ;")
        records = list(cursor.fetchall())
        if len(records) == 0 :
            cursor.execute('INSERT INTO service_it.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
            conn.commit()
        else:
            return render_template('registration.html', error="Login already exists. create another login")

        return redirect('/login/')

    return render_template('registration.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
