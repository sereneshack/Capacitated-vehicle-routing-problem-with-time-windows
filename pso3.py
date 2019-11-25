from operator import attrgetter
import random, sys, time, copy
import numpy as np
import math
from geopy.distance import geodesic
from matplotlib import pyplot as plt
import time


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
     c = int(c)
     d = int(d)

     loc1 = (latitude[c], longitude[c])
     loc2 = (latitude[d], longitude[d])
     b = (geodesic(loc1, loc2).km)

     totalcost = totalcost + b

     return totalcost
    def getCostPath(self, path):
     print(path)
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
            particle = Particle(solution=solution, cost=calculatefinal(solution,customerno))
            self.amount_vertices = customerno-1
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
           finalpath.append(obj)
        x= np.zeros(customerno-1, dtype = int)
        k=0
        for i in finalpath:
          x[k]=latitude[i-1]
          k=k+1
        y= np.zeros(customerno-1, dtype = int)
        u=0
        for i in finalpath:
          y[u]=longitude[i-1]
          u=u+1
        print(x)
        plt.plot(x, y, linewidth=line_width)
        plt.scatter(x, y, s=math.pi * (point_radius ** 2.0))
        n=[]
        for i in range(customerno-1):
            n.append(i+1)
        for i, txt in enumerate(n):
            plt.annotate(txt, (x[i], y[i]))
        if save:
            
            plt.savefig(name, dpi=dpi)
        plt.show()
        plt.gcf().clear()
    def animate(i):
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        line.set_data(x, y)
        return line,


        anim = animation.FuncAnimation(fig, animate, init_func=init,
        frames=200, interval=20, blit=True)


        anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

        plt.show()
    def run(self):

        for t in range(self.iterations):

            self.gbest = min(self.particles, key=attrgetter('cost_pbest_solution'))

            for particle in self.particles:

                particle.clearVelocity()
                temp_velocity = []
                solution_gbest = copy.copy(self.gbest.getPBest())
                solution_pbest = particle.getPBest()[:]
                solution_particle = particle.getCurrentSolution()[:]
                
                for i in range(self.graph.amount_vertices-3):
                    if solution_particle[i] != solution_pbest[i]:
                        swap_operator = (i, solution_pbest.index(solution_particle[i]), self.alfa)

                        temp_velocity.append(swap_operator)

                        aux = solution_pbest[swap_operator[0]]
                        solution_pbest[swap_operator[0]] = solution_pbest[swap_operator[1]]
                        solution_pbest[swap_operator[1]] = aux

                for i in range(self.graph.amount_vertices-3):
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

def main(beta,alpha,it):
     
     print(customerno)
     graph = Graph(amount_vertices=sheet.nrows)
     i=0
     j=0
   
     for i in range(customerno - 1):
         for j in range(customerno-1):
             graph.addEdge(idno[i],idno[j],graph.calculatecost(idno[i],idno[j]))
     graph.showGraph()

     pso = PSO(graph, iterations=it, size_population=100, beta=beta, alfa=alpha)
     pso.run() 

     pso.showsParticles()
     pso.plot()
 
     print('global_best(final route): %s -> cost(minimum possible cost): %d\n' % (pso.getGBest().getPBest(), pso.getGBest().getCostPBest()))
     final_route=[]
     final_route=pso.getGBest().getPBest()
     
     cost=calculatefinal(final_route,customerno-1)
     
    
     print("AND THE FINAL COST FOR OUR SOLUTION IS")
     print(cost)
     
