import sys

from simulation import SIMULATION

directOrGui = sys.argv[1]
SolutionID = sys.argv[2]
simulation = SIMULATION(directOrGui, SolutionID)
simulation.Run()
simulation.Get_Fitness()
