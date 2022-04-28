import numpy
import matplotlib.pyplot as plt

time = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
value = (0.10,0.55,0.99,1.1,1.2,1.1,1.11,1.51,1.641, 2.151, 2.24, 2.24, 2.24, 2.24, 2.24, 2.24, 2.24, 2.24, 2.24,2.24)

backLegSensorValues = numpy.load('data/BestFitnessA.npy')


plt.plot(backLegSensorValues, label="Fitness", linewidth=2.8)


plt.legend(loc='center right')
plt.show()

