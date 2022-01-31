import pyrosim.pyrosim as pyrosim 

l = 1
w = 1
h = 1
x = 0
y = 0
z = 0.5


def Create_World():
    pyrosim.Start_SDF("world.sdf")
  
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name = "Torso", pos=[0,0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5,0,0.5])
    pyrosim.Send_Cube(name = "BackLeg", pos=[0.5,0,1] , size=[1,1,1])
    pyrosim.Send_Joint( name = "BackLeg_FrontLeg" , parent= "BackLeg" , child = "FrontLeg" , type = "revolute", position = [0.5,0,0])
    pyrosim.Send_Cube(name = "FrontLeg", pos=[1,0,0] , size=[1,1,1])

    pyrosim.End()
