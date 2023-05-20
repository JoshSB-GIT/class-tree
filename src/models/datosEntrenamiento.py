import numpy as np


class DatosPrueba:

    def __init__(self):
        self.entrada = np.array(
            [(3, 4), (5, 12), (8, 15), (7, 24), (10, 24), (8, 6)])
        self.salida = np.array([5.0, 13.0, 17.0, 25.0, 26.0, 10.0])

    def catetos_prueba(self):
        return self.entrada

    def hipotenusa_prueba(self):
        return self.salida
