## Ejemplo extraído de ChatGPT

import unittest
import pandas as pd
from utils import preprocess_data, train_model
from unittest.mock import patch

class TestTraining(unittest.TestCase):

    @patch('joblib.dump')  # Evitamos la escritura en el disco durante la prueba
    def test_train_model_function(self, mock_dump):
        # Prueba si la función de entrenamiento crea y guarda el modelo
        data = pd.read_csv('data/test_dataset.csv')
        processed_data = preprocess_data(data)

        # Llamar a la función de entrenamiento
        train_model(processed_data)

        # Comprobar que el modelo fue guardado
        mock_dump.assert_called_once_with('models/trained_model.pkl')

    def test_model_accuracy(self):
        # Validamos la precisión del modelo entrenado
        data = pd.read_csv('data/test_dataset.csv')
        processed_data = preprocess_data(data)

        # Entrenar el modelo
        model = train_model(processed_data)

        # Comprobamos que el modelo no esté vacío y tiene precisión
        accuracy = model.score(processed_data.drop(columns=['target']), processed_data['target'])
        self.assertGreaterEqual(accuracy, 0.7)  # Asegurar que la precisión es aceptable

if __name__ == '__main__':
    unittest.main()
