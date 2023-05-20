
class EntrenarModelo:
    def __init__(self, modelo):
        self.modelo = modelo

    def __call__(self, catetos, hipotenusas):
        historia_entrenamiento = self.modelo.fit(
            x=catetos, y=hipotenusas, epochs=1000, verbose=0)
        perdida = historia_entrenamiento.history['loss']
        return perdida
