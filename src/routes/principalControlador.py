from models.datosEntrenamiento import DatosPrueba as datos

# Definimos la clase Controlador para coordinar las operaciones del modelo y
# la vista


class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    # Método principal para ejecutar la aplicación
    def ejecutar(self):
        # Construimos el modelo de la red neuronal
        modelo = self.modelo.construir()
        self.modelo.asignar_entrenar(modelo)
        self.modelo.asignar_predecir(modelo)
        self.datos = datos

        # Definimos los valores de entrada y salida para entrenar el modelo
        catetos = self.datos().catetos_prueba()
        hipotenusas = self.datos().hipotenusa_prueba()

        perdida = self.modelo.entrenar(catetos, hipotenusas)
        self.modelo.graficar_perdida(perdida)

        nuevos_catetos = self.vista.obtener_catetos()
        nueva_hipotenusa = self.modelo.predecir(nuevos_catetos)
        return str(self.vista.mostrar_resultado(nueva_hipotenusa[0][0]))
