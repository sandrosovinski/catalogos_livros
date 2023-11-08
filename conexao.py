#!/usr/local/bin python3

# Conteudo para conexao com banco de dados MySQL
#

#from flask import Flask
#from flask_mysqldb import MySQL

#app = Flask(__name__)

#mysql = MySQL()
#mysql.init_app(app)

#app.config["MYSQL_USER"] = "catalagos_livros"
#app.config["MYSQL_PASSWORD"] = "HIgxmc5dP3NQNG7"
#app.config["MYSQL_HOST"] = "localhost"
#app.config["MYSQL_DB"] = "catalagos_livros"

#mysql = MySQL(app)

#@app.route("/")
#def CONNECT_DB():
#    CONN = mysql.connection.cursor();
#    if CONN :
#        print("Conectado")
#    else:
#        print("Erro conexão")

#if __name__ == "__main__":
#    app.run(debug=True)

# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="catalagos_livros",
        password="HIgxmc5dP3NQNG7",
        host="10.0.0.101",
        port=3306,
        database="catalagos_livros"

    )
    print("Conectado")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.close()
