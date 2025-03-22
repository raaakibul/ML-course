import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Generate regression data
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)  # Random X values
y = np.sin(X).ravel() + np.random.randn(80) * 0.1  # y = sin(x) with noise

# Train Random Forest Regressor
regressor = RandomForestRegressor(n_estimators=50, max_depth=3, random_state=42)
regressor.fit(X, y)

# Predict values
X_test = np.linspace(0, 5, 100).reshape(-1, 1)
y_pred = regressor.predict(X_test)

# Plot results
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicted")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
