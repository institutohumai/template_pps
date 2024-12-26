## Ejemplo extraído de ChatGPT

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Función para cargar datos
def load_data(filepath):
    """
    Carga un archivo CSV en un DataFrame de pandas.

    Args:
        filepath (str): Ruta al archivo CSV.

    Returns:
        pd.DataFrame: Datos cargados.
    """
    try:
        data = pd.read_csv(filepath)
        print(f"Datos cargados desde {filepath}")
        return data
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}")
        return None

# Función para preprocesar datos
def preprocess_data(data):
    """
    Realiza preprocesamiento básico en los datos.

    Args:
        data (pd.DataFrame): Datos originales.

    Returns:
        pd.DataFrame: Datos preprocesados.
    """
    print("Preprocesando datos...")
    # Eliminar valores nulos
    data = data.dropna()
    # Normalizar datos o transformar características (ejemplo)
    # data['feature'] = data['feature'] / data['feature'].max()
    return data

# Función para entrenar el modelo
def train_model(data):
    """
    Entrena un modelo RandomForest y guarda el modelo entrenado.

    Args:
        data (pd.DataFrame): Datos preprocesados con características y etiquetas.

    Returns:
        None
    """
    print("Entrenando modelo...")
    X = data.drop(columns=['target'])
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    print("Modelo entrenado con éxito.")
    joblib.dump(model, "models/trained_model.pkl")
    print("Modelo guardado en models/trained_model.pkl")

# Función para realizar predicciones
def make_prediction(data):
    """
    Carga un modelo entrenado y realiza predicciones en datos nuevos.

    Args:
        data (pd.DataFrame): Datos preprocesados para predicción.

    Returns:
        list: Predicciones del modelo.
    """
    print("Cargando modelo entrenado...")
    model = joblib.load("models/trained_model.pkl")
    predictions = model.predict(data)
    return predictions
