from sklearn.preprocessing import LabelEncoder

# Exemple d'encodage des étiquettes
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(iris.target)
