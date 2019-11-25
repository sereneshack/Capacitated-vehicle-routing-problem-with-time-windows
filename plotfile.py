from matplotlib import pyplot as plt


def main():
 y = [40766.4,38098.4,32456.7,33456.7,40987.6,30456.78] 
 x = ['GA','PSO','ACO ELLITIST','ACO ACS','HYBRID GA','HYBRID ACO PSO'] 
 plt.plot(x, y) 
 plt.xlabel('x - axis') 
 plt.ylabel('y - axis') 
 plt.title('Cost for instance 1') 
 plt.show()
 
 y = [322.23,5.46,345.56,657.86,134.56] 
 x = ['GA','PSO','ACO','HYBRID GA','HYBRID ACO PSO'] 
 plt.plot(x, y) 
 plt.xlabel('x - axis') 
 plt.ylabel('y - axis') 
 plt.title('Computational time for instance 1') 
 plt.show() 

 y = [45366.4,40098.4,33456.7,33452.7,42435.6,33456.78] 
 x = ['GA','PSO','ACO ELLITIST','ACO ACS','HYBRID GA','HYBRID ACO PSO'] 
 plt.plot(x, y) 
 plt.xlabel('x - axis') 
 plt.ylabel('y - axis') 
 plt.title('Cost for instance 2') 
 plt.show()
 
 y = [350.23,5.90,423.56,634.86,137.56] 
 x = ['GA','PSO','ACO','HYBRID GA','HYBRID ACO PSO'] 
 plt.plot(x, y) 
 plt.xlabel('x - axis') 
 plt.ylabel('y - axis') 
 plt.title('Computational time for instance 2') 
 plt.show() 

 x = ['csize=50 steps=10','csize=100 steps=20','csize=150 steps=30','csize=200 steps=40','csize=250 steps=50']
 y=[37711.78,37213.80,37389.08,38338.3,38726.55]
 plt.plot(x, y) 
 plt.xlabel('x - axis') 
 plt.ylabel('y - axis') 
 plt.title('Parameter variation for hybrid ACO AND PSO') 
 plt.show() 

 y = [40766.4,38098.4,32456.7,33456.7,40987.6,30456.78] 
 x = ['GA','PSO','ACO ELLITIST','ACO ACS','HYBRID GA','HYBRID ACO PSO'] 
 plt.bar(x,y) 
 y = [322.23,5.46,345.56,345.56,657.86,134.56] 
 x = ['GA','PSO','ACO ELLITIST','ACO ACS','HYBRID GA','HYBRID ACO PSO'] 
 plt.bar(x,y)
 plt.title('Cost vs Computational time for instance 1')  
 plt.show()

 y = [45366.4,40098.4,33456.7,33452.7,42435.6,33456.78] 
 x = ['GA','PSO','ACO ELLITIST','ACO ACS','HYBRID GA','HYBRID ACO PSO'] 
 plt.bar(x,y)
 y = [350.23,5.90,423.56,423.56,634.86,137.56] 
 x = ['GA','PSO','ACO ELLITIST','ACO ACS','HYBRID GA','HYBRID ACO PSO'] 
 plt.bar(x,y)
 plt.title('Cost vs Computational time for instance 2')  
 plt.show()


 




