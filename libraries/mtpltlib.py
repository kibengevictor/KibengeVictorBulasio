import matplotlib.pyplot as plt

#basic line graph

# x = [0,2,4,8,10]
# y = [0,4,8,16,36]

# fig, ax = plt.subplots()

# ax.plot(x, y, marker='o', label="Data Points")

# ax.set_title("Basic Line Graph")
# ax.set_xlabel("X-Axis")
# ax.set_ylabel("Y-Axis")

# ax.legend()

# plt.show()

#bar graph
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# fig, ax = plt.subplots()

# ax.bar(x, y, label="Data Bars")

# ax.set_title("Basic Bar Graph")
# ax.set_xlabel("X-Axis")
# ax.set_ylabel("Y-Axis")

# ax.legend()

# plt.show()

#histogram
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# fig, ax = plt.subplots()

# ax.hist(data, bins=5, label="Data Histogram")

# ax.set_title("Basic Histogram")
# ax.set_xlabel("Value")
# ax.set_ylabel("Frequency")

# ax.legend()

# plt.show()

#heatmap
import seaborn as sns

x=[1, 2, 3, 4, 5]
y=[5, 4, 3, 2, 1]
z=[[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
sns.heatmap(z, xticklabels=x, yticklabels=y)
plt.show()