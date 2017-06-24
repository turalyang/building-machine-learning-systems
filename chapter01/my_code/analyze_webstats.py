import scipy as sp
import os
import matplotlib.pyplot as plt
data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data")
data = sp.genfromtxt(os.path.join(data_dir, "web_traffic.tsv"), delimiter="\t")
print(data[:10])
print(data.shape)
x = data[:, 0]
y = data[:, 1]
print(x)
print(y)
print(x[~sp.isnan(y)])
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x, y)
plt.title("Web Traffic")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*24*7 for w in range(10)], ["week %i" % w for w in range(10)])
plt.grid()
plt.show()
