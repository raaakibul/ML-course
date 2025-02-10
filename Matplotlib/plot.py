from matplotlib import pyplot as plt

plt.style.use('ggplot')
# plt.xkcd()

dev_x = [25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

c =['r', 'b']

plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='+', label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(dev_x, py_dev_y, color='r', linestyle='--', marker='o', label="Python Devs")

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")
plt.legend()

plt.tight_layout()
plt.savefig('plot.png')
plt.show()