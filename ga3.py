import numpy as np
import random as random
from geopy.distance import geodesic
import math
from matplotlib import pyplot as plt
import time

def findindex(obj,p2,popsize):
    
    for j in range(popsize):
      if(p2[j]==obj):
        return j

def crossover(p1,p2,popsize):

 start_pos=2
 end_pos=18
 
 
 xtra=np.zeros(popsize-17)

 list=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

 for p in sorted(list):

  obj1=p1[p]
  popsize=len(p2)
  i1=findindex(obj1,p2,popsize)
  p2=np.delete(p2,i1)
  xtra = np.append (xtra, obj1)
 


 no=17
 for i in range(no):
  p2=np.append(p2,0)


 child=p2
 child=child+xtra

 return child

def mutation(p1,popsize):
 
 start_pos=3
 ptemp=np.zeros(popsize)
 ptemp=p1
 xtra=np.zeros(popsize-8)
 list=[3,4,5,6,7,8,9,10]

 for p in sorted(list):
  obj1=p1[p]
  popsize=len(ptemp)
  i1=findindex(obj1,ptemp,popsize)
  ptemp=np.delete(ptemp,i1)

  xtra = np.append (xtra, obj1)

 no=8
 for i in range(no):
  ptemp=np.append(ptemp,0)


 ptemp=ptemp+xtra
 return ptemp

    
def selection(ga,popsize):
  number=50
  size=10
  array = np.zeros((10,popsize))
  a = np.random.randint(50, size =10)
  k=0
  for i in  range(size):
    index=a[k] 
    array[i]=ga[index]
    k=k+1  
  
  fitness=[]
  k=0
  bestwo = np.zeros((2,popsize))
  sum=0
  for i in range(size):
      array[k]=array[k].astype(int)
      f,cost=calculatecost(array[k],popsize)
      fitness.append(f)   
      sum=sum+fitness[k]
      k=k+1
  fixedpoint=random.uniform(0,sum)
  partialsum=0
  k=0
  count=0
  p=0
  for i in range(size):
     if(count==2):
       break
     partialsum=partialsum+fitness[k]
     k=k+1
     if(partialsum>fixedpoint):
         bestwo[p]=array[i]
         count=count+1
         p=p+1
  if(count==1):
     bestwo[1]=array[2]
  return bestwo 

def selectionformutation(ga,popsize):
  number=50
  size=10
  array = np.zeros((10,popsize))
  a = np.random.randint(50, size =10)
  k=0
  for i in  range(size):
    index=a[k] 
    array[i]=ga[index]
    k=k+1  
  
  fitness=[]
  k=0
  bestone = np.zeros((1,popsize))
  sum=0
  for i in range(size):
      f,cost=calculatecost(array[k],popsize)
      array[k]=array[k].astype(int)
      fitness.append(f)   
      sum=sum+fitness[k]
      k=k+1
  fixedpoint=random.uniform(0,sum)
  partialsum=0
  k=0
  count=0
  p=0
  for i in range(size):
     if(count==1):
       break
     partialsum=partialsum+fitness[k]
     k=k+1
     if(partialsum>fixedpoint):
         bestone[p]=array[i]
         count=count+1
         p=p+1
  if(count==0):
     bestone[1]=array[2]
  return bestone 

def selectchromosomes(ga,ganew50):
  number=50
  size=10
  array = np.zeros((10,popsize))
  a = np.random.randint(50, size =10)
  k=0
  for i in  range(size):
    index=a[k] 
    array[i]=ga[index]
    k=k+1  
  
  fitness=[]
  k=0
  bestfifty = np.zeros((1,popsize))
  sum=0
  for i in range(size):
      f,cost=calculatecost(array[k],popsize)
      array[k]=array[k].astype(int)
      fitness.append(f)   
      sum=sum+fitness[k]
      k=k+1
  fixedpoint=random.uniform(0,sum)
  partialsum=0
  k=0
  count=0
  p=0
  m=0
  for i in range(size):
     if(count==1):
       break
     partialsum=partialsum+fitness[k]
     k=k+1
     if(partialsum>fixedpoint):
         bestfifty[p]=array[i]
         count=count+1
         p=p+1
  if(count==0):
     bestfifty[m]=array[2]
     m=m+1
  return bestfifty 
  

def plot(lastbest, line_width=1, point_radius=math.sqrt(2.0), annotation_size=8, dpi=120, save=True, name=None):
        
        
        lastbes=[]
        
        x= np.zeros(customerno, dtype = int)
        k=0
        for i in lastbest:
          x[k]=latitude[i-1]
          k=k+1
        y= np.zeros(customerno, dtype = int)
        u=0
        for i in lastbest:
          y[u]=longitude[i-1]
          u=u+1
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

def assignvehicles(p1,capacity,maxvehicles,demand,readytime,duedate,servicetime):
 customerno=101
 route = np.zeros((maxvehicles+1,customerno))
 for i in range(maxvehicles):
     currentcapacity[i]=capacity
      
 curveh=1
 p1=p1.astype(int)
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

def fitnessfunction(elapsedtime,distancecost):
  timecost=np.sum(elapsedtime)
  a=np.random.dirichlet(np.ones(2),size=1)
  totalcost=distancecost+timecost
  return a[0][0]*timecost+a[0][1]*distancecost,totalcost


def calculatecost(p1,customerno):
   for i in range(maxvehicles):
     elapsedtime[i]=0
   route=assignvehicles(p1,capacity,maxvehicles,demand,readytime,duedate,servicetime)
   distancecost=calculatedistcost(route,customerno)
   f,totalcost=fitnessfunction(elapsedtime,distancecost)
   return f,totalcost
 
'''main function'''
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



def main(generations):
 print(customerno)

 flag=0        
 

 for t in range(generations):
  print("\n\ngeneration number==")
  print(t)
  popsize=customerno
  iters=50
  op=2
  b=[]
  b=idno
  
  if(flag==0):
   ga = np.zeros((50,popsize))
  else:
   ga=selectchromosomes(ga,ganew50)
  for p in range(iters):
    c = np.zeros((op,popsize))
    a = np.random.randint(50, size =popsize)
    for i in range(op):
      for j in range(popsize):
         if (i==0):
           a[j]=int(a[j])
         
           c[i][j]=a[j]
         else:
           b[j]=int(b[j])
           c[i][j]=b[j]
    c=c.astype(int)
    
    for i in range(popsize): 
     for j in range(0, popsize-i-1): 
  
              if(c[0][j]>c[0][j+1]):
               temp=c[0][j]
               c[0][j]=c[0][j+1]
               c[0][j+1]=temp
               temp=c[1][j]
               c[1][j]=c[1][j+1]
               c[1][j+1]=temp
   
    m=0
    for j in range(popsize):
        m = int(m)
        m=c[1][j]
        ga[p][j]=m
     
  
  print("initial 50 chromosomes generated\n")
  ga=ga.astype(int)
  print(ga)
  ganew50 = np.zeros((iters,popsize))
  ganew50=ganew50.astype(int)

  crossover_population=40
  for i in range(crossover_population):
   bestwo = np.zeros((2,popsize))
   bestwo=selection(ga,popsize)
   child=crossover(bestwo[0],bestwo[1],popsize)
   ganew50[i]=child
 
  list=[40,41,42,43,44,45,46,47,48,49]
  for i in sorted(list):
   bestwo = np.zeros((1,popsize))
   bestone=selectionformutation(ga,popsize)
   child=mutation(bestone[0],popsize)
   ganew50[i]=child
   
  print("\nNew 50 chromosomes matrix after mutation and crossover\n")
  print(ganew50)
  

  print("\n\ncalculating cost of all chromosomes\n")

  costof100chromo=np.zeros(100)
  no=100
  m=0
  fitnessof100chromo=np.zeros(100)
  ga=ga.astype(int)
  ganew50=ganew50.astype(int)
  print(ga)
  print(ganew50)
  for i in range(no):
   cost=0
   if(i>49):
    f,cost=calculatecost(ganew50[m],popsize)
    m=m+1
    costof100chromo[i]=cost
    fitnessof100chromo[i]=f

   else:
   
    f,cost=calculatecost(ga[i],popsize)
    costof100chromo[i]=cost
    fitnessof100chromo[i]=f

  print(costof100chromo)

  print("\nfitness of all chromosomes\n")
  

 
  print(fitnessof100chromo)
  bestelement=min(fitnessof100chromo)
  i1=findindex(bestelement,fitnessof100chromo,100)
  print("\nbest fitness is=>")
  print(bestelement)
  print("cost of best element is")
  print(costof100chromo[i1])
  if(t==generations-1):
    lastcost=costof100chromo[i1]
  print("best route is=>")
  lastbest=[]
  if(i1>49):
   i1=i1-50
   print(ganew50[i1])
   if(t==generations-1):
     lastbest=ganew50[i1]
  else: 
   print(ga[i1])
   if(t==generations-1):
     lastbest=ga[i1]


 lastbest=lastbest.astype(int)
 f,finalcost=calculatecost(lastbest,popsize)
 
 print("AND THE FINAL COST FOR OUR SOLUTION IS",finalcost)
 plot(lastbest)
 
 return lastbest








   
