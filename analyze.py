import numpy
import matplotlib.pyplot as plt

time = (0, 10, 20, 30, 40)
data = (1.3, 1.5, 2.4, 3.1, 3.3)

RobotA = numpy.load('data/BestFitnessA.npy')
RobotB = numpy.load('data2/BestFitnessB.npy')

plt.plot(time, data, label= "Test")
plt.plot(RobotA, label="RobotA", linewidth=2.8)
plt.plot(RobotA, label="RobotB", linewidth=0.8)

plt.legend(loc='upper right')
plt.show()

