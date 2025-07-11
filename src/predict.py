
import argparse
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Predict dropout risk using a trained XGBoost model.")
parser.add_argument('--input', type=str, required=True, help='Path to input CSV file')
parser.add_argument('--model', type=str, required=True, help='Path to trained model file (.joblib)')
parser.add_argument('--output', type=str, required=True, help='Path to save the predictions CSV')
args = parser.parse_args()

# Cargar datos
df = pd.read_csv(args.input)

# Cargar modelo
model_bundle = joblib.load(args.model)
model = model_bundle['model']
features = model_bundle['features']
threshold = model_bundle['threshold']
scaler = model_bundle['scaler']

# Preprocesamiento
X = df[features]
X_scaled = scaler.transform(X)

# Predicciones
proba = model.predict_proba(X_scaled)[:, 1]
pred = (proba >= threshold).astype(int)

# Guardar resultados
df['dropout_risk_score'] = proba
df['dropout_prediction'] = pred
df.to_csv(args.output, index=False)

print(f"Predictions saved to {args.output}")
