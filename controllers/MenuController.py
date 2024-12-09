class ControladorPrincipal:
    def __init__(self, controlador_tarea, controlador_etiqueta, vista_principal):
        self.controlador_tarea = controlador_tarea
        self.controlador_etiqueta = controlador_etiqueta
        self.vista = vista_principal
    
    def ejecutar(self):
        while True:
            self.vista.mostrar_menu_principal()
            opcion = self.vista.obtener_opcion_principal()
    
            match opcion:
                case '1':
                    self.controlador_tarea.ejecutar()
                case '2':
                    self.controlador_etiqueta.mostrar_menu()
                case '3':
                    self.vista.mostrar_mensaje("Saliendo del programa. ¡Hasta pronto!")
                    break
                case _:
                    self.vista.mostrar_mensaje("Opción no válida. Por favor, intente de nuevo.")
