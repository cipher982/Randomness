"""
Video animation of Monte Carlo estimation of a circle's area.
The function (x**2 + y**2 + r**2) can be changed around to create other shapes of choice.

By: David Rose
Date : 10/9/2017
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import cycle


# Select dot count (more gives better accuracy!, seems to converge around ~2k normally)
dotCount = 10000

x = np.random.uniform(-1.5, 1.5, dotCount)
y = np.random.uniform(-1, 1, dotCount)
plotArea = 3 * 2
# print('all x is: ',x)
xx = np.linspace(-1, 1, 100)
yy = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(xx, yy)
F = X ** 2 + Y ** 2 - 1

# Clear out plot memory
plt.close("all")
fig = plt.figure(2)
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
scat = ax.scatter([], [], s=5)

plt.contour(X, Y, F, [0])
plt.axis("equal")


def init():
    scat.set_offsets([])
    return scat


global objectArea
count = 0


def animate(i, F=F, plotArea=plotArea):
    data = np.hstack((x[:i, np.newaxis], y[:i, np.newaxis]))
    scat.set_offsets(data)

    try:
        global count
    except NameError:
        count = 0
    else:
        pass

    colors = []
    for ii in range(0, len(x) - 1):
        if x[ii] ** 2 + y[ii] ** 2 - 1 < 0:
            colors.append("blue")

        else:
            colors.append("red")
    print("-----------------", np.size(colors))
    scat.set_color(colors)

    if i < len(x):
        if x[i] ** 2 + y[i] ** 2 - 1 < 0:
            print(x[i], ",", y[i], " is in, count is now ", count)
            count = count + 1
            # scat.set_color('blue')
            # print('now count is ',count)
        else:
            print(x[i], ",", y[i], " is out")
            # scat.set_color('red')

    objectArea = plotArea * (count / (i + 1))
    areaStr = str(round(objectArea, 2))

    plt.title("Current Estimate of Circle's area is: " + areaStr)

    if i == len(x):
        objectArea = plotArea * (count / len(x))
        print(objectArea)
        print(count)
        print("Monte Carlo Estimation is: ", objectArea)

    return scat


anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=len(x) + 1, interval=2, blit=False
)

anim.save(
    "monte_carlo_test.mp4",
    fps=20,
    dpi=200,
    bitrate=-1,
    extra_args=["-vcodec", "libx264"],
)
