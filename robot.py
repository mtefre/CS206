import os.path
import os
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import numpy
import constants as c

class ROBOT:

    def __init__(self, SolutionID):
        self.SolutionId = SolutionID
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(SolutionID))
        os.system("del brain{}.nndf".format(self.SolutionId))

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)



    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = (self.nn.Get_Value_Of(neuronName) * c.motorJointRange)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)


    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self, Id):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xCooridnateOfLinkZero = basePosition[0] * -1
        #print(positionLinkOfZero[0], xCooridnateOfLinkZero[1])
        f = open("fitness{}.txt".format(str(Id)), "w")
        f.write(str(xCooridnateOfLinkZero))











