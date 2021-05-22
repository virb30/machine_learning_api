import numpy as np
from tensorflow import keras


class Predictor:
    file = ''
    model = None

    def __init__(self, model_file: str):
        self.file = model_file

    def load_model(self):
        self.model = keras.models.load_model(self.file)

    @staticmethod
    def _prepare_values(values: dict):
        return np.asarray(list(values.values())).reshape(1, -1)

    def predict(self, values):
        if not self.model:
            self.load_model()
        input_values = self._prepare_values(values)
        predicted = self.model.predict(input_values)[0]
        return float(predicted)
