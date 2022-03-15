import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.length)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeB
        self.frequency = c.frequencyB
        self.offset = c.phaseOffsetB

        if(self.jointName == "Torso_BackLeg"):
            self.motorValues = self.amplitude * numpy.sin((self.frequency/2) * c.graphline + self.offset)
        else:
            self.motorValues = self.amplitude * numpy.sin(self.frequency * c.graphline + self.offset)

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot,
                            jointName=self.jointName,
                            controlMode=p.POSITION_CONTROL,
                            targetPosition=desiredAngle,
                            maxForce=50)

