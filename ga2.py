import numpy as np
import random as random
from geopy.distance import geodesic
import math
from matplotlib import pyplot as plt


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


def calculatecost(p1,popsize):
 totalcost=0
 #print(p1)
 for i in range(popsize-2):
        c=p1[i]
        d=p1[i+1]
        c=c-12341
        d=d-12341
        c = int(c) 
        d = int(d) 
        #print(c)
        #print(d)
        loc1=(latitude[c],longitude[c])
        loc2=(latitude[d],longitude[d])
        b=(geodesic(loc1,loc2).km)

        totalcost=totalcost+b 

 
 
 return totalcost

def calculatefitness(x):
 return 1/x



def selectchromosomes(ga,ganew50):
 tempga = np.zeros((50,popsize))
 no=50

 for i in range(no):
  if(i>24):
   gatemp[i]=ganew50[i]
  else:
   gatemp[i]=ga[i]
 return tempga

def calculatefinal(lastbest,popsize):
 
 j=0
 penaltycost=0
 for i in range(int(vehicleno)):
   #cap=int(capacity)
   
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
      cost=calculatecost(array[k],popsize)
      obj=calculatefitness(cost)
      fitness.append(obj)   
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
      cost=calculatecost(array[k],popsize)
      obj=calculatefitness(cost)
      fitness.append(obj)   
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


def plot(lastbest, line_width=1, point_radius=math.sqrt(2.0), annotation_size=8, dpi=120, save=True, name=None):
        
        
        lastbes=[]
        for i in range(customerno-1):
            obj=int(lastbest[i])
            
            lastbes.append(obj-12341)
        
        x = [latitude[i] for i in sorted(lastbes)]
        x.append(x[0])
        y = [longitude[i] for i in sorted(lastbes)]
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
 
'''main function'''
import numpy as np
import xlrd
loc=("/home/sakshi/minorpro2/instance1.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
customerno=sheet.nrows-1
print(customerno)

idno=[]

for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,0)
    idno.append (obj1)
latitude=[]
longitude=[]
amtordered=[]
penalty=[]
time=[]
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,1)
    latitude.append (obj1)
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,2)
    longitude.append (obj1)
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,3)
    amtordered.append (obj1)
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,4)
    time.append (obj1)
for i in range(customerno+1):
  if(i!=0):
    obj1=sheet.cell_value(i,6)
    penalty.append (obj1)

vehicleno=sheet.cell_value(1,5)
capacity=[]

l=1
vehicleno=int(vehicleno)
for i in range(vehicleno):
    obj1=sheet.cell_value(l,7)
    capacity.append (obj1)
    l=l+1



def main(generations):

 flag=0        
 #generations=10

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
           c[i][j]=a[j]
         else:
           c[i][j]=b[j]

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
  print(ga)
  ganew50 = np.zeros((iters,popsize))

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
 
 
  for i in range(no):
   cost=0
   if(i>49):
    cost=calculatecost(ganew50[m],popsize)
    m=m+1
    costof100chromo[i]=cost

   else:
   
    cost=calculatecost(ga[i],popsize)
    costof100chromo[i]=cost

  print(costof100chromo)

  print("\nfitness of all chromosomes\n")
  fitnessof100chromo=np.zeros(100)

  for i in range(no):
   fitnessof100chromo[i]=calculatefitness(costof100chromo[i])


 
  print(fitnessof100chromo)
  bestelement=max(fitnessof100chromo)
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


 print(lastbest)
 finalcost=calculatefinal(lastbest,customerno)
 ffinalcost=finalcost+lastcost
 print("AND THE FINAL COST FOR OUR SOLUTION IS",ffinalcost)
 plot(lastbest)


   












   
