import sqlite3

def init_db():
    conn = sqlite3.connect('vehicles.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS vehicle (
        id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        year INTEGER,
        vin TEXT UNIQUE
    )
    ''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS maintenance (
        id INTEGER PRIMARY KEY,
        vehicle_id INTEGER,
        description TEXT,
        date TEXT,
        mileage INTEGER,
        reminder INTEGER,
        FOREIGN KEY(vehicle_id) REFERENCES vehicle(id)
    )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('vehicles.db')
    return conn
