from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Charger le jeu de données Iris
iris = load_iris()
X = iris.data

# Normaliser les données
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)
