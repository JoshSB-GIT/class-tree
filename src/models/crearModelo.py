from models.construirModelo import ConstruirModelo
from models.entrenarModelo import EntrenarModelo
from models.predecirModelo import PredecirModelo
from models.graficarPerdida import GraficarPerdida


class Modelo:
    def __init__(self):
        self.construir = ConstruirModelo()
        self.entrenar = None
        self.predecir = None
        self.graficar_perdida = GraficarPerdida()

    def asignar_entrenar(self, modelo):
        self.entrenar = EntrenarModelo(modelo)

    def asignar_predecir(self, modelo):
        self.predecir = PredecirModelo(modelo)
