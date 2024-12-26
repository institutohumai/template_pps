## Ejemplo extraído de ChatGPT

import unittest
import pandas as pd
from utils import make_prediction
from unittest.mock import patch

class TestInference(unittest.TestCase):

    @patch('joblib.load')  # Mock de la carga del modelo
    def test_make_prediction_function(self, mock_load):
        # Prueba si la función make_prediction hace predicciones correctamente
        data = pd.read_csv('data/test_dataset.csv').drop(columns=['target'])
        mock_load.return_value = 'fake_model'  # Mock de modelo cargado

        predictions = make_prediction(data)
        
        # Asegurar que la salida es una lista
        self.assertIsInstance(predictions, list)
        self.assertEqual(len(predictions), data.shape[0])  # Verificar que la cantidad de predicciones es igual al número de datos

    @patch('joblib.load')  # Mock de la carga del modelo
    def test_prediction_values(self, mock_load):
        # Verificar que las predicciones sean valores dentro de un rango esperado
        data = pd.read_csv('data/test_dataset.csv').drop(columns=['target'])
        mock_load.return_value = 'fake_model'  # Mock de modelo cargado

        predictions = make_prediction(data)
        
        # Verificar que las predicciones no sean valores nulos o vacíos
        self.assertTrue(all([p is not None for p in predictions]))
        self.assertTrue(all([isinstance(p, (int, float)) for p in predictions]))  # Asegurarse de que las predicciones sean numéricas

if __name__ == '__main__':
    unittest.main()
