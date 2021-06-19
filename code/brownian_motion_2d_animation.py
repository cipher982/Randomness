"""
A simple example of an animated Brownian motion plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Length of array (or how long motion is modeled)
motionLength = 1000

x = np.zeros((motionLength, 2))
for i in range(0, len(x) - 1):

    for ii in range(0, len(x[i])):
        n = np.random.choice([1, 0, -1])
        x[i + 1][ii] = x[i][ii] + n

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
# ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
xyMin = x.min() * 1.2
xyMax = x.max() * 1.2
plt.axis("equal")
ax = plt.axes(xlim=(xyMin, xyMax), ylim=(xyMin, xyMax))

(line,) = plt.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return (line,)


def iterr(i):
    line.set_data(x[0:i, 0], x[0:i, 1])
    return (line,)


anim = animation.FuncAnimation(
    fig, iterr, init_func=init, frames=motionLength, interval=100, blit=True
)

anim.save(
    "test_animation_2.mp4", fps=120, bitrate=-1, extra_args=["-vcodec", "libx264"]
)

plt.show()
