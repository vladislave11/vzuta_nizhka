from flask import Flask, render_template, request, abort, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect(database='vzuta.db')
    connection.row_factory = sqlite3.Row
    return connection

connection = get_db_connection()
shoe = connection.execute('SELECT * FROM shoes')
shoes = {}
names = []
prices = []
descrips = []
photo1s = []
photo2s = []
photo3s = []
photo4s = []
photo5s = []
photo6s = []
photo7s = []



for i in shoe:
    names.append(i['name'])
    shoes['name'] = names
    prices.append(i['price'])
    shoes['price'] = prices
    descrips.append(i['description'])
    shoes['descriptions'] = descrips
    photo1s.append(i['photo1'])
    shoes['photo1'] = photo1s
    photo2s.append(i['photo2'])
    shoes['photo2'] = photo2s
    photo3s.append(i['photo3'])
    shoes['photo3'] = photo3s
    photo4s.append(i['photo4'])
    shoes['photo4'] = photo4s
    photo5s.append(i['photo5'])
    shoes['photo5'] = photo5s
    photo6s.append(i['photo6'])
    shoes['photo6'] = photo6s
    photo7s.append(i['photo7'])
    shoes['photo7'] = photo7s


@app.route('/')
def main():
    length = len(shoes['name'])
    return render_template('index.html', shoes = shoes, length = length)





print(shoes)









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