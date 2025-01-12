# Regression with Supervised Learning
# i’ll use a linear regression model to predict a student’s score based on the number of hours they study.

# Step 1: Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 2: Dataset
# Features (hours studied) and labels (scores)
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Reshaped to 2D array
scores = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # Perfect linear relationship

# Step 3: Split the data
X_train, X_test, y_train, y_test = train_test_split(hours_studied, scores, test_size=0.2, random_state=42)

# Step 4: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions
predictions = model.predict(X_test)

# Step 6: Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Step 7: Visualize the results
plt.scatter(hours_studied, scores, color='blue', label='Actual Data')
plt.plot(hours_studied, model.predict(hours_studied), color='red', label='Regression Line')
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.legend()
plt.show()