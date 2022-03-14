import pybullet as p
import time
import pybullet_data

import numpy
import constants as c
import pyrosim.pyrosim

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        for i in range(0, c.length):
            time.sleep(1 / 600)



            #c.valuesF.append(c.amplitudeF * numpy.sin(c.graphline[i] * c.frequencyF + c.phaseOffsetF) * numpy.pi / 8)
            #c.valuesB.append(c.amplitudeB * numpy.sin(c.graphline[i] * c.frequencyB + c.phaseOffsetB) * numpy.pi / 10)

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            #pyrosim.Set_Motor_For_Joint(bodyIndex=r.robotId,
            #                            jointName="Torso_BackLeg",
            #                            controlMode=p.POSITION_CONTROL,
            #                            targetPosition=c.valuesB[i],
            #                            maxForce=50)

            #pyrosim.Set_Motor_For_Joint(bodyIndex=r.robotId,
            #                            jointName="Torso_FrontLeg",
            #                            controlMode=p.POSITION_CONTROL,
            #                            targetPosition=c.valuesF[i],
            #                            maxForce=50)

    def __del__(self):
        p.disconnect()
