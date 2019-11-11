from operator import attrgetter
import random, sys, time, copy
import numpy as np
import math
from geopy.distance import geodesic
from matplotlib import pyplot as plt


class Graph:

    def __init__(self, amount_vertices):
        self.edges = {}
        self.vertices = set()
        self.amount_vertices = amount_vertices

    def existsEdge(self, src, dest):
        return (True if (src, dest) in self.edges else False)

    def addEdge(self, src, dest, cost=0):

        if not self.existsEdge(src, dest):
            self.edges[(src, dest)] = cost
            self.vertices.add(src)
            self.vertices.add(dest)

    def showGraph(self):
        print('DISTANCES BETWEEN VARIOUS CITIES:\n')
        for edge in self.edges:
            print('distance btw %d and %d -> %d' % (edge[0], edge[1], self.edges[edge]))

    def calculatecost(self,i,j):
     totalcost = 0

     c = i
     d = j
     c = c - 12341
     d = d - 12341
     c = int(c)
     d = int(d)

     loc1 = (latitude[c], longitude[c])
     loc2 = (latitude[d], longitude[d])
     b = (geodesic(loc1, loc2).km)

     totalcost = totalcost + b

     return totalcost

    def getCostPath(self, path):

     total_cost = 0
     self.amount_vertices = customerno-1
     for i in range(customerno - 2):
         total_cost += self.edges[(path[i], path[i + 1])]

     total_cost += self.edges[(path[customerno - 2], path[0])]
     return total_cost

    def getRandomPaths(self, max_size):

        random_paths, list_vertices = [], list(self.vertices)

        initial_vertice = random.choice(list_vertices)

        list_vertices.remove(initial_vertice)
        list_vertices.insert(0, initial_vertice)

        for i in range(max_size):
            list_temp = list_vertices[1:]
            random.shuffle(list_temp)
            list_temp.insert(0, initial_vertice)

            if list_temp not in random_paths:
                random_paths.append(list_temp)

        return random_paths


class CompleteGraph(Graph):

    def generates(self):
        for i in range(self.amount_vertices):
            for j in range(self.amount_vertices):
                if i != j:
                    weight = random.randint(1, 10)
                    self.addEdge(i, j, weight)


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

    def __init__(self, graph, iterations, size_population, beta=1, alfa=1):
        self.graph = graph  # the graph
        self.iterations = iterations
        self.size_population = size_population
        self.particles = []
        self.beta = beta
        self.alfa = alfa

        solutions = self.graph.getRandomPaths(self.size_population)

        for solution in solutions:
            particle = Particle(solution=solution, cost=graph.getCostPath(solution))

            self.particles.append(particle)

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

    def plot(self, line_width=1, point_radius=math.sqrt(2.0), annotation_size=8, dpi=120, save=True, name=None):
        
        finalpath=[]
        for i in self.getGBest().getPBest():
           obj=int(i)
           obj=obj-12341
           finalpath.append(obj)
        
        x = [latitude[i] for i in sorted(finalpath)]
        x.append(x[0])
        y = [longitude[i] for i in sorted(finalpath)]
        y.append(y[0])
        plt.plot(x, y, linewidth=line_width)
        plt.scatter(x, y, s=math.pi * (point_radius ** 2.0))
        
        n=[]
        for i in range(customerno-1):
            n.append(i+1+12341)
        for i, txt in enumerate(n):
            plt.annotate(txt, (x[i], y[i]))
        if save:
            
            plt.savefig(name, dpi=dpi)
        plt.show()
        plt.gcf().clear()
    def run(self):

        for t in range(self.iterations):

            self.gbest = min(self.particles, key=attrgetter('cost_pbest_solution'))

            for particle in self.particles:

                particle.clearVelocity()
                temp_velocity = []
                solution_gbest = copy.copy(self.gbest.getPBest())
                solution_pbest = particle.getPBest()[:]
                solution_particle = particle.getCurrentSolution()[
                                    :]

                for i in range(self.graph.amount_vertices):
                    if solution_particle[i] != solution_pbest[i]:
                        swap_operator = (i, solution_pbest.index(solution_particle[i]), self.alfa)

                        temp_velocity.append(swap_operator)

                        aux = solution_pbest[swap_operator[0]]
                        solution_pbest[swap_operator[0]] = solution_pbest[swap_operator[1]]
                        solution_pbest[swap_operator[1]] = aux

                for i in range(self.graph.amount_vertices):
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

                cost_current_solution = self.graph.getCostPath(solution_particle)

                particle.setCostCurrentSolution(cost_current_solution)

                if cost_current_solution < particle.getCostPBest():
                    particle.setPBest(solution_particle)
                    particle.setCostPBest(cost_current_solution)
                # particle.calculatefinal(particle.getPbest)
def calculatefinal(lastbest,popsize):
 
        j=0
        penaltycost=0
        for i in range(int(vehicleno)):
 
   
           print("Vehicle number",i+1," ==>")
           cap=capacity[i]
           count=0
           while(cap>0):
              custindex=lastbest[j]
              custid=int(custindex)
              custindex=int(custindex)-12341
              check=cap-int(amtordered[custindex])
              if(check<0):
                 break
      
              if(count>1):
                 if(int(time[custindex])==0):
                    penaltycost=penaltycost+penalty[custindex]
      
              cap=cap-int(amtordered[custindex])
              print(custid,"--",amtordered[custindex],"--")
              j=j+1
              p=popsize-1
              if(j>p):
                 break
              count=count+1
           if(j>p):
               break
        return penaltycost



import xlrd


loc = ("/home/sakshi/minorpro2/instance1.xlsx")

 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

customerno = sheet.nrows - 1

idno = []

for i in range(customerno + 1):
         if (i != 0):
            obj1 = sheet.cell_value(i, 0)
            idno.append(obj1)
latitude = []
longitude = []
amtordered = []
penalty = []
time = []

for i in range(customerno + 1):
         if (i != 0):
            obj1 = sheet.cell_value(i, 1)
            latitude.append(obj1)
for i in range(customerno + 1):
         if (i != 0):
            obj1 = sheet.cell_value(i, 2)
            longitude.append(obj1)
for i in range(customerno + 1):
         if (i != 0):
            obj1 = sheet.cell_value(i, 3)
            amtordered.append(obj1)
for i in range(customerno + 1):
         if (i != 0):
            obj1 = sheet.cell_value(i, 4)
            time.append(obj1)
for i in range(customerno + 1):
         if (i != 0):
            obj1 = sheet.cell_value(i, 6)
            penalty.append(obj1)

vehicleno = sheet.cell_value(1, 5)
vehicleno=sheet.cell_value(1,5)
capacity=[]

l=1
vehicleno=int(vehicleno)
for i in range(vehicleno):
       obj1=sheet.cell_value(l,7)
       capacity.append (obj1)
       l=l+1

c=sheet.nrows-1

def main(beta,alpha):
     
     
     graph = Graph(amount_vertices=sheet.nrows)
     i=0
     j=0
   
     for i in range(customerno - 1):
         for j in range(customerno-1):
             graph.addEdge(idno[i],idno[j],graph.calculatecost(idno[i],idno[j]))
     graph.showGraph()

     pso = PSO(graph, iterations=40, size_population=40, beta=beta, alfa=alpha)
     pso.run() 

     pso.showsParticles()
     pso.plot()
 
     print('global_best(final route): %s -> cost(minimum possible cost): %d\n' % (pso.getGBest().getPBest(), pso.getGBest().getCostPBest()))
     final_route=[]
     final_route=pso.getGBest().getPBest()
     
     penaltycost=calculatefinal(final_route,customerno-1)
     
    
     print("AND THE FINAL COST FOR OUR SOLUTION IS")
     print(penaltycost+pso.getGBest().getCostPBest())
