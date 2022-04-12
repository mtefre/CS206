
import numpy


length = 600

numSensorNeurons = 9
numMotorNeurons = 12

motorJointRange = 0.3

amplitudeF = numpy.pi/2
frequencyF = 20
phaseOffsetF = numpy.pi/2

amplitudeB = numpy.pi/4
frequencyB = 10
phaseOffsetB = numpy.pi/2

graphline = numpy.linspace(0, 2*numpy.pi, length)

numberOfGenerations = 20

populationSize = 10