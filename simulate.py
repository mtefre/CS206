import pybullet as p
import time
import pybullet_data
from generate import *
import pyrosim.pyrosim as pyrosim
i = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.9)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
worldId = p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

for x in range(50000):
    Create_Robot()
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegTouch)
    time.sleep(1 / 60)

p.disconnect()
