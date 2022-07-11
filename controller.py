from dis import Instruction
from os import curdir
import sqlite3 as sql

def commitClose(conn):
    conn.commit()
    conn.close()

def connectionDB():
    return sql.connect("productos.db")

def createDB():
    conn = connectionDB()
    commitClose(conn)

def createTable():
    conn = connectionDB()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE productos(
        nombre text,
        precio integer,
        cantidad integer
    )
    """)
    commitClose(conn)
    
def insertRow(name, prec, cant):
    conn = connectionDB()
    cursor = conn.cursor();
    instruction = f"INSERT INTO productos VALUES ('{name}',{prec},{cant})"
    cursor.execute(instruction)
    commitClose(conn)

def readRows():
    conn = connectionDB()
    cursor = conn.cursor()
    instruction = f"SELECT * FROM productos"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    commitClose(conn)
    print(datos)

def insertRows(productosList):
    conn = connectionDB()
    cursor = conn.cursor()
    instruction = f"INSERT INTO productos VALUES(?,?,?)"
    cursor.executemany(instruction, productosList)
    conn.commit()
    conn.close()

def readordered(field):
    conn = connectionDB()
    cursor = conn.cursor()
    instruction = f"SELECT * FROM productos ORDER BY {field}"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search(field):
    conn = connectionDB()
    cursor = conn.cursor()
    instruction = f"SELECT * FROM productos WHERE nombre like '{field}%'"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def updateFields():
    conn = connectionDB()
    cursor = conn.cursor()
    instruction = f"UPDATE productos SET cantidad = 25 where nombre = 'milk'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
def deleteRow():
    conn = connectionDB()
    cursor = conn.cursor()
    instruction = f"DELETE FROM productos where nombre = 'arroz'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #createDB()
    #createTable()
    #commitClose()
    #insertRow('milk', 100,60)
    #readRows()
    productos_Lista = [
        ('gaseosa', 64, 25),
        ('arroz', 120, 1),
        ('galleta', 74, 50),
    ]

    #insertRows(productos_Lista)
    #readordered('precio')
    #search('mi')
    #updateFields()
    deleteRow()
