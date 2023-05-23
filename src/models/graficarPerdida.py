import matplotlib.pyplot as plt


class GraficarPerdida:

    _path_img = './src/assets/img/'

    def __call__(self, perdida):
        epochs = range(1, len(perdida) + 1)
        plt.plot(epochs, perdida, 'b', label='Función de pérdida')
        plt.title('Función de pérdida durante el entrenamiento')
        plt.xlabel('Épocas')
        plt.ylabel('Pérdida')
        plt.legend()
        file_name = 'graph_neuro'
        plt.savefig(self._path_img+file_name)
