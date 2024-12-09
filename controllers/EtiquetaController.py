class ControladorEtiqueta:
    def __init__(self, modelo_etiqueta, vista_etiqueta):
        self.modelo = modelo_etiqueta
        self.vista = vista_etiqueta
    
    def mostrar_menu(self):
        while True:
            self.vista.mostrar_menu_etiquetas()
            opcion = input("Seleccione una opción: ").strip()
    
            match opcion:
                case '1':
                    nombre = self.vista.obtener_datos_etiqueta()
                    self.modelo.agregar_etiqueta(nombre)
                    self.vista.mostrar_mensaje("¡Etiqueta agregada correctamente!")
                case '2':
                    etiquetas = self.modelo.obtener_etiquetas()
                    self.vista.mostrar_etiquetas(etiquetas)
                case '3':
                    etiquetas = self.modelo.obtener_etiquetas()
                    self.vista.mostrar_etiquetas(etiquetas)
                    if not etiquetas:
                        continue
                    id_etiqueta = self.vista.obtener_id_etiqueta()
                    nuevo_nombre = self.vista.obtener_nuevo_nombre_etiqueta()
                    self.modelo.actualizar_etiqueta(id_etiqueta, nuevo_nombre)
                    self.vista.mostrar_mensaje("¡Etiqueta actualizada correctamente!")
                case '4':
                    break
                case _:
                    self.vista.mostrar_mensaje("Opción no válida. Por favor, intente de nuevo.")
