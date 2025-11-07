from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "super_secret_key"

username = ""


def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="password", database="palette"
    )
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT p.name AS palette_name, u.username
        FROM palette p
        JOIN user u on p.user_id = u.user_id
    """
    )
    palettes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", palettes=palettes)


@app.route("/main-page", methods=["GET", "POST"])
def main_page():
    # If someone tries to access this page directly → redirect them
    if request.method == 'GET':
        flash("Please log in first.")
        return redirect(url_for('index'))

    # Get the username and password
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    # If no username/password, require user to input these
    if not username or not password:
        flash("Please enter both a username and password")
        return redirect(url_for("index"))

    # Get the database connection and cursor
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Check if user exists
    cursor.execute(
        "SELECT user_id, password FROM user WHERE username = %s", (username,)
    )
    user = cursor.fetchone()

    # if the user exists
    if user:
        # Check if the password matches
        if user["password"] == password:
            # Get all the palettes from the user
            cursor.execute(
                """
                SELECT p.name AS palette_name, u.username
                FROM palette p
                JOIN user u ON p.user_id = u.user_id
                WHERE u.username = %s
            """,
                (username,),
            )
            palettes = cursor.fetchall()
            cursor.close()
            conn.close()
            # render the main page
            return render_template(
                "main-page.html", palettes=palettes, username=username
            )
        # If the password does not match, provide an error message, stay on the page
        else:
            flash("Username already taken, or invalid password")
            cursor.close()
            conn.close()
            return redirect(url_for("index"))
    # The user does not exist, create a new one
    else:
        # Create new user
        cursor.execute(
            "INSERT INTO user (username, password) VALUES (%s, %s)",
            (username, password))
        conn.commit()
        # Get user palettes
        cursor.execute(
            """
            SELECT p.name AS palette_name, u.username
            FROM palette p
            JOIN user u ON p.user_id = u.user_id
            WHERE u.username = %s
        """,
            (username,),
        )
        palettes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("main-page.html", palettes=palettes, username=username)


if __name__ == "__main__":
    app.run(debug=True)
