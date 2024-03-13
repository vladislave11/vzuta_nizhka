from flask import Flask, render_template, request, abort, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect(database='vzuta.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/add', methods = ['GET', 'POST'])
def add_model():
    connection = get_db_connection()
    cursor = connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        description = request.form['description']
        print(description)
        price = request.form['price']
        photo1 = request.form['photo1']
        photo2 = request.form['photo2']
        photo3 = request.form['photo3']
        photo4 = request.form['photo4']
        photo5 = request.form['photo5']
        photo6 = request.form['photo6']
        photo7 = request.form['photo7']
        cursor.execute("INSERT INTO shoes (name,price,description,photo1,photo2,photo3,photo4,photo5,photo6,photo7) VALUES (?,?,?,?,?,?,?,?,?,?)", (name,price,description,photo1,photo2,photo3,photo4,photo5,photo6,photo7))
        connection.commit()
        connection.close()
        return render_template("index.html")

    return render_template('add_model_form.html')





app.run(port=5000, host="0.0.0.0", debug=True)