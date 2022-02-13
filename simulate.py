import pybullet as p
import time
import pybullet_data
from generate import *
import pyrosim.pyrosim as pyrosim
import numpy
import os

i = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
worldId = p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(500)
frontLegSensorValues = numpy.zeros(500)


for x in range(500):
    create_robot()
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(backLegSensorValues)
    print(frontLegSensorValues)
    time.sleep(1 / 1000)

numpy.save(os.path.join('data', "SensorValues"), backLegSensorValues)
numpy.save(os.path.join('data', "FrontSensors"), frontLegSensorValues)

p.disconnect()
