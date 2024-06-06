import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn):
    """Create a tasks table."""
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT
    );
    """

    try:
        c = conn.cursor()
        c.execute(sql_create_table)
        print("Tasks table created successfully.")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "tasks.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
