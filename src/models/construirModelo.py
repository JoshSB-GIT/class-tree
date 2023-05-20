import tensorflow as tf


class ConstruirModelo:
    def __call__(self):
        modelo = tf.keras.models.Sequential([
            tf.keras.layers.Dense(
                units=1, input_shape=(2,), activation='linear')
        ])
        modelo.compile(optimizer=tf.keras.optimizers.Adam(
            0.1), loss='mean_squared_error')
        return modelo
