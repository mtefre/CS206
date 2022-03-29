import pybullet as p
import time
import pybullet_data

import numpy
import constants as c
import pyrosim.pyrosim

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGui, SolutionID):
        self.ID = SolutionID
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)


        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT(SolutionID)



    def Run(self):
        for i in range(0, c.length):
            time.sleep(1 / 200)

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()

    def Get_Fitness(self):
        self.robot.Get_Fitness(self.ID)

    def __del__(self):
        p.disconnect()
