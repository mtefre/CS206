from solution import SOLUTION
import os
import constants as c
import copy
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #self.parent = SOLUTION()
        os.system('del brain*.nndf')
        os.system('del fitness*.txt')


        self.parents = {}
        self.nextAvailableID = 0

        for entry in range(0, c.populationSize):
            self.parents[entry] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents, 'DIRECT')


        for currentGeneretaion in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Spawn(self):
        self.childeren = {}
        self.nextID = 0
        for key in self.parents:
            self.childeren[key] = copy.deepcopy(self.parents[key])
            self.childeren[key].Set_ID(self.nextID)
            self.nextID +=1

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.childeren, "DIRECT")
        self.Print()
        self.Select()

    def Evaluate(self, solutions, gui):
        for i in solutions:
            solutions[i].Start_Simulation(gui)

        for j in solutions:
            solutions[j].Waiting_For_Simulation_To_End()


    def Mutate(self):
        for child in self.childeren:
            self.childeren[child].Mutate()

    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness > self.childeren[i].fitness:
                self.parents[i] = self.childeren[i]

    def Print(self):
        print("")
        for parent in self.parents:
            print("parent: " + str(self.parents[parent].fitness) + " child: " + str(self.childeren[parent].fitness))
        print("")

    def Show_Best(self):
        best_solution = 0
        for i in range(c.populationSize):
            if self.parents[i].fitness > self.childeren[i].fitness:
                best_solution = 1
        self.parents[best_solution].Start_Simulation('GUI')
        print("Best Fitness: ", self.parents[best_solution].fitness)
        #self.parent.Evaluate(self.string2)