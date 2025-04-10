# Line Plot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x,y, color='Green', linestyle='--', marker='o')

plt.title("Basic Line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()