from models.Tarea import ModeloTarea
from models.Etiqueta import ModeloEtiqueta
from views.ViewTarea import VistaTarea 
from views.ViewEtiqueta import VistaEtiqueta 
from views.ViewMenu import VistaPrincipal
from controllers.TareaController import ControladorTarea 
from controllers.EtiquetaController import ControladorEtiqueta 
from controllers.MenuController import ControladorPrincipal
def main():
    # Conexión a la base de datos (si es necesario)
    

    # Instanciar los modelos y vistas
    modelo_tarea = ModeloTarea()
    vista_tarea = VistaTarea()
    controlador_tarea = ControladorTarea(modelo_tarea, ModeloEtiqueta(), vista_tarea, VistaEtiqueta())

    # Instanciar controlador de etiquetas si es necesario
    modelo_etiqueta = ModeloEtiqueta()
    vista_etiqueta = VistaEtiqueta()
    controlador_etiqueta = ControladorEtiqueta(modelo_etiqueta, vista_etiqueta)

    # Instanciar el controlador principal con los controladores de tareas y etiquetas
    controlador_principal = ControladorPrincipal(controlador_tarea, controlador_etiqueta, VistaPrincipal())
    controlador_principal.ejecutar()

if __name__ == "__main__":
    main()