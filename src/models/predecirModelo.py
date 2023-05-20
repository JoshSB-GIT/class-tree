
class PredecirModelo:
    def __init__(self, modelo):
        self.modelo = modelo

    def __call__(self, nuevos_catetos):
        return self.modelo.predict(nuevos_catetos)
