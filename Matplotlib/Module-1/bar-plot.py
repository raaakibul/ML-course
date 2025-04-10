import matplotlib.pyplot as plt

categories = ['A','B','C','D','E']
values = [3,7,2,5,9]

plt.bar(categories,values, color='purple')

plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()