class ControladorTarea:
    def __init__(self, modelotarea, modeloetiqueta, vistatarea, vistaetiqueta):
        self.modelo = modelotarea
        self.modelo_etiqueta = modeloetiqueta
        self.vista = vistatarea
        self.vista_etiqueta = vistaetiqueta
    
    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()
    
            match opcion:
                case '1':
                    titulo, descripcion = self.vista.obtener_datos_tarea()
                    id_tarea = self.modelo.agregar_tarea(titulo, descripcion)
                    if id_tarea:
                        self.vista.mostrar_mensaje("¡Tarea agregada correctamente!")
                        # Manejar etiquetas
                        while self.vista.preguntar_agregar_etiquetas():
                            etiquetas_disponibles = self.modelo_etiqueta.obtener_etiquetas()
                            if not etiquetas_disponibles:
                                self.vista.mostrar_mensaje("No hay etiquetas disponibles. Por favor, agregue etiquetas primero.")
                                break
                            id_etiqueta_list = self.vista.seleccionar_etiquetas(etiquetas_disponibles)
                            for id_etiqueta in id_etiqueta_list:
                                self.modelo_etiqueta.asociar_etiqueta_a_tarea(id_tarea, id_etiqueta)
                            self.vista.mostrar_mensaje("Etiquetas agregadas a la tarea correctamente!")
                case '2':
                    tareas = self.modelo.obtener_tareas()
                    tareas_con_etiquetas = []
                    for tarea in tareas:
                        etiquetas = self.modelo_etiqueta.obtener_etiquetas_por_tarea(tarea[0])
                        tareas_con_etiquetas.append(tarea + (etiquetas,))
                    self.vista.mostrar_tareas(tareas_con_etiquetas)
                case '3':
                    id_tarea = self.vista.obtener_id_tarea()
                    nuevo_titulo, nueva_descripcion, nuevo_estado = self.vista.obtener_datos_actualizados()
                    if nuevo_titulo or nueva_descripcion or nuevo_estado:
                        self.modelo.actualizar_tarea(id_tarea, nuevo_titulo, nueva_descripcion, nuevo_estado)
                        self.vista.mostrar_mensaje("¡Tarea actualizada correctamente!")
                    else:
                        self.vista.mostrar_mensaje("No se realizaron cambios en la tarea.")
                case '4':
                    id_tarea = self.vista.obtener_id_tarea()
                    self.modelo.eliminar_tarea(id_tarea)
                    self.vista.mostrar_mensaje("¡Tarea eliminada correctamente!")
                case '5':
                    self.vista.mostrar_mensaje("Regresando al menú principal")
                    break
                case _:
                    self.vista.mostrar_mensaje("Opción no válida. Por favor, intente de nuevo.")
