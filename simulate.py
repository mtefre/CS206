import sys

from simulation import SIMULATION

directOrGui = sys.argv[1]
simulation = SIMULATION(directOrGui)
simulation.Run()
simulation.Get_Fitness()
