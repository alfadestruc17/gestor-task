import mysql.connector
from models.conexion import ConexionDB
class ModeloEtiqueta:
    def __init__(self):
        self.conn = ConexionDB.conexion()
        self.cursor = self.conn.cursor()
    def agregar_etiqueta(self, nombre):
        try:
            consulta = "INSERT INTO etiquetas (nombre) VALUES (%s)"
            self.cursor.execute(consulta, (nombre,))
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al agregar etiqueta: {e}")
    
    def obtener_etiquetas(self):
        try:
            self.cursor.execute("SELECT * FROM etiquetas")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al obtener etiquetas: {e}")
            return []
    
    def actualizar_etiqueta(self, id_etiqueta, nuevo_nombre):
        try:
            consulta = "UPDATE etiquetas SET nombre = %s WHERE id = %s"
            self.cursor.execute(consulta, (nuevo_nombre, id_etiqueta))
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al actualizar etiqueta: {e}")
    
    def asociar_etiqueta_a_tarea(self, id_tarea, id_etiqueta):
        try:
            consulta = "INSERT INTO tareaetiqueta (id_tarea, id_etiqueta) VALUES (%s, %s)"
            self.cursor.execute(consulta, (id_tarea, id_etiqueta))
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al asociar etiqueta a tarea: {e}")
    
    def obtener_etiquetas_por_tarea(self, id_tarea):
        try:
            consulta = """
                SELECT etiquetas.id, etiquetas.nombre
                FROM etiquetas
                JOIN tareaetiqueta ON etiquetas.id = tareaetiqueta.id_etiqueta
                WHERE tareaetiqueta.id_tarea = %s
            """
            self.cursor.execute(consulta, (id_tarea,))
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al obtener etiquetas por tarea: {e}")
            return []
