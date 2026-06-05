from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def obtener_rentas(precio_maximo):
    conexion = sqlite3.connect("rentas.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM rentas WHERE precio <= ?", (precio_maximo,))
    rentas = cursor.fetchall()
    conexion.close()
    return rentas

@app.route("/")
def inicio():
    precio_maximo = request.args.get("precio_maximo", 10000)
    rentas = obtener_rentas(precio_maximo)
    print("Rentas encontradas:", len(rentas))
    return render_template("index.html", rentas=rentas)

if __name__ == "__main__":
    app.run(debug=True)