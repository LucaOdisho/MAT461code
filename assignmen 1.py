"""
Luca Odisho, MAT461 assignment 1 question 2 plots
"""

import matplotlib.pyplot as plt
from numpy import *


def U(x):
    """
    Our potential energy function
    """
    return -(x ** 3) * (x - 2) * (x - 4)


def du(x):
    # The derivative of U
    h = 0.1
    t = U(x + h) - U(x - h)
    return t / (2 * h)


N = 5  # number of points in phase space
T = 5  # time of evolution
dt = 0.1  # time step interval
# The following are the coordinates that define [x0,x1]x[y0,y1]
x0 = -0.5
x1 = 2
y0 = -0.5
y1 = 10
# Note: These x and y work pretty well, if you change them, the points picked
# will quickly diverge to infinity when their path is taken

pointarray = empty([N, 2])  # array that holds the generated points

# The following loop chooses random points in phase space
for i in range(N):
    x = random.uniform(x0, x1)
    y = random.uniform(y0, y1)
    pointarray[i] = (x, y)

paths = empty([N, int(T / dt), 2])  # array that contains paths in phase space
for i in range(N):
    paths[i][0] = pointarray[i]
for j in range(N):  # Loop evolves each path through phase space
    for n in range(1, int(T / dt)):
        paths[j][n] = (paths[j][n - 1][0] + dt * U(paths[j][n - 1][0]),
                       paths[j][n - 1][1] + dt * du(paths[j][n - 1][0]))
col = ["black", "red", "blue", "green", "grey"]
plot1 = plt
for i in range(N):
    for j in range(1, int(T / dt)):
        plot1.scatter(paths[i][j][0], paths[i][j][1], color=col[i%4])
        plot1.text(paths[i][j][0], paths[i][j][1], str(j),
                   horizontalalignment='right')

plot1.xlabel("x")
plot1.ylabel("velocity")
plot1.grid()
plot1.title("Phase space")
plot1.show()
