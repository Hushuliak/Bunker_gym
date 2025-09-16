from flask import Flask, render_template, request, redirect
import psycopg2
import os

app = Flask(__name__)

# підключення до бази (Render Postgres)
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, last_name, first_name, phone, card_number, comment, renewal_date, expiry_date FROM members ORDER BY id DESC")
    members = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", members=members)

@app.route("/add", methods=["POST"])
def add():
    data = request.form
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO members (last_name, first_name, phone, card_number, comment, renewal_date, expiry_date) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (data.get("last_name"), data.get("first_name"), data.get("phone"), data.get("card_number"),
         data.get("comment"), data.get("renewal_date") or None, data.get("expiry_date") or None)
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")
