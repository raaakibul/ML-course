import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from mlxtend.plotting import plot_decision_regions # type: ignore

# Generate synthetic data
np.random.seed(0)
X = np.random.randint(18, 60, (200, 2))  # Age, Salary
y = (X[:, 0] > 30).astype(int)  # Buys product if age > 30

# Split into train-test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN model
k = 5  # Number of neighbors
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

# Plot decision boundary
plt.figure(figsize=(8, 6))
plot_decision_regions(X_train, y_train, clf=model, legend=2)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("KNN Decision Boundary")
plt.show()
