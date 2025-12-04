import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Jackm00re",
    "database": "proyecto_final",
}


def obtener_conexion():
    return mysql.connector.connect(**DB_CONFIG)


def agregar_paciente():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI (8 dígitos): ")
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
        telefono = input("Telefono: ")
        email = input("Email: ")

        sql = """
        INSERT INTO paciente (nombre, apellido, dni, fecha_nacimiento, telefono, email)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nombre, apellido, dni, fecha_nacimiento, telefono, email))
        conn.commit()
        print("✅ Paciente agregado con exito.")
    except Error as e:
        print("❌ Error al agregar paciente:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def ver_pacientes():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_paciente, nombre, apellido, dni FROM paciente")
        for row in cursor.fetchall():
            print(row)
    except Error as e:
        print("❌ Error al listar pacientes:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def actualizar_paciente():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        id_paciente = input("ID del paciente a actualizar: ")

        print("Dejá vacío el campo que no quieras cambiar.")
        nombre = input("Nuevo nombre: ")
        apellido = input("Nuevo apellido: ")
        telefono = input("Nuevo teléfono: ")
        email = input("Nuevo email: ")

        campos = []
        valores = []

        if nombre:
            campos.append("nombre = %s")
            valores.append(nombre)
        if apellido:
            campos.append("apellido = %s")
            valores.append(apellido)
        if telefono:
            campos.append("telefono = %s")
            valores.append(telefono)
        if email:
            campos.append("email = %s")
            valores.append(email)

        if not campos:
            print("No se indicó ningún cambio.")
            return

        valores.append(id_paciente)
        sql = "UPDATE paciente SET " + ", ".join(campos) + " WHERE id_paciente = %s"
        cursor.execute(sql, tuple(valores))
        conn.commit()
        print("✅ Paciente actualizado.")
    except Error as e:
        print("❌ Error al actualizar paciente:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def eliminar_paciente():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        id_paciente = input("ID del paciente a eliminar: ")
        cursor.execute("DELETE FROM paciente WHERE id_paciente = %s", (id_paciente,))
        conn.commit()
        if cursor.rowcount == 0:
            print("No se encontró el paciente.")
        else:
            print("✅ Paciente eliminado.")
    except Error as e:
        print("❌ Error al eliminar paciente (verificá turnos asociados):", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



def agregar_medico():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI (8 dígitos): ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        especialidad = input("Especialidad: ")

        sql = """
        INSERT INTO medico (nombre, apellido, dni, telefono, email, especialidad)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nombre, apellido, dni, telefono, email, especialidad))
        conn.commit()
        print("✅ Médico agregado con éxito.")
    except Error as e:
        print("❌ Error al agregar médico:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def ver_medicos():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_medico, nombre, apellido, especialidad FROM medico")
        for row in cursor.fetchall():
            print(row)
    except Error as e:
        print("❌ Error al listar médicos:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def actualizar_medico():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        id_medico = input("ID del médico a actualizar: ")

        print("Dejá vacío el campo que no quieras cambiar.")
        telefono = input("Nuevo telefono: ")
        email = input("Nuevo email: ")
        especialidad = input("Nueva especialidad: ")

        campos = []
        valores = []

        if telefono:
            campos.append("telefono = %s")
            valores.append(telefono)
        if email:
            campos.append("email = %s")
            valores.append(email)
        if especialidad:
            campos.append("especialidad = %s")
            valores.append(especialidad)

        if not campos:
            print("No se indicó ningún cambio.")
            return

        valores.append(id_medico)
        sql = "UPDATE medico SET " + ", ".join(campos) + " WHERE id_medico = %s"
        cursor.execute(sql, tuple(valores))
        conn.commit()
        print("✅ Médico actualizado.")
    except Error as e:
        print("❌ Error al actualizar médico:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



def programar_turno():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        id_paciente = input("ID paciente: ")
        id_medico = input("ID médico: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        hora = input("Hora (HH:MM:SS): ")
        motivo = input("Motivo: ")

        sql = """
        INSERT INTO turno (id_paciente, id_medico, fecha, hora, motivo)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (id_paciente, id_medico, fecha, hora, motivo))
        conn.commit()
        print("✅ Turno programado.")
    except Error as e:
        print("❌ Error al programar turno:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def actualizar_turno():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        id_turno = input("ID del turno a actualizar: ")
        print("Dejá vacío el campo que no quieras cambiar.")
        fecha = input("Nueva fecha (YYYY-MM-DD): ")
        hora = input("Nueva hora (HH:MM:SS): ")
        estado = input("Nuevo estado (PROGRAMADO/CANCELADO/REALIZADO): ")

        campos = []
        valores = []
        if fecha:
            campos.append("fecha = %s")
            valores.append(fecha)
        if hora:
            campos.append("hora = %s")
            valores.append(hora)
        if estado:
            campos.append("estado = %s")
            valores.append(estado)

        if not campos:
            print("No se indicó ningún cambio.")
            return

        valores.append(id_turno)
        sql = "UPDATE turno SET " + ", ".join(campos) + " WHERE id_turno = %s"
        cursor.execute(sql, tuple(valores))
        conn.commit()
        print("✅ Turno actualizado.")
    except Error as e:
        print("❌ Error al actualizar turno:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def cancelar_turno():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        id_turno = input("ID del turno a cancelar: ")
        sql = "UPDATE turno SET estado = 'CANCELADO' WHERE id_turno = %s"
        cursor.execute(sql, (id_turno,))
        conn.commit()
        if cursor.rowcount == 0:
            print("No se encontró el turno.")
        else:
            print("✅ Turno cancelado.")
    except Error as e:
        print("❌ Error al cancelar turno:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()




def buscar_pacientes():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        texto = input("Buscar por nombre, apellido o DNI (texto parcial): ")
        like = f"%{texto}%"
        sql = """
        SELECT id_paciente, nombre, apellido, dni
          FROM paciente
         WHERE nombre LIKE %s
            OR apellido LIKE %s
            OR dni LIKE %s
        """
        cursor.execute(sql, (like, like, like))
        for row in cursor.fetchall():
            print(row)
    except Error as e:
        print("❌ Error en búsqueda de pacientes:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def buscar_medicos():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        texto = input("Buscar por nombre, apellido o especialidad (texto parcial): ")
        like = f"%{texto}%"
        sql = """
        SELECT id_medico, nombre, apellido, especialidad
          FROM medico
         WHERE nombre LIKE %s
            OR apellido LIKE %s
            OR especialidad LIKE %s
        """
        cursor.execute(sql, (like, like, like))
        for row in cursor.fetchall():
            print(row)
    except Error as e:
        print("❌ Error en búsqueda de médicos:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()




def reporte_top3_medicos():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.callproc("top3_medicos_mas_turnos")
        for result in cursor.stored_results():
            for row in result.fetchall():
                print(row)
    except Error as e:
        print("❌ Error al generar reporte:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def cancelar_turnos_rango():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        id_medico = input("ID médico: ")
        fecha_desde = input("Fecha desde (YYYY-MM-DD): ")
        fecha_hasta = input("Fecha hasta (YYYY-MM-DD): ")

        cursor.callproc("cancelar_turnos_medico_rango", (id_medico, fecha_desde, fecha_hasta))
        conn.commit()
        print("✅ Turnos cancelados en el rango indicado.")
    except Error as e:
        print("❌ Error al cancelar turnos en rango:", e)
        if conn.is_connected():
            conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



def menu_pacientes():
    while True:
        print("\n--- Gestión de Pacientes ---")
        print("1. Agregar paciente")
        print("2. Ver pacientes")
        print("3. Actualizar paciente")
        print("4. Eliminar paciente")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_paciente()
        elif opcion == "2":
            ver_pacientes()
        elif opcion == "3":
            actualizar_paciente()
        elif opcion == "4":
            eliminar_paciente()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_medicos():
    while True:
        print("\n--- Gestión de Médicos ---")
        print("1. Agregar médico")
        print("2. Ver médicos")
        print("3. Actualizar médico")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_medico()
        elif opcion == "2":
            ver_medicos()
        elif opcion == "3":
            actualizar_medico()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_turnos():
    while True:
        print("\n--- Gestión de Turnos ---")
        print("1. Programar turno")
        print("2. Actualizar turno")
        print("3. Cancelar turno")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            programar_turno()
        elif opcion == "2":
            actualizar_turno()
        elif opcion == "3":
            cancelar_turno()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_busquedas():
    while True:
        print("\n--- Búsquedas Avanzadas ---")
        print("1. Buscar pacientes")
        print("2. Buscar médicos")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            buscar_pacientes()
        elif opcion == "2":
            buscar_medicos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_reportes():
    while True:
        print("\n--- Reportes y Operaciones Especiales ---")
        print("1. Top 3 médicos con más turnos")
        print("2. Cancelar turnos por rango de fechas (médico)")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            reporte_top3_medicos()
        elif opcion == "2":
            cancelar_turnos_rango()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_principal():
    while True:
        print("\n=== Sistema de Gestión de Hospital ===")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("3. Manejo de Turnos")
        print("4. Búsquedas Avanzadas")
        print("5. Reporte de Turnos y Cancelaciones")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "4":
            menu_busquedas()
        elif opcion == "5":
            menu_reportes()
        elif opcion == "0":
            print("Hasta luego 👋")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu_principal()
