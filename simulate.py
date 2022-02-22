import pybullet as p
import time
import pybullet_data

import pyrosim.pyrosim as pyrosim
import numpy
import os
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()


"""""
c.gravity
c.searchPath
c.physicsClient

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
worldId = p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

valuesF = []
valuesB = []


for i in range(0, c.length):
    time.sleep(1 / 600)

    c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    valuesF.append(c.amplitudeF * numpy.sin(c.graphline[i] * c.frequencyF + c.phaseOffsetF) * numpy.pi/8)
    valuesB.append(c.amplitudeB * numpy.sin(c.graphline[i] * c.frequencyB + c.phaseOffsetB) * numpy.pi/10)

    p.stepSimulation()
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=valuesB[i],
                                maxForce=50)

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=valuesF[i],
                                maxForce=50)


numpy.save(os.path.join('data', "SensorValues"), c.backLegSensorValues)
numpy.save(os.path.join('data', "FrontSensors"), c.frontLegSensorValues)

p.disconnect()
"""