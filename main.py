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

@app.route('/add', methods = ['GET', 'POST']) #Для того, щоб можна було заповнювати магазин товаром динамічно через форму
def add_model():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        photo1 = request.form['photo1']
        photo2 = request.form['photo2']
        photo3 = request.form['photo3']
        photo4 = request.form['photo4']
        photo5 = request.form['photo5']
        photo6 = request.form['photo6']
        photo7 = request.form['photo7']
        connection = get_db_connection()
        connection.execute("INSERT INTO vzuta.db (name,price,description,photo1,photo2,photo3,photo4,photo5,photo6,photo7) VALUES (?,?,?,?,?,?,?,?,?,?)", (name,price,description,photo1,photo2,photo3,photo4,photo5,photo6,photo7))
        connection.commit()
        connection.close()
        return render_template("index.html")

    return render_template('add_model_form.html')


#тобі потрібно написати форму в файлі add_model_form 👆



app.run(port=5000, debug=True)