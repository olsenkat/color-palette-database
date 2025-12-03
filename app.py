from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    jsonify,
)
import mysql.connector
from functools import wraps

app = Flask(__name__)
app.secret_key = "super_secret_key"

########################################################
#                Helper Functions
########################################################


def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="password", database="palette"
    )
    return conn


def get_palettes_by_user(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
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
    return palettes


def get_all_palettes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT p.name AS palette_name, u.username
        FROM palette p
        JOIN user u ON p.user_id = u.user_id
    """
    )
    palettes = cursor.fetchall()
    cursor.close()
    conn.close()
    return palettes


def get_palette_by_name(palette_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM palette WHERE name = %s LIMIT 1", (palette_name,))
    palette = cursor.fetchone()

    return palette


def get_current_user():
    """Return the logged-in username or redirect to login"""
    username = session["username"]
    if not username:
        flash("Please log in first.")
        return redirect(url_for("index"))
    return username


def set_query_type():
    """Get the currently selected query type from form or session, default to username."""
    dropdown_value = request.form.get("myDropdown")
    if dropdown_value:
        query_type = dropdown_value
    else:
        query_type = session.get("query_type") or session.get("username")
    session["query_type"] = query_type
    return query_type


def fetch_palettes():
    """Returns the current palette list based on query type."""
    username = session["username"]
    query_type = session.get("query_type", username)

    if query_type == username:
        session["palettes"] = get_palettes_by_user(username)
    elif query_type == "all-users":
        session["palettes"] = get_all_palettes()
    else:
        session["palettes"] = get_palettes_by_user("katie")
    return session["palettes"]


########################################################
#                Helper Color Functions
########################################################


def get_palette_colors(palette_name):
    """Returns a palette's colors."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT c.hex_value
        FROM palette_color pc
        JOIN palette p ON pc.palette_id = p.palette_id
        JOIN color c ON pc.color_id = c.color_id
        WHERE p.name = %s
        ORDER BY pc.order_index
    """,
        (palette_name,),
    )
    colors = cursor.fetchall()
    cursor.close()
    conn.close()
    return [color["hex_value"] for color in colors]


def add_color_to_palette(palette_name, color_name, hex_value, r, g, b):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Insert new color
    cursor.execute(
        """
        INSERT INTO color (hex_value, r, g, b, name)
        VALUES
        (%s, %s, %s, %s, %s)
        """,
        (hex_value, r, g, b, color_name),
    )
    color_id = cursor.lastrowid

    # Get palette_id
    cursor.execute("SELECT palette_id FROM palette WHERE name = %s", (palette_name,))
    palette_row = cursor.fetchone()
    if not palette_row:
        raise ValueError(f"Palette '{palette_name}' not found")
    palette_id = palette_row["palette_id"]

    # Determine next order index
    cursor.execute(
        "SELECT COUNT(*) AS count FROM palette_color WHERE palette_id = %s",
        (palette_id,),
    )
    count_row = cursor.fetchone()
    order_index = count_row["count"] + 1

    # Link color to palette
    cursor.execute(
        """
        INSERT INTO palette_color (palette_id, color_id, order_index)
        VALUES
        (%s, %s, %s)
        """,
        (palette_id, color_id, order_index),
    )

    conn.commit()
    cursor.close()
    conn.close()


########################################################
#                Helper Tag functions
########################################################


def get_palette_tags(palette_name):
    """Returns a palette's tags."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT p.name AS palette, t.name as tag_name
        FROM palette_tag pt
        JOIN palette p ON pt.palette_id = t.palette_id
        JOIN tags t ON pt.tag_id = t.tag_id
        WHERE p.name = %s
    """,
        (palette_name,),
    )
    tags = cursor.fetchall()
    cursor.close()
    conn.close()
    return tags


########################################################
#                Authentication
########################################################


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            flash("Please log in first.")

            # Save URL they want to access
            next_url = request.path
            return redirect(url_for("index", next=next_url))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if not username or not password:
        flash("Please enter both a username and password")
        return redirect(url_for("index"))

    next_url = request.form.get("next") or url_for("main_page")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT user_id, password FROM user WHERE username = %s", (username,)
    )
    user = cursor.fetchone()

    if user:
        if user["password"] == password:
            session["username"] = username
            return redirect(next_url)
        else:
            flash("Username already taken, or invalid password")
            cursor.close()
            conn.close()
            return redirect(url_for("index"))
    else:
        cursor.execute(
            "INSERT INTO user (username, password) VALUES (%s, %s)",
            (username, password),
        )
        conn.commit()
        cursor.close()
        conn.close()
        session["username"] = username
        return redirect(next_url)


#################################################
#               Main Pages - POST
#################################################


@app.route("/")
def index():
    palettes = get_all_palettes()
    return render_template("index.html", palettes=palettes)


@app.route("/main-page", methods=["GET", "POST"])
@login_required
def main_page():
    username = session["username"]
    palettes = fetch_palettes()
    return render_template(
        "main-page.html",
        palettes=palettes,
        username=username,
        query_type=session.get("query_type", username),
    )


@app.route("/palettes-fetch", methods=["POST"])
@login_required
def palettes_fetch():
    set_query_type()
    return redirect(url_for("palettes") or request.referrer)


@app.route("/tags-fetch", methods=["GET", "POST"])
@login_required
def tags_fetch():
    set_query_type()
    return redirect(url_for("tags") or request.referrer)


@app.route("/colors-fetch", methods=["GET", "POST"])
@login_required
def colors_fetch():
    set_query_type()
    return redirect(url_for("colors") or request.referrer)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("index"))


#################################################
#               Main Pages - GET
#################################################
@app.route("/palettes", methods=["GET"])
@login_required
def palettes():
    username = session["username"]
    all_palettes = fetch_palettes()

    # Pagination
    page = int(request.args.get("page", 1))
    per_page = 8
    start = (page - 1) * per_page
    end = start + per_page

    palettes_page = all_palettes[start:end]

    palette_colors = {
        palette["palette_name"]: get_palette_colors(palette["palette_name"])
        for palette in palettes_page
    }

    # palette_tags = {
    #     palette.palette_name: get_palette_tags(palette.palette_name)
    #     for palette in palettes
    # }

    total_pages = len(all_palettes) + per_page - 1

    return render_template(
        "palette-list.html",
        palettes=palettes_page,
        palette_colors=palette_colors,
        # palette_tags=palette_tags,
        username=username,
        page=page,
        total_pages=total_pages,
        query_type=session["query_type"],
        fetch_url=url_for("palettes_fetch"),
    )


@app.route("/tags", methods=["GET"])
@login_required
def tags():
    username = session["username"]
    palettes = fetch_palettes()
    return render_template(
        "edit-palette.html",
        palettes=palettes,
        username=username,
        query_type=session["query_type"],
        fetch_url=url_for("tags_fetch"),
    )


@app.route("/colors", methods=["GET"])
@login_required
def colors():
    username = session["username"]
    palettes = fetch_palettes()
    # colors = get_colors()
    return render_template(
        "edit-palette.html",
        palettes=palettes,
        username=username,
        query_type=session.get("query_type", username),
        fetch_url=url_for("colors_fetch"),
    )


@app.route("/palettes/<palette_name>/edit", methods=["GET", "POST"])
@login_required
def edit_palette(palette_name):
    username = session["username"]

    palette = get_palette_by_name(palette_name)
    if not palette:
        flash("Palette is not defined")

    colors = get_palette_colors(palette["name"])

    return render_template(
        "edit-palette.html",
        palette_name=palette_name,
        query_type=session["query_type"],
        colors=colors,
        username=username,
        palette=palette,
    )


@app.route("/palettes/<palette_name>/delete", methods=["GET", "POST"])
@login_required
def delete_palette(palette_name):
    username = session["username"]
    # your logic here
    # TODO delete palette

    return redirect(url_for("palettes") or request.referrer)


@app.route("/add_color_ajax", methods=["POST"])
@login_required
def add_color_ajax():
    try:
        data = request.get_json()

        palette_name = data.get("palette")
        color_name = data.get("name")
        hex_val = data.get("hex")
        r = data.get("r")
        g = data.get("g")
        b = data.get("b")

        # Save the color to your database
        add_color_to_palette(palette_name, color_name, hex_val, r, g, b)

        # Fetch updated colors
        colors = get_palette_colors(palette_name)

        # returns list of hex strings
        return jsonify({"colors": colors})
    except Exception as e:
        # Log to console
        print("Error in add_color_ajax:", e)
        # Return JSON with error for debugging
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
