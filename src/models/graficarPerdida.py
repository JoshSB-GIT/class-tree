import matplotlib.pyplot as plt


class GraficarPerdida:
    def __call__(self, perdida):
        epochs = range(1, len(perdida) + 1)
        plt.plot(epochs, perdida, 'b', label='Función de pérdida')
        plt.title('Función de pérdida durante el entrenamiento')
        plt.xlabel('Épocas')
        plt.ylabel('Pérdida')
        plt.legend()
