import pybullet as p
import time
import pybullet_data

import numpy
import constants as c
import pyrosim.pyrosim

import world as w
import robot as r

class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = w.WORLD()
        self.robot = r.ROBOT()


    def Run(self):
        for i in range(0, c.length):
            time.sleep(1 / 600)

            #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            #c.valuesF.append(c.amplitudeF * numpy.sin(c.graphline[i] * c.frequencyF + c.phaseOffsetF) * numpy.pi / 8)
            #c.valuesB.append(c.amplitudeB * numpy.sin(c.graphline[i] * c.frequencyB + c.phaseOffsetB) * numpy.pi / 10)

            p.stepSimulation()
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
