from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
# app.secret_key = "secret_key"


def get_connection():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE ,number,img,description,urgent DEFAULT 0)"""
    )


@app.route("/cars/", methods=["GET", "POST", "PUT", "DELETE"])
def car_list():
    # GET CARS
    conn = get_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM cars")
        rows = cursor.fetchall()
        cars = [dict(row) for row in rows]
        conn.close()
        return cars
    elif request.method == "POST":
        car_data = request.json
        new_car = list(car_data.values())
        cursor.execute(
            "INSERT INTO cars(number,img,description) VALUES(?,?,?)", new_car
        )
        conn.commit()
        conn.close()
        return "{'response':'success'}"
    elif request.method == "DELETE":
        car_data = request.json
        car_id = car_data.get("id")
        cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
        conn.commit()
        conn.close()
        return "{'response':'success'}"


@app.route("/cars/<int:id>/", methods=["PUT", "GET"])
def car_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM cars WHERE id=?", (id,))
        rows = cursor.fetchone()
        row = dict(rows)
        return row
    if request.method == "PUT":
        car_data = request.json
        print(car_data)
        car_id = car_data.get("id")
        cursor.execute("SELECT * FROM cars WHERE id=?", (car_id,))
        get_car = cursor.fetchone()
        car = dict(get_car)
        cursor.execute(
            "UPDATE CARS SET number=?, img=?,description=? WHERE id=?",
            [
                car_data.get("number"),
                car_data.get("img"),
                car_data.get("description"),
                car_id,
            ],
        )
        conn.commit()
        conn.close()
        return "{'response':'success'}"


if __name__ == "__main__":
    create_tables()
    app.run(debug=True, port=9000)
