import math
import random
from matplotlib import pyplot as plt
import numpy as np
from geopy.distance import geodesic
import xlrd
from operator import attrgetter
import time
import copy
costt=0

def calculatecosttt(self,i,j):
     totalcost = 0

     c = i
     d = j
     c = int(c)
     d = int(d)

     loc1 = (latitude[c], longitude[c])
     loc2 = (latitude[d], longitude[d])
     b = (geodesic(loc1, loc2).km)

     totalcost = totalcost + b

     return totalcost
    
def findindex(obj,p2,popsize):
    
    for j in range(popsize):
      if(p2[j]==obj):
        return j
def assignvehicles(p1,capacity,maxvehicles,demand,readytime,duedate,servicetime):
 customerno=101
 route = np.zeros((maxvehicles+1,customerno))
 for i in range(maxvehicles):
     currentcapacity[i]=capacity
      
 curveh=1
 customerno=100
 for i in range(customerno):
   
   ide=p1[i]
   assigned=0
   demand=demand.astype(int)
   dem=demand[ide-1]
   curveh=1
  
   while(assigned!=1):
     
     
     if dem<currentcapacity[curveh][0] and elapsedtime[curveh][0]<duedate[ide-1]:
        popsize=customerno
        i1=findindex(0,route[curveh],popsize)
        route[curveh][i1]=ide
        elapsedtime[curveh][0]=elapsedtime[curveh][0]+readytime[ide-1]+servicetime[ide-1]
        currentcapacity[curveh][0]=currentcapacity[curveh][0]-dem
        assigned=1
        route=route.astype(int)
     if(curveh<20):
      curveh=curveh+1
     else:
      break
 print("route")
 print(route)

 return route


   

def calculatedistcost(route,popsize):
 distancecost=0
 
 
 for i in range(maxvehicles):
   subroute=route[i]
   j=0
   c=subroute[j]
   d=subroute[j+1]
        
        
   c = int(c) 
   d = int(d) 
   loc1=(latitude[c-1],longitude[c-1])
   loc2=(latitude[d-1],longitude[d-1])
   b=(geodesic(loc1,loc2).km)
   distancecost=distancecost+b
 
 return distancecost

def calculatefinal(p1,customerno):
   for i in range(maxvehicles):
     elapsedtime[i]=0
   route=assignvehicles(p1,capacity,maxvehicles,demand,readytime,duedate,servicetime)
   distancecost=calculatedistcost(route,customerno)
   timecost=np.sum(elapsedtime)
   totalcost=distancecost+timecost
   
   return totalcost

global current
class Particle:

    def __init__(self, solution, cost):
        self.solution = solution

        self.pbest = solution

        self.cost_current_solution = cost
        self.cost_pbest_solution = cost

        self.velocity = []

    def setPBest(self, new_pbest):
        self.pbest = new_pbest

    def getPBest(self):
        return self.pbest

    def setVelocity(self, new_velocity):
        self.velocity = new_velocity

    def getVelocity(self):
        return self.velocity

    def setCurrentSolution(self, solution):
        self.solution = solution

    def getCurrentSolution(self):
        return self.solution

    def setCostPBest(self, cost):
        self.cost_pbest_solution = cost

    def getCostPBest(self):
        return self.cost_pbest_solution

    def setCostCurrentSolution(self, cost):
        self.cost_current_solution = cost

    def getCostCurrentSolution(self):
        return self.cost_current_solution

    def clearVelocity(self):
        del self.velocity[:]

    
class PSO:
    
    def __init__(self,ants, iterations, size_population, beta=1, alfa=1):
        
        self.iterations = iterations
        self.size_population = size_population
        self.particles = []
        self.beta = beta
        self.alfa = alfa
       
    def add (self, tour, costly):
        particle = Particle(solution=tour, cost=costly)
        self.particles.append(particle)
        current=costly
        self.size_population = len(self.particles)

    def setGBest(self, new_gbest):
        self.gbest = new_gbest

    def getGBest(self):
        return self.gbest

    def showsParticles(self):

        print('\nALL POSSIBLE ROUTES\n')
        for particle in self.particles:
            print('pbest: %s\t->\tcost pbest: %d\t|\tcurrent solution: %s\t->\tcost current solution: %d' \
                  % (str(particle.getPBest()), particle.getCostPBest(), str(particle.getCurrentSolution()),
                     particle.getCostCurrentSolution()))
        print('')



    def run2(self):

        for t in range(self.iterations):

            self.gbest = min(self.particles, key=attrgetter('cost_pbest_solution'))

            for particle in self.particles:

                particle.clearVelocity()
                temp_velocity = []
                solution_gbest = copy.copy(self.gbest.getPBest())
                solution_pbest = particle.getPBest()[:]
                solution_particle = particle.getCurrentSolution()[
                                    :]

                for i in range(customerno-1):
                    if solution_particle[i] != solution_pbest[i]:
                        swap_operator = (i, solution_pbest.index(solution_particle[i]), self.alfa)

                        temp_velocity.append(swap_operator)

                        aux = solution_pbest[swap_operator[0]]
                        solution_pbest[swap_operator[0]] = solution_pbest[swap_operator[1]]
                        solution_pbest[swap_operator[1]] = aux

                for i in range(customerno-1):
                    if solution_particle[i] != solution_gbest[i]:
                        swap_operator = (i, solution_gbest.index(solution_particle[i]), self.beta)

                        temp_velocity.append(swap_operator)

                        aux = solution_gbest[swap_operator[0]]
                        solution_gbest[swap_operator[0]] = solution_gbest[swap_operator[1]]
                        solution_gbest[swap_operator[1]] = aux

                particle.setVelocity(temp_velocity)

                for swap_operator in temp_velocity:
                    if random.random() <= swap_operator[2]:
                        aux = solution_particle[swap_operator[0]]
                        solution_particle[swap_operator[0]] = solution_particle[swap_operator[1]]
                        solution_particle[swap_operator[1]] = aux

                particle.setCurrentSolution(solution_particle)

                cost_current_solution = particle.getCostCurrentSolution()

                particle.setCostCurrentSolution(cost_current_solution)

                if cost_current_solution < particle.getCostPBest():
                    particle.setPBest(solution_particle)
                    particle.setCostPBest(cost_current_solution)
                    particle.calculatefinal(particle.getPbest)
                print('pbest: %s\t->\tcost pbest: %d\t|\tcurrent solution: %s\t->\tcost current solution: %d' \
                  % (str(particle.getPBest()), particle.getCostPBest(), str(particle.getCurrentSolution()),
                     particle.getCostCurrentSolution()))
        print('')
class SolveVRPUsingACO:
    class Edge:
        def __init__(self, a, b, weight, initial_pheromone):
            self.a = a
            self.b = b
            self.weight = weight
            self.pheromone = initial_pheromone

    class Ant:
        def __init__(self, alpha, beta, num_nodes, edges):
            self.alpha = alpha
            self.beta = beta
            self.num_nodes = num_nodes
            self.edges = edges
            self.tour = None
            self.distance = 0.0

        def _select_node(self):
            roulette_wheel = 0.0
            unvisited_nodes = [node for node in range(self.num_nodes) if node not in self.tour]
            heuristic_total = 0.0
            for unvisited_node in unvisited_nodes:
                heuristic_total += self.edges[self.tour[-1]][unvisited_node].weight
            for unvisited_node in unvisited_nodes:
                roulette_wheel += pow(self.edges[self.tour[-1]][unvisited_node].pheromone, self.alpha) * \
                                  pow((heuristic_total / self.edges[self.tour[-1]][unvisited_node].weight), self.beta)
            random_value = random.uniform(0.0, roulette_wheel)
            wheel_position = 0.0
            for unvisited_node in unvisited_nodes:
                wheel_position += pow(self.edges[self.tour[-1]][unvisited_node].pheromone, self.alpha) * \
                                  pow((heuristic_total / self.edges[self.tour[-1]][unvisited_node].weight), self.beta)
                if wheel_position >= random_value:
                    return unvisited_node

        def find_tour(self):
            self.tour = [random.randint(0, self.num_nodes - 1)]
            while len(self.tour) < self.num_nodes:
                self.tour.append(self._select_node())
            return self.tour

        def get_distance(self):
            self.distance = 0.0
            for i in range(self.num_nodes):
                self.distance += self.edges[self.tour[i]][self.tour[(i + 1) % self.num_nodes]].weight
            return self.distance

    def __init__(self, mode='ACS', colony_size=200, elitist_weight=1.0,alpha=1.0, beta=3.0,
                 rho=0.1, pheromone_deposit_weight=1.0, initial_pheromone=1.0, steps=50, nodes=None, labels=None):
        self.mode = mode
        self.colony_size = colony_size
        self.elitist_weight = elitist_weight
        self.rho = rho
        self.pheromone_deposit_weight = pheromone_deposit_weight
        self.steps = steps
        self.num_nodes = len(nodes)
        self.nodes = nodes
        if labels is not None:
            self.labels = labels
        else:
            self.labels = range(1, self.num_nodes + 1)
        self.edges = [[None] * self.num_nodes for _ in range(self.num_nodes)]
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                self.edges[i][j] = self.edges[j][i] = self.Edge(i, j, math.sqrt(
                    pow(self.nodes[i][0] - self.nodes[j][0], 2.0) + pow(self.nodes[i][1] - self.nodes[j][1], 2.0)),
                                                                initial_pheromone)
        self.ants = [self.Ant(alpha, beta, self.num_nodes, self.edges) for _ in range(self.colony_size)]
        self.global_best_tour = None
        self.global_best_distance = float("inf")

    def _add_pheromone(self, tour, distance, weight=1.0):
        pheromone_to_add = self.pheromone_deposit_weight / distance
        for i in range(self.num_nodes):
            self.edges[tour[i]][tour[(i + 1) % self.num_nodes]].pheromone += weight * pheromone_to_add

   

    def _elitist(self):
        
        for step in range(self.steps):
            for ant in self.ants:
                pso = PSO( self.ants,iterations=40, size_population=50, beta=0.89, alfa=0.97)
                pso.add(ant.find_tour(), ant.get_distance())
                pso.run2()
            
               
                if ant.distance < self.global_best_distance:
                    self.global_best_tour = pso.getGBest().getPBest()
                    self.global_best_distance = pso.getGBest().getCostPBest()
            self._add_pheromone(pso.getGBest().getPBest(),pso.getGBest().getCostPBest())  
            
            self._add_pheromone(self.global_best_tour, self.global_best_distance, weight=self.elitist_weight)
            for i in range(self.num_nodes):
                for j in range(i + 1, self.num_nodes):
                    self.edges[i][j].pheromone *= (1.0 - self.rho)

    

    def run(self):
        print('Started : {0}'.format(self.mode))
        if self.mode == 'ACS':
            self._acs()
        elif self.mode == 'Elitist':
            self._elitist()
        print('Ended : {0}'.format(self.mode))
        print('Sequence : <- {0} ->'.format(' - '.join(str(self.labels[i]) for i in self.global_best_tour)))
        print('Total distance travelled to complete the tour : {0}\n'.format(round(self.global_best_distance, 2)))
        cost=round(self.global_best_distance, 2)
        finalroute=[]
        k=0
        for i in self.global_best_tour:
             obj=self.labels[i]
             finalroute.append(obj)
             k=k+1
        return finalroute,cost

    def plot(self, line_width=1, point_radius=math.sqrt(2.0), annotation_size=8, dpi=120, save=True, name=None):
        x = [self.nodes[i][0] for i in self.global_best_tour]
        x.append(x[0])
        y = [self.nodes[i][1] for i in self.global_best_tour]
        y.append(y[0])
        plt.plot(x, y, linewidth=line_width)
        plt.scatter(x, y, s=math.pi * (point_radius ** 2.0))
        plt.title(self.mode)
        
        n=[]
        for i in range(customerno-1):
            n.append(i+1)
        for i, txt in enumerate(n):
            plt.annotate(txt, (x[i], y[i]))
        if save:
            if name is None:
                name = '{0}.png'.format(self.mode)
            plt.savefig(name, dpi=dpi)
        plt.show()
        plt.gcf().clear()


import numpy as np
import xlrd
loc=("/home/sakshi/minorpro3/instance2.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
maxvehicles=20
capacity=200
customerno=sheet.nrows-1

idno=[]
elapsedtime = np.zeros((maxvehicles+1,1))
currentcapacity = np.zeros((maxvehicles+1,1))


for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,0)
    obj1=int(obj1)
    idno.append (obj1)
latitude=[]
longitude=[]
demand= np.zeros(customerno, dtype = int) 
readytime=[]
duedate= np.zeros(customerno, dtype = int)
route = np.zeros((maxvehicles+1,customerno))
servicetime=[]
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,1)
    latitude.append (obj1)
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,2)
    longitude.append (obj1)
k=0
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,3)
    demand[k]=obj1
    k=k+1
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,4)
    readytime.append (obj1)

po=0
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,5)
    duedate[po]=obj1
    po=po+1

for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,6)
    servicetime.append (obj1)

def main(_colony_size,_steps): 
     print(customerno)   
     _nodes = [(latitude[i], longitude[i]) for i in range(0, customerno-1)]
     elitist = SolveVRPUsingACO(mode='Elitist', colony_size=_colony_size, steps=_steps, nodes=_nodes)
     ellitistfinalroute=[]
     ellitistfinalroute,ellitistpartial=elitist.run()
     elitist.plot()
     
     
     print("ELLITIST")
     costellitist=calculatefinal(ellitistfinalroute,customerno-1)
   
     print("Cost for Hybrid mode",costellitist)


