from sklearn.model_selection import train_test_split

# Diviser les données
X_train, X_test, y_train, y_test = train_test_split(X_normalized, iris.target, test_size=0.2, random_state=42)
