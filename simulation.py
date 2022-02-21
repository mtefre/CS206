import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.world = WORLD()

        p.setGravity(0, 0, -9.8)
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        pyrosim.Prepare_To_Simulate()
