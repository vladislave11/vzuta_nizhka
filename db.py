import sqlite3



try:
    sqlite_connection = sqlite3.connect("vzuta.db")
    sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS shoes(
                                    name TEXT,
                                    price INTEGER,
                                    description TEXT,
                                    photo1 BLOB,
                                    photo2 BLOB,
                                    photo3 BLOB,
                                    photo4 BLOB,
                                    photo5 BLOB,
                                    photo6 BLOB,
                                    photo7 BLOB); '''
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