import random
import time
import constants as c
import numpy as np
import os


import pyrosim.pyrosim as pyrosim

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = str(nextAvailableID)

    def Set_ID(self, assignedID):
        self.myID = assignedID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="box", pos=[1, 3, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg",parent="Torso",child="FrontLeg",type="revolute",position=[0, 0.5, 1.0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg",parent="Torso",child="BackLeg",type="revolute",position=[0, -0.5, 1.0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",position=[-0.5, -0.3, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1,0.2,0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",position=[0.5, 0.3, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",position=[0, 1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",position=[0, -1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # New Legs
        pyrosim.Send_Joint(name="Torso_LeftLeftLeg", parent="Torso", child="LeftLeftLeg", type="revolute", position=[-0.5, 0.3, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        #
        pyrosim.Send_Joint(name="LeftLeftLeg_LowerLeftLeftLeg", parent="LeftLeftLeg", child="LeftLeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        #
        #
        pyrosim.Send_Joint(name="Torso_RightRightLeg", parent="Torso", child="RightRightLeg", type="revolute", position=[0.5, -0.3, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightRightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        #
        pyrosim.Send_Joint(name="RightRightLeg_LowerRightRightLeg", parent="RightRightLeg", child="RightRightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightRightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])


        pyrosim.End()


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_BackLeg")

        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_LeftLeftLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_RightRightLeg")

        pyrosim.Send_Motor_Neuron(name=15, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="BackLeg_BackLowerLeg")

        pyrosim.Send_Motor_Neuron(name=17, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=18, jointName="RightLeg_RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=19, jointName="LeftLeftLeg_LowerLeftLeftLeg")
        pyrosim.Send_Motor_Neuron(name=20, jointName="RightRightLeg_LowerRightRightLeg")

        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 9, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()


    def Start_Simulation(self, directOrGui):
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py {} {}".format(directOrGui, self.myID))
        #os.system("start /B python simulate.py "+directOrGui+" "+self.myID)

    def Waiting_For_Simulation_To_End(self):
        fitnessFileName = "fitness{}.txt".format(self.myID)
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        file = open("fitness{}.txt".format(self.myID), "r")
        self.fitness = float(file.read())
        file.close()

        os.system('del fitness{}.txt'.format(self.myID))


    def Mutate(self):
        row = random.randint(0,self.weights.shape[0] - 1)
        col = random.randint(0,self.weights.shape[1] - 1)
        self.weights[row][col] = random.random() * 2 - 1















