import pybullet as p
import time 
i = 0

physicsClient = p.connect(p.GUI)

for x in range(1000):
    p.stepSimulation()
    time.sleep(1/200)
    i += 1
    print(i)
    
p.disconnect()