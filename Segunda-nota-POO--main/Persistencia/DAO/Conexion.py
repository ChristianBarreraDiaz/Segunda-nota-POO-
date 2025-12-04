import pymysql

def obtener_conexion():
    conexion = pymysql.connect(
        host="localhost",
        user="tu_usuario",       # <-- CAMBIAR
        password="tu_password",  # <-- CAMBIAR
        database="empresa_poo",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexion
