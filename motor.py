import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.motorValues = numpy.zeros(c.length)
        self.jointName = jointName


    def Set_Value(self, robot, desiredAngle):

        pyrosim.Set_Motor_For_Joint(bodyIndex=robot,
                            jointName=self.jointName,
                            controlMode=p.POSITION_CONTROL,
                            targetPosition= (desiredAngle),
                            maxForce=25)

