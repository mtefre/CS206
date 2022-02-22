import pybullet as p
import pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.motors = MOTOR()

    def Prepare_To_Sense(self):
        self.sensors = SENSOR()
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


