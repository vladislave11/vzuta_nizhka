import sqlite3



try:
    sqlite_connection = sqlite3.connect("vzuta.db")
    sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS shoes(
                                    name TEXT,
                                    price INTEGER,
                                    description TEXT,
                                    type TEXT,
                                    photo1 TEXT,
                                    photo2 TEXT,
                                    photo3 TEXT,
                                    photo4 TEXT,
                                    photo5 TEXT,
                                    photo6 TEXT,
                                    photo7 TEXT); '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Table ORDERS Created')
    cursor.close()

except sqlite3.Error as error:
    print('Error: ', error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')



def add_test_item():
    sqlite_connection = sqlite3.connect("vzuta.db")
    cursor = sqlite_connection.cursor()
    cursor.execute(
        "INSERT INTO shoes (name,price,description,type,photo1,photo2,photo3,photo4,photo5,photo6,photo7) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        ('ТЕСТ', 300, 'TEST', 'Босоніжки', 'https://images.prom.ua/2539521333_w640_h640_tolko-36r-i.jpg', '', '', '', '', '', ''))
    sqlite_connection.commit()
    sqlite_connection.close()


add_test_item()