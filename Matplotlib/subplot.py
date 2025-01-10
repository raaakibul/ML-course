import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,8,27,64,125]

# Creating a 1x2 grid of subplots
fig,(ax1,ax2) = plt.subplots(1,2)

# First subplot
ax1.plot(x,y1, 'r-')
ax1.set_title("Plot 1")

# second subplot
ax2.plot(x,y2, 'b-')
ax2.set_title("Plot 2")

# plt.plot(x,y1)
# plt.plot(x,y2)


plt.show()