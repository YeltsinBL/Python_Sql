"""Uso directo de consultas"""
from conexion import conexion
def listado_simple():
    """Listado"""
    try:
        connection= conexion()
        cursor = connection.cursor()
        # Consulta directa
        cursor.execute("select * from cliente")

        # #1ra forma: resultado con datos de uno a uno
        # cliente = cursor.fetchone()
        # while cliente:
        #     print("1LS:",cliente)
        #     cliente = cursor.fetchone()

        #2da forma: resultado con todos los datos
        clientes =cursor.fetchall()
        for cliente in clientes:
            print("1LS:",cliente)
        cursor.close()
    except ImportError as ex:
        print(ex)
def listado_parametro(dni):
    """Listado con parámetro"""
    try:
        connection= conexion()
        cursor = connection.cursor()
        # Consulta directa
        cursor.execute(f"select * from cliente where dni = {dni}")
        cliente =cursor.fetchone()
        print("2LP:",cliente)
        cursor.close()
    except ImportError as ex:
        print(ex)


listado_simple()
listado_parametro(78984568)
