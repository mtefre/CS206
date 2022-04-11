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
            self.Evolve_For_One_Generation('DIRECT')


    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.childeren, directOrGUI)
        self.Print()
        self.Select()

    def Spawn(self):
        self.childeren = {}
        self.nextID = 0
        for key in self.parents:
            self.childeren[key] = copy.deepcopy(self.parents[key])
            self.childeren[key].Set_ID(self.nextID)
            self.nextID +=1

    def Mutate(self):
        for child in self.childeren:
            self.childeren[child].Mutate()

    def Select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness < self.childeren[key].fitness:
                self.parents[key] = self.childeren[key]

    def Show_Best(self):
        best_loc = 0
        best_fit = 1000
        for parent in self.parents.keys():
            if self.parents[parent].fitness > best_fit:
                best_loc = parent
                best_fit = self.parents[parent].fitness

        self.parents[best_loc].Start_Simulation('GUI')
        print("Best Fitness: ", self.parents[best_loc].fitness)
        #self.parent.Evaluate(self.string2)

    def Evaluate(self, solutions, gui):
        for i in solutions:
            solutions[i].Start_Simulation(gui)
        for i in solutions:
            solutions[i].Waiting_For_Simulation_To_End()


    def Print(self):
        print("")
        for parent in self.parents:
            print("parent: " + str(self.parents[parent].fitness) + " child: " + str(self.childeren[parent].fitness))
        print("")