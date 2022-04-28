import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load('data/BestFitnessA.npy')


plt.plot(backLegSensorValues, label="Fitness", linewidth=2.8)


plt.legend(loc='center right')
plt.show()

