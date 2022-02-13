import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load('data/SensorValues.npy')
frontLegSensorValues = numpy.load('data/FrontSensors.npy')

plt.plot(backLegSensorValues, label="BackLeg", linewidth=2.8)
plt.plot(frontLegSensorValues, label="FrontLeg")
plt.legend(loc='upper right')
plt.show()

