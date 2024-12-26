## Ejemplo extraído de ChatGPT

import unittest
import pandas as pd
from utils import load_data, preprocess_data, train_model, make_prediction
from unittest.mock import patch

class TestUtils(unittest.TestCase):

    def test_load_data(self):
        # Prueba si la función load_data carga correctamente un archivo CSV
        data = load_data('data/test_dataset.csv')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(data.shape[0], 100)  # Comprobar el número de filas esperadas

    def test_preprocess_data(self):
        # Prueba si la función preprocess_data elimina valores nulos
        data = pd.read_csv('data/test_dataset.csv')
        processed_data = preprocess_data(data)
        self.assertFalse(processed_data.isnull().values.any())  # Verificar que no haya valores nulos

    @patch('joblib.dump')  # Parcheamos joblib.dump para evitar la escritura del modelo durante las pruebas
    def test_train_model(self, mock_dump):
        # Prueba si la función train_model entrena un modelo correctamente
        data = pd.read_csv('data/test_dataset.csv')
        processed_data = preprocess_data(data)
        train_model(processed_data)
        mock_dump.assert_called_once_with('models/trained_model.pkl')  # Verificar que se haya llamado a joblib.dump

    @patch('joblib.load')  # Parcheamos joblib.load para evitar la carga real del modelo
    def test_make_prediction(self, mock_load):
        # Prueba si la función make_prediction hace predicciones correctamente
        data = pd.read_csv('data/test_dataset.csv').drop(columns=['target'])
        mock_load.return_value = 'fake_model'  # Mock de un modelo cargado
        predictions = make_prediction(data)
        self.assertIsInstance(predictions, list)
        self.assertEqual(len(predictions), data.shape[0])  # Verificar que las predicciones coincidan con el número de filas

if __name__ == '__main__':
    unittest.main()
