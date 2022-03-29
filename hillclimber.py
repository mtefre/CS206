from solution import SOLUTION
import constants as c
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        self.Evolve()

    def Evolve(self):
        self.string = "DIRECT"
        self.string2 = "GUI"
        self.parent.Evaluate(self.string2)

        for currentGeneretaion in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(self.string)
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent.fitness = self.child.fitness

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate(self.string2)


