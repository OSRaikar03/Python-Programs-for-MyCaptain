import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)

    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTEL (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, VALUE INT, RATING INT)")

    print("Table created successfully!")

    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table : " + str(values))
    insert_sql = "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, VALUE, RATING) VALUES (?, ?, ?, ?, ?)"

    conn.execute(insert_sql, values)

    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn.sqlite3.connect(dbname)

    cur = conn.cursor()

    cur.execute("SELECT * FROM OYO HOTELS")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)
