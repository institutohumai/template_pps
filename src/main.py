## Ejemplo extraído de ChatGPT

# Importar módulos necesarios
import argparse
from utils import load_data, preprocess_data, train_model, make_prediction

def main():
    # Configurar argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Herramienta de IA para estudiantes")
    parser.add_argument('--train', action='store_true', help="Entrenar el modelo")
    parser.add_argument('--predict', type=str, help="Ruta al archivo de datos para predicción")
    args = parser.parse_args()

    if args.train:
        # Lógica de entrenamiento
        print("Cargando datos para entrenamiento...")
        data = load_data("data/dataset.csv")
        processed_data = preprocess_data(data)
        train_model(processed_data)
    elif args.predict:
        # Lógica de predicción
        print(f"Realizando predicciones en: {args.predict}")
        data = load_data(args.predict)
        predictions = make_prediction(data)
        print("Predicciones:", predictions)
    else:
        print("Por favor, proporciona un argumento. Usa --help para más información.")

if __name__ == "__main__":
    main()
