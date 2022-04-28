
import numpy


length = 1000

numSensorNeurons = 8
numMotorNeurons = 12

motorJointRange = 0.2

amplitudeF = numpy.pi/2
frequencyF = 20
phaseOffsetF = numpy.pi/2

amplitudeB = numpy.pi/4
frequencyB = 10
phaseOffsetB = numpy.pi/2

graphline = numpy.linspace(0, 2*numpy.pi, length)

numberOfGenerations = 10

populationSize = 10