"""
Video animation of stock charts to represent randomness
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import cycle


# Length of array (or how long motion is modeled)
motionLength = 50

# Total lines to draw
lineCount = 1


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
# ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
xMin = 0
xMax = x[:, 0].max()
yMin = x[:, 1].min() * 1.8
yMax = x[:, 1].max() * 1.8
plt.axis("equal")
plt.title("50 random chart movements, static range (-5,5)")
ax = plt.axes(
    xlim=(0, 1000),
    ylim=(-300, 300),
    title="50 random chart movements, static range (-5,5)",
)

# Create list of various colors to cycle through for each line below
# cycol = cycle('RGBA')


def build_tickers(lineCount=3, length=1000):
    x = np.zeros((length, 2))

    for i in range(0, len(x) - 1):
        for ii in range(0, len(x[i])):
            if ii == 0:
                # For x-value
                # Iterate 0,1,2,...
                x[i + 1][ii] = x[i][ii] + 1
            else:
                # For y-value
                # go a random direction

                n = np.random.randrange(-5, 6, 1)
                x[i + 1][ii] = x[i][ii] + n

    (line,) = plt.plot([], [], lw=1)
    line.set_data([], [])
    line.set_data(x[0:i, 0], x[0:i, 1])
    return (line,)


anim = animation.FuncAnimation(
    fig, build_tickers, init_func=init, frames=motionLength, interval=2, blit=True
)
anim.save(
    "ticker_animation_test.mp4",
    fps=20,
    dpi=400,
    bitrate=-1,
    extra_args=["-vcodec", "libx264"],
)

plt.show()
