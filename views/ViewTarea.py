from colorama import Fore, Style

class VistaTarea:
    @staticmethod
    def mostrar_menu():
        print("--- Gestor de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Ver Tareas")
        print("3. Actualizar Tarea")
        print("4. Eliminar Tarea")
        print("5. Volver al Menú Principal")
    
    @staticmethod
    def obtener_datos_tarea():
        while True:
            titulo = input("Ingrese el título de la tarea: ").strip()
            if not titulo:
                print(Fore.RED + "El título no puede estar vacío. Intente de nuevo." + Style.RESET_ALL)
                continue
            if any(char.isdigit() for char in titulo):
                print(Fore.RED + "El título de la tarea no puede contener números. Intente de nuevo." + Style.RESET_ALL)
                continue
    
            descripcion = input("Ingrese la descripción de la tarea: ").strip()
            if not descripcion:
                print(Fore.RED + "La descripción no puede estar vacía. Intente de nuevo." + Style.RESET_ALL)
                continue
    
            return titulo, descripcion
    
    @staticmethod
    def mostrar_tareas(tareas):
        colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        
        print(Fore.GREEN + "--- Lista de Tareas ---" + Style.RESET_ALL)
        if not tareas:
            print(Fore.RED + "No hay tareas registradas." + Style.RESET_ALL)
        else:
            for tarea in tareas:
                etiquetas = tarea[-1]
                
                # Asignar un color a cada etiqueta
                if etiquetas:
                    etiquetas_coloreadas = [
                        colores[i % len(colores)] + etiqueta[1] + Style.RESET_ALL
                        for i, etiqueta in enumerate(etiquetas)
                    ]
                    etiquetas_str = ', '.join(etiquetas_coloreadas)
                else:
                    etiquetas_str = 'Sin etiquetas'
                
                print(Fore.BLUE + f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: {tarea[2]}, Estado: {tarea[3]}, Creado el: {tarea[4]}, Etiquetas: {etiquetas_str}" + Style.RESET_ALL)
    
    @staticmethod
    def obtener_id_tarea():
        while True:
            try:
                id_tarea = int(input("Ingrese el ID de la tarea: "))
                return id_tarea
            except ValueError:
                print(Fore.RED + "El ID debe ser un número entero válido. Intente de nuevo." + Style.RESET_ALL)
    
    @staticmethod
    def obtener_datos_actualizados():
        print("Ingrese los nuevos datos. Deje en blanco para mantener el valor actual:")
        nuevo_titulo = input("Nuevo título: ").strip()
        nuevo_descripcion = input("Nueva descripción: ").strip()
        nuevo_estado = input("Nuevo estado (pendiente/completada): ").strip().lower()
    
        if nuevo_estado and nuevo_estado not in ["pendiente", "completada"]:
            print(Fore.RED + "Estado inválido. Solo se permite 'pendiente' o 'completada'." + Style.RESET_ALL)
            return None, None, None
    
        return nuevo_titulo or None, nuevo_descripcion or None, nuevo_estado or None
    
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"{mensaje}")
    
    @staticmethod
    def preguntar_agregar_etiquetas():
        while True:
            respuesta = input("¿Desea agregar una etiqueta a la tarea? (s/n): ").strip().lower()
            if respuesta not in ['s', 'n']:
                print(Fore.RED + "Opción no válida. Por favor, ingrese 's' para sí o 'n' para no." + Style.RESET_ALL)
            else:
                return respuesta == 's'
    
    @staticmethod
    def seleccionar_etiquetas(etiquetas_disponibles):
        print("--- Etiquetas Disponibles ---")
        for etiqueta in etiquetas_disponibles:
            print(f"ID: {etiqueta[0]}, Nombre: {etiqueta[1]}")
        print("Ingrese los IDs de las etiquetas que desea agregar, separados por comas (ej: 1,3,5): ")
        while True:
            try:
                ids = input("IDs de etiquetas: ").strip()
                if not ids:
                    print(Fore.RED + "Debe ingresar al menos un ID de etiqueta." + Style.RESET_ALL)
                    continue
                id_list = [int(id_.strip()) for id_ in ids.split(',') if id_.strip()]
                if not id_list:
                    print(Fore.RED + "Debe ingresar al menos un ID de etiqueta." + Style.RESET_ALL)
                    continue
                return id_list
            except ValueError:
                print(Fore.RED + "Debe ingresar solo números separados por comas. Intente de nuevo." + Style.RESET_ALL)
