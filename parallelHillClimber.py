from solution import SOLUTION
import os
import constants as c
import copy
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #self.parent = SOLUTION()
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0

        for entry in range(0, c.populationSize):
            self.parents[entry] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents, "DIRECT")



        #self.string = "DIRECT"
        #self.string2 = "GUI"
        #self.parent.Evaluate(self.string)

        for currentGeneretaion in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.childeren, "DIRECT")
        #self.Print()
        #self.Select()

    def Spawn(self):
        self.childeren = {}
        for key in self.parents:
            self.childeren[key] = copy.deepcopy(SOLUTION)
            self.childeren[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1

    def Evaluate(self, solutions, gui):
        for i in solutions:
            self.parents[i].Start_Simulation(gui)

        for i in solutions:
            self.parents[i].Waiting_For_Simulation_To_End()



    def Mutate(self):
        for i in self.childeren:
            self.childeren[i].Mutate()

    def Select(self):
        if self.parents.fitness > self.child.fitness:
            self.parents = self.child

    def Print(self):
        pass
        #print(self.parents.fitness, self.child.fitness)

    def Show_Best(self):
        pass
        #self.parent.Evaluate(self.string2)