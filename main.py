# Universidade Federal de Pernambuco
# ME653 Programacao Robotica
# 2021.1
# Alana Ingrid Fernandes Costa da Silva e Edgleyson Pereira da Silva
# Projeto 1

from numpy import*
from random import randrange
from plotLib import plotRealEnv, plotRobEnv, plotPlanningMap

class envClass:

    def __init__(self, nbRow, nbCol):
        self.nbRow = nbRow
        self.nbCol = nbCol
        self.map = zeros((nbRow,nbCol)) #cria matriz[nbRow x nbCol] representando o ambiente

    def addObstacle(self, row, col):
        self.map[row][col] = -1

    def removeObstacle(self, row, col):
        self.map[row][col] = 0


class robotClass:

    def __init__(self, nbRow, nbCol, robotRow, robotCol, sensorRange):
        self.nbRow = nbRow
        self.nbCol = nbCol
        self.row = robotRow
        self.col = robotCol
        self.map = zeros((nbRow,nbCol))
        self.sensorRange = sensorRange
        self.path = []

    def setGoal(self, goalRow, goalCol):
        self.goalRow = goalRow
        self.goalCol = goalCol

    def updateMap(self, refreshMap):
        for i in range(-self.sensorRange, self.sensorRange+1):
            for j in range(-self.sensorRange, self.sensorRange+1):
                row = self.row + i
                col = self.col + j
                if row < self.nbRow and col < self.nbCol:
                    self.map[row][col] = refreshMap[row][col]

    def pathPlanner(self):
        pathMap = self.map.copy()
        value = 1
        n = 1
        if self.nbRow > self.nbCol:
            maxCel = 2*self.nbRow - 1
        elif self.nbCol > self.nbRow:
            maxCel = 2*self.nbCol -1
        else:
            maxCel = 2*self.nbRow - 1
        pathMap[self.goalRow, self.goalCol] = value
        while n < maxCel:
            for i in range(self.nbRow):
                for j in range(self.nbCol):
                    if pathMap[i][j] == value and i != 0 and pathMap[i-1][j] == 0:
                        pathMap[i-1][j] = value + 1
                    if pathMap[i][j] == value and i != self.nbRow - 1 and pathMap[i+1][j] == 0:
                        pathMap[i+1][j] = value + 1
                    if pathMap[i][j] == value and j != 0 and pathMap[i][j-1] == 0:
                        pathMap[i][j-1] = value + 1
                    if pathMap[i][j] == value and j != self.nbCol - 1 and pathMap[i][j+1] == 0:
                        pathMap[i][j+1] = value + 1
            value = value + 1
            n = n + 1
        rowPosition = self.row
        colPosition = self.col
        robotPosition = pathMap[self.row][self.col]
        while robotPosition != 1:
            if pathMap[rowPosition - 1][colPosition] == robotPosition - 1 and self.map[rowPosition - 1][colPosition] != -1:
               robotPosition = pathMap[rowPosition - 1][colPosition]
               self.path.append((rowPosition - 1, colPosition))
               rowPosition = rowPosition - 1

            if pathMap[rowPosition + 1][colPosition] == robotPosition - 1 and self.map[rowPosition + 1][colPosition] != -1:
               robotPosition = pathMap[rowPosition + 1][colPosition]
               self.path.append((rowPosition + 1, colPosition))
               rowPosition = rowPosition + 1

            if pathMap[rowPosition][colPosition - 1] == robotPosition - 1 and self.map[rowPosition][colPosition - 1] != -1:
               robotPosition = pathMap[rowPosition][colPosition - 1]
               self.path.append((rowPosition, colPosition - 1))
               colPosition = colPosition - 1

            if pathMap[rowPosition][colPosition + 1] == robotPosition - 1 and self.map[rowPosition][colPosition + 1] != -1:
                robotPosition = pathMap[rowPosition][colPosition + 1]
                self.path.append((rowPosition, colPosition + 1))
                colPosition = colPosition + 1
        # To plot grid filled with numbers:
        # func: plotPlanningMap(arg1. arg2, arg3)
        # arg1: matrix object representing the grid filled with values
        # arg2: number of row
        # arg3: number of col

    def move(self, path):
        movement = path[0]
        moveRow = movement[0]
        moveCol = movement[1]
        self.row = moveRow
        self.Col = moveCol




#----------------------------------------------


# MAIN FUNCTION

# To plot the real environment with the robot position
# func: plotRealEnv(arg1,arg2)
# arg1: object type envClass
# arg2: object type robotClass

# To plot the environment known by the robot and the computed path
# func: plotRobEnv(arg1)
# arg1: object type robotClass