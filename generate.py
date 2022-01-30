import pyrosim.pyrosim as pyrosim 

l = 1
w = 1
h = 1
x = 0
y = 0
z = 0.5



pyrosim.Start_SDF("boxes.sdf")

for y in range(10):
    y = -1
    l-=0.05
    w-=0.05
    h-=0.05
    for j in range(5):
        x=-1.1
        y+=1.1
        z+=1.1
        for i in range(5):
            x+=1.1
            pyrosim.Send_Cube(name = "Box", pos=[x,y,z] , size=[l,w,h])
                      
            

           
        
        

        
            

           
    
       
        
            

pyrosim.End()

