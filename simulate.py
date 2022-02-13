import pybullet as p
import time
import pybullet_data
from generate import *
import pyrosim.pyrosim as pyrosim
i = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
worldId = p.loadSDF("world.sdf")


for x in range(50000):
    p.stepSimulation()
    Create_Robot()
    time.sleep(1 / 60)

p.disconnect()
