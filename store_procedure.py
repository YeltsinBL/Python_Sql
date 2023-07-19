"""Uso directo de consultas"""
from conexion import conexion

def listado():
    """Listar Todo"""
    try:
        connection= conexion()
        cursor = connection.cursor()
        #Listar todo
        cursor.execute("exec spListarClienteAll")
        resultset=cursor.fetchall()
        for cliente in resultset:
            print("SP1:",cliente)
        connection.close()
    except ImportError as ex:
        print(ex)
def listado__apellido_dni(valor, indicador=0):
    """Listar por: valor=apellido o dni, indicador= 0-apellido 1-dni"""
    try:
        connection= conexion()
        cursor = connection.cursor()
        # # procedimiento y parámetros juntos
        # cursor.execute(f"exec spListarCliente '{valor}',{indicador}")
        # resultset=cursor.fetchone()
        # print("SP2:",resultset)
        # connection.close()

        # procedimiento y parámetos separados
        store_proc = "exec spListarCliente @strDniApellido = ?, @bitEsDni = ?"
        params = (valor,indicador)

        cursor.execute(store_proc, params)
        resultset=cursor.fetchone()
        print("SP2:",resultset)
        connection.close()

    except ImportError as ex:
        print(ex)
listado()
listado__apellido_dni("Cruz Leon",1)
