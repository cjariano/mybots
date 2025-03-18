from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        for parent in self.parents.values():
            parent.Evaluate("GUI")

        # for currentGeneration in range(c.numberOfGenerations-1):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}  # Store new children separately

        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])  # Clone parent
            self.children[i].Set_ID(self.nextAvailableID)  # Assign new ID
            self.nextAvailableID += 1  # Increment after assignment

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")