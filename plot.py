# Universidade Federal de Pernambuco
# ME653 Programacao Robotica
# 2021.1

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

#-------------------------
def plotRealEnv(env, rob):
    # Create a new empty map
    envMaptoPlot = []
    line = []
    for i in range(env.nbRow):
        line = []
        for j in range(env.nbCol):
            line.append(0)
        envMaptoPlot.append(line)

    # Fill the new map with the robot data
    for i in range(env.nbRow):
        for j in range(env.nbCol):
            envMaptoPlot[i][j] = env.map[i][j]

    # Allocate values for start and goal
    envMaptoPlot[2][2] = 1
    envMaptoPlot[rob.rowGoal][rob.colGoal] = 2

    # Create discrete colormap
    cmap = colors.ListedColormap(['black', 'white', 'red','green'])
    bounds = [-1,0,1,2,3]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(envMaptoPlot, cmap=cmap, norm=norm)

    ax.set_xticks(np.arange(env.nbRow))
    ax.set_yticks(np.arange(env.nbCol))

    plt.show()

#-------------------------
def plotPlanningMap(pathMap, nbRow, nbCol):
    # create discrete colormap
    cmap = colors.ListedColormap(['black','white'])
    bounds = [-1,0,1000]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    fig, ax = plt.subplots()
    ax.imshow(pathMap, cmap=cmap, norm=norm)

    # Loop over data dimensions and create text annotations.
    for i in range(nbRow):
        for j in range(nbCol):
            text = ax.text(j, i, pathMap[i][j], ha="center", va="center", color="k")

    ax.set_xticks(np.arange(nbRow))
    ax.set_yticks(np.arange(nbCol))

    plt.show()

#-------------------
def plotRobEnv(rob):
    # robMaptoPlot = rob.map.copy()
    robMaptoPlot = []
    line = []
    for i in range(rob.nbRow):
        line = []
        for j in range(rob.nbCol):
            line.append(0)
        robMaptoPlot.append(line)

    # Fill the new map with the robot data
    for i in range(rob.nbRow):
        for j in range(rob.nbCol):
            robMaptoPlot[i][j] = rob.map[i][j]

    for index in rob.path:
        robMaptoPlot[index[0]][index[1]] = 1
    robMaptoPlot[rob.rowGoal][rob.colGoal] = -2
    robMaptoPlot[rob.row][rob.col] = -3

    # create discrete colormap
    cmap = colors.ListedColormap(['blue','green','black','white','yellow'])
    bounds = [-3,-2,-1,0,1,2]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(robMaptoPlot, cmap=cmap, norm=norm)

    ax.set_xticks(np.arange(rob.nbRow))
    ax.set_yticks(np.arange(rob.nbCol))

    plt.show()