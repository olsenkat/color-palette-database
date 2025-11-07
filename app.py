from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="palette"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.name AS palette_name, u.username
        FROM palette p
        JOIN user u on p.user_id = u.user_id
    """)
    palettes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', palettes=palettes)


@app.route('/main-page')
def main_page():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.name AS palette_name, u.username
        FROM palette p
        JOIN user u on p.user_id = u.user_id
    """)
    palettes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('main-page.html', palettes=palettes)

if __name__ == '__main__':
    app.run(debug=True)