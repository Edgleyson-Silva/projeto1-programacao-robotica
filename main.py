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

    def pathPlanner(...):

        # To plot grid filled with numbers:
        # func: plotPlanningMap(arg1. arg2, arg3)
        # arg1: matrix object representing the grid filled with values
        # arg2: number of row
        # arg3: number of col

    def move(...):



#----------------------------------------------


# MAIN FUNCTION

# To plot the real environment with the robot position
# func: plotRealEnv(arg1,arg2)
# arg1: object type envClass
# arg2: object type robotClass

# To plot the environment known by the robot and the computed path
# func: plotRobEnv(arg1)
# arg1: object type robotClass