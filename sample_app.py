from flask import Flask, render_template, request, redirect, url_for
import pymysql

sample = Flask(__name__)

SQL_CREAR_TABLA = """
CREATE TABLE IF NOT EXISTS aprendices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    numero_documento VARCHAR(20) NOT NULL,
    ficha VARCHAR(20) NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def get_db_connection():
    return pymysql.connect(
        host="servidor-bd",
        user="root",
        password="sena123",
        database="adso_db",
        cursorclass=pymysql.cursors.DictCursor
    )

def init_db():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(SQL_CREAR_TABLA)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error inicializando la BD: {e}")

@sample.route("/", methods=["GET"])
def home():
    init_db()
    aprendices = []
    error = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM aprendices ORDER BY id DESC")
            aprendices = cursor.fetchall()
        conn.close()
    except Exception as e:
        error = f"Error al consultar la BD: {e}"

    return render_template("index.html", aprendices=aprendices, error=error)

@sample.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form.get("nombre_completo")
    documento = request.form.get("numero_documento")
    ficha = request.form.get("ficha")

    if nombre and documento and ficha:
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO aprendices (nombre_completo, numero_documento, ficha) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, documento, ficha))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error insertando: {e}")

    return redirect(url_for("home"))

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=False) # nosec B104
