import pymysql

def obtener_conexion():
    conexion = pymysql.connect(
        host="localhost",
        port=8889,
        user="root",       # <-- CAMBIAR
        password="",  # <-- CAMBIAR
        database="empresa_poo",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexion
