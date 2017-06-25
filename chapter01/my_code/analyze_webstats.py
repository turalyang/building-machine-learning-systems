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


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


def plot_models(x, y, models):
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title("Web Traffic")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w*24*7 for w in range(10)], ["week %i" % w for w in range(10)])

    mx = sp.linspace(0, x[-1], 1000)

    if models:
        for model in models:
            plt.plot(mx, model(mx), linewidth=4)

        plt.legend(["d=%i" % m.order for m in models], loc="upper left")

    plt.grid()
    plt.show()

fp1, res, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
print("fp1:", fp1)
print("res:", res)
print("rank:", rank)
print("sv:", sv)
print("rcond:", rcond)
print("x[-1]:", x[-1])

f1 = sp.poly1d(fp1)
print("f1:", f1)
print(error(f1, x, y))

fx = sp.linspace(0, x[-1], 1000)
print("fx:", fx)
plt.plot(fx, f1(fx), linewidth=4)

f2p = sp.polyfit(x, y, 2)
print("f2p:", f2p)
f2 = sp.poly1d(f2p)
print("f2:", f2)
print("f2 error:", error(f2, x, y))

f3 = sp.poly1d(sp.polyfit(x, y, 3))
f10 = sp.poly1d(sp.polyfit(x, y, 10))
f100 = sp.poly1d(sp.polyfit(x, y, 100))

print("f3 error:", error(f3, x, y))
print("f10 error:", error(f10, x, y))
print("f100 error:", error(f100, x, y))

plot_models(x, y, [f1, f2, f3, f10, f100])
