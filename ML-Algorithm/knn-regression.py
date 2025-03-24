import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

# Generate regression data
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)  # Random X values
y = np.sin(X).ravel() + np.random.randn(80) * 0.1  # y = sin(x) with noise

# Train KNN Regressor
k = 5  # Number of neighbors
regressor = KNeighborsRegressor(n_neighbors=k)
regressor.fit(X, y)

# Predict values
X_test = np.linspace(0, 5, 100).reshape(-1, 1)
y_pred = regressor.predict(X_test)

# Plot results
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="KNN Prediction")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()