import mysql.connector
from models.conexion import ConexionDB

class ModeloTarea:
    def __init__(self):
        self.conn = ConexionDB.conexion()
        self.cursor = self.conn.cursor()

    def agregar_tarea(self, titulo, descripcion):
        try:
            consulta = "INSERT INTO tareas (titulo, descripcion) VALUES (%s, %s)"
            self.cursor.execute(consulta, (titulo, descripcion))
            self.conn.commit()
            return self.cursor.lastrowid  # Retorna el ID de la tarea creada
        except mysql.connector.Error as e:
            print(f"Error al agregar tarea: {e}")
            return None
    
    def obtener_tareas(self):
        try:
            self.cursor.execute("SELECT * FROM tareas")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al obtener tareas: {e}")
            return []
    
    def actualizar_tarea(self, id_tarea, titulo=None, descripcion=None, estado=None):
        campos = []
        valores = []
    
        if titulo:
            campos.append("titulo = %s")
            valores.append(titulo)
        if descripcion:
            campos.append("descripcion = %s")
            valores.append(descripcion)
        if estado:
            campos.append("estado = %s")
            valores.append(estado)
    
        if campos:
            consulta = f"UPDATE tareas SET {', '.join(campos)} WHERE id = %s"
            valores.append(id_tarea)
            try:
                self.cursor.execute(consulta, tuple(valores))
                self.conn.commit()
            except mysql.connector.Error as e:
                print(f"Error al actualizar tarea: {e}")
    
    def eliminar_tarea(self, id_tarea):
        try:
            consulta = "DELETE FROM tareas WHERE id = %s"
            self.cursor.execute(consulta, (id_tarea,))
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al eliminar tarea: {e}")
    
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
        
    def obtener_ultimo_id(self):
        consulta = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(consulta)
        return self.cursor.fetchone()[0]