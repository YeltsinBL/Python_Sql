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
    except Exception as ex:
        print(ex)



listado_simple()
