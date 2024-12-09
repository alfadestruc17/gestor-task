from colorama import Fore, Style

class VistaEtiqueta:
    @staticmethod
    def mostrar_menu_etiquetas():
        print("--- Gestor de Etiquetas ---")
        print("1. Agregar Etiqueta")
        print("2. Ver Etiquetas")
        print("3. Actualizar Etiqueta")
        print("4. Volver al Menú Principal")
    
    @staticmethod
    def obtener_datos_etiqueta():
        while True:
            nombre = input("Ingrese el nombre de la etiqueta: ").strip()
            if not nombre:
                print(Fore.RED + "El nombre de la etiqueta no puede quedar en blanco. Intente de nuevo." + Style.RESET_ALL)
                continue
            if any(char.isdigit() for char in nombre):
                print(Fore.RED + "El nombre de la etiqueta no puede contener números. Intente de nuevo." + Style.RESET_ALL)
                continue
            return nombre
    
    @staticmethod
    def mostrar_etiquetas(etiquetas):
        print("--- Lista de Etiquetas ---")
        if not etiquetas:
            print("No hay etiquetas registradas.")
        else:
            for etiqueta in etiquetas:
                print(f"ID: {etiqueta[0]}, Nombre: {etiqueta[1]}")
    
    @staticmethod
    def obtener_id_etiqueta():
        while True:
            try:
                id_etiqueta = int(input("Ingrese el ID de la etiqueta: "))
                return id_etiqueta
            except ValueError:
                print(Fore.RED + "El ID debe ser un número entero válido. Intente de nuevo." + Style.RESET_ALL)
    
    @staticmethod
    def obtener_nuevo_nombre_etiqueta():
        while True:
            nuevo_nombre = input("Ingrese el nuevo nombre de la etiqueta: ").strip()
            if not nuevo_nombre:
                print(Fore.RED + "El nombre de la etiqueta no puede quedar en blanco. Intente de nuevo." + Style.RESET_ALL)
                continue
            if any(char.isdigit() for char in nuevo_nombre):
                print(Fore.RED + "El nombre de la etiqueta no puede contener números. Intente de nuevo." + Style.RESET_ALL)
                continue
            return nuevo_nombre
    
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"{mensaje}")
