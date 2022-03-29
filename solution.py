import random
import time

import numpy as np
import os


import pyrosim.pyrosim as pyrosim

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weight = np.random.rand(3, 2) * 2 - 1
        self.myID = str(nextAvailableID)




    def Set_ID(self, assignedID):
        self.myID = assignedID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="box", pos=[1, 3, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.0, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0.5, 0, 1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[1.5, 0, 1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=self.weight[currentRow][currentColumn])

        pyrosim.End()

    def Start_Simulation(self, directOrGui):
        self.Create_Brain()
        os.system("start /B python simulate.py {} {}".format(directOrGui, self.myID))


    def Waiting_For_Simulation_To_End(self):
        fitnessFileName = "fitness{}.txt".format(self.myID)
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        file = open("fitness{}.txt".format(self.myID), "r")
        self.fitness = float(file.read())
        file.close()
        os.system('del fitness{}.txt'.format(self.myID))


    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,1)
        self.weight[row][col] = random.random() * 2 - 1









