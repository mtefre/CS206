import pybullet as p
import time
import pybullet_data
import random
import pyrosim.pyrosim as pyrosim
import numpy
import os

length = 2000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
worldId = p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
amplitudeF = numpy.pi/2
frequencyF = 20
phaseOffsetF = numpy.pi/2

amplitudeB = numpy.pi/2
frequencyB = 5
phaseOffsetB = 0

backLegSensorValues = numpy.zeros(length)
frontLegSensorValues = numpy.zeros(length)

graphline = numpy.linspace(0, 2*numpy.pi, length)
valuesF = []
valuesB = []


for i in range(0, length):
    time.sleep(1 / 600)

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    valuesF.append(amplitudeF * numpy.sin(graphline[i] * frequencyF + phaseOffsetF) * numpy.pi/8)
    valuesB.append(amplitudeB * numpy.sin(graphline[i] * frequencyB + phaseOffsetB) * numpy.pi/10)

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


numpy.save(os.path.join('data', "SensorValues"), backLegSensorValues)
numpy.save(os.path.join('data', "FrontSensors"), frontLegSensorValues)

p.disconnect()
