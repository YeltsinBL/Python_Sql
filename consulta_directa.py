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
def guardar_parametro(dni,ape_pat,ape_mat,nombre,edad):
    """Guardar información"""
    try:
        connection= conexion()
        cursor = connection.cursor()
        sql = f"Insert into cliente(dni,apellidopaterno,apellidomaterno,nombres,edad)\
                values({dni},'{ape_pat}','{ape_mat}','{nombre}','{edad}')"
        cursor.execute(sql)
        cursor.commit()
        cursor.close()
    except ImportError as ex:
        print(ex)
def modificar_parametro(dni, edad):
    """Modificar información"""
    try:
        connection= conexion()
        cursor = connection.cursor()
        sql = "update cliente set edad= ? where dni=?"
        cursor.execute(sql, edad, dni)
        cursor.commit()
        cursor.close()
    except ImportError as ex:
        print(ex)
def eliminar_parametro(dni):
    """Eliminar información"""
    try:
        connection= conexion()
        cursor = connection.cursor()
        sql = "delete from cliente where dni=?"
        cursor.execute(sql, dni)
        cursor.commit()
        cursor.close()
    except ImportError as ex:
        print(ex)
listado_simple()
listado_parametro(78984568)
#guardar_parametro(111111,"Vlas","Vlas","Vlas",18)
#modificar_parametro(111111,20)
eliminar_parametro(111111)
listado_simple()
