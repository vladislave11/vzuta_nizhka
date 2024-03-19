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