class VistaPrincipal:
    @staticmethod
    def mostrar_menu_principal():
        print("--- Menú Principal ---")
        print("1. Gestionar Tareas")
        print("2. Gestionar Etiquetas")
        print("3. Salir")
    
    @staticmethod
    def obtener_opcion_principal():
        return input("Seleccione una opción: ").strip()
    
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"{mensaje}")
