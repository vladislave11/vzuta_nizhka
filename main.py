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
shoe_type = []
photo1s = []
photo2s = []
photo3s = []
photo4s = []
photo5s = []
photo6s = []
photo7s = []



for element in shoe:
    names.append(element['name'])
    shoes['name'] = names
    prices.append(element['price'])
    shoes['price'] = prices
    descrips.append(element['description'])
    shoes['descriptions'] = descrips
    shoe_type.append(element['type'])
    shoes['type'] = shoe_type
    photo1s.append(element['photo1'])
    shoes['photo1'] = photo1s
    photo2s.append(element['photo2'])
    shoes['photo2'] = photo2s
    photo3s.append(element['photo3'])
    shoes['photo3'] = photo3s
    photo4s.append(element['photo4'])
    shoes['photo4'] = photo4s
    photo5s.append(element['photo5'])
    shoes['photo5'] = photo5s
    photo6s.append(element['photo6'])
    shoes['photo6'] = photo6s
    photo7s.append(element['photo7'])
    shoes['photo7'] = photo7s


@app.route('/')
def main():
    length = len(shoes['name'])
    return render_template('index.html', shoes = shoes, length = length)


print(shoes)



@app.route('/add', methods = ['GET', 'POST'])
def add_model():
    length = len(shoes['name'])
    connection = get_db_connection()
    cursor = connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        type = request.form['category']
        photo1 = request.form['photo1']
        photo2 = request.form['photo2']
        photo3 = request.form['photo3']
        photo4 = request.form['photo4']
        photo5 = request.form['photo5']
        photo6 = request.form['photo6']
        photo7 = request.form['photo7']
        cursor.execute("INSERT INTO shoes (name,price,description,type,photo1,photo2,photo3,photo4,photo5,photo6,photo7) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (name,price,description,type,photo1,photo2,photo3,photo4,photo5,photo6,photo7))
        connection.commit()
        connection.close()
        return render_template("index.html", length = length, shoes = shoes)

    return render_template('add_model_form.html')



@app.route('/flipflops')
def flipflops():
    return render_template('flipflops.html')


@app.route('/loafers')
def loafers():
    return render_template('loafers.html')


@app.route('/sandals')
def sandals():
    return render_template('sandals.html')



@app.route('/slipons')
def slipons():
    return render_template('slipons.html')


@app.route('/sneakers')
def sneakers():
    return render_template('sneakers.html')


@app.route('/shoe')
def shoe():
    return render_template('shoe.html')




app.run(port=5000, host="0.0.0.0", debug=True)