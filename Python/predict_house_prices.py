# Predict House Prices Using Linear Regression
# Problem: Predict the price of a house based on its size (in square feet).
# Algorithm: Linear Regression

# Step-by-Step Code Implementation in Python


# Step 1: Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 2: Prepare the data
# Example data
house_size = np.array([750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200])  # Size in square feet
house_price = np.array([150, 160, 165, 170, 175, 180, 185, 190, 200, 210])  # Price in $1000s

# Step 3: Reshape data (needed for scikit-learn models)
house_size = house_size.reshape(-1, 1)

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(house_size, house_price, test_size=0.2, random_state=42)

# Step 5: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
predictions = model.predict(X_test)

# Step 7: Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Step 8: Visualize results
plt.scatter(house_size, house_price, color='blue', label='Actual Data')
plt.plot(house_size, model.predict(house_size), color='red', label='Regression Line')
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price ($1000s)")
plt.legend()
plt.show()