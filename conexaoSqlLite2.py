# Module Imports
import sqlite3

# Connect to Sqlite3
class conecta():
    try:
        conn = sqlite3.connect("catalogos_livros.db")
        cur = conn.cursor()
        print("Conectado")
        titulo='Título'
        cur.execute("SELECT Id,Titulo,Autor,Exemplares FROM catalogos_livros where Titulo like '%' || ? || '%'", (titulo,))
        for row in cur.fetchall():
            print(row)
    except sqlite3.Error as e:
        print(f"Error connecting to Sqlite3 Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    cur.close()

conecta()
