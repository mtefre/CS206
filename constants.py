
import numpy


length = 2000


amplitudeF = numpy.pi/2
frequencyF = 20
phaseOffsetF = numpy.pi/2

amplitudeB = numpy.pi/2
frequencyB = 5
phaseOffsetB = 0

backLegSensorValues = numpy.zeros(length)
frontLegSensorValues = numpy.zeros(length)

graphline = numpy.linspace(0, 2*numpy.pi, length)
