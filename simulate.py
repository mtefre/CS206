import pybullet as p
import time 
i = 0

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.9)
p.loadSDF("box.sdf")
for x in range(1000):
    p.stepSimulation()
    time.sleep(1/50)
    i += 1
    print(i)
    
p.disconnect()