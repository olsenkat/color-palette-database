import mysql.connector

TEST = True

def setup_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="palette"
    )

    cursor = conn.cursor()

    # Initialize the database

    # Choose which SQL file to use
    sql_file = "reset.sql" if TEST else "db-init.sql"

    with open(sql_file, "r") as f:
        sql_commands = f.read()

    for statement in sql_commands.split(";"):
        statement = statement.strip()
        if statement:
            try:
                cursor.execute(statement)
            except mysql.connector.Error as err:
                print(f"Error executing: {statement[:100]}...\n{err}")

    # If in a test environment, insert the values
    if TEST:
        try:
            with open("insert-test-values.sql", "r") as f:
                sql_commands = f.read()
            for statement in sql_commands.split(";"):
                statement = statement.strip()
                if statement:
                    cursor.execute(statement)
        except FileNotFoundError:
            print("No test data file found — skipping test inserts.")
        
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully")


if __name__ == "__main__":
    setup_db()