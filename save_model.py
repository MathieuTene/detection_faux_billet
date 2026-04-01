import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# 1. Chargement des données
df = pd.read_csv("billets.csv", sep=";")

# 2. Nettoyage et Préparation
df.rename(columns={'Unnamed: 0': 'is_genuine'}, inplace=True)

# Imputation par classe (pour rester cohérent avec l'entraînement du notebook)
df['margin_low'] = df.groupby('is_genuine')['margin_low'].transform(
    lambda x: x.fillna(x.median())
)

# Ordre explicite des colonnes
feature_columns = ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']

X = df[feature_columns]
y = df['is_genuine']

# 3. Entraînement
# Note : Pour les arbres, le StandardScaler n'est pas strictement nécessaire mais 
# nous le gardons pour ne pas changer le code de l'application Dash.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Utilisation de RandomForestClassifier pour plus de robustesse
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_scaled, y)

# 4. Sauvegarde
joblib.dump(model, 'model.joblib')
joblib.dump(scaler, 'scaler.joblib')

print("Modèle RANDOM FOREST sauvegardé avec succès !")
