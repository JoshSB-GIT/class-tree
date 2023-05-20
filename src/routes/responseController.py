import numpy as np


class Response_controller:

    def __init__(self, hick, hick2):
        self.hick = hick
        self.hick2 = hick2

    # Método para obtener los valores de los catetos del usuario
    def obtener_catetos(self):
        cateto1 = self.hick
        cateto2 = self.hick2
        return np.array([(cateto1, cateto2)])

    # Método para mostrar el resultado de la predicción al usuario
    def mostrar_resultado(self, hipotenusa):
        return "hypotenuse is: {:.6f}".format(hipotenusa)
