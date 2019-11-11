from matplotlib import pyplot as plt

def main():
 
 #Instance1(36 ccustomers 6 vehicles)
 # x-axis values 
 x = ['ga','pso','abcacs','abcellitist','abcmaxmin'] 

 # Y-axis values 
 y = [128948.121,129616.959982,145672.85,146783.67,145727.19] 

 
 plt.bar(x,y) 
 plt.show() 
 #Instance2(45 customers 10 vehicles)
 # x-axis values 
 x = ['ga','pso','abcacs','abcellitist','abcmaxmin'] 

 # Y-axis values 
 y = [259935.5125,243317.959982,237893.43,237700.17,237657.2] 

 
 plt.bar(x,y) 
 plt.show() 

 #Instance3(64 customers 16 vehicles)
 # x-axis values 
 x = ['ga','pso','abcacs','abcellitist','abcmaxmin'] 

 # Y-axis values 
 y = [391047.3495,336766.95,407216.92,407211.57,407194.06] 

 
 plt.bar(x,y) 
 plt.show() 


 #running ga for instance 1 with different generations

 x = ['genno=10','genno=20','genno=30','genno=40','genno=50'] 


 # Y-axis values 
 y = [137346.99,127929.95,123116.92,133007.57,132113.06] 
 plt.bar(x,y) 
 plt.show() 

 #running pso for instance 1 with different generations
 x = ['a=0.90 b=0.82','a=0.83 b=0.75','a=0.76 b=0.68','a=0.69 b=0.61','a=0.62 b=0.54']

 y=[122407.00,106199.83,119686.06,117566.21,123143.07]
 plt.bar(x,y) 
 plt.show() 
 #running abc for instance 1 with different generations for acs mode
 x = ['csize=60 steps=6','csize=70 steps=7','csize=80 steps=8','csize=90 steps=9','csize=100 steps=10']

 y=[201588.92,201775.21,201478.66,201538.62,201607.14]
 plt.bar(x,y) 
 plt.show() 


