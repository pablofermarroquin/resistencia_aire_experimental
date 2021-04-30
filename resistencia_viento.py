import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error
import math

t= np.linspace(0, 1.36, 100, endpoint = True) 

expe= -0.0488*t**2 + 0.9469*t - 0.0192

alpha=0.0026
g=9.8
C=0.00001
step=1/240

n=1
Ay=-5.0676
Vy=-5.0676*t+6.8347
#As=[]
N=0
CC=0
while(n<=2):
    while(C<=10):
        a=g-C*Vy**n
        a_prom=np.mean(a)
        error=abs((a_prom-Ay)/Ay)*100
        #print(error)
        if(error<=0.1):
            #print("C: ",C,"n:",n)
            N=n
            CC=C
            break
        #As.append(a)
        C+=0.00001
    n+=0.01
 

y=[]
y.append(0)
t=[]
n=1
C=0.003
t.append(0)
dt=1/240
v=6.314
a=-9.8
while(y[len(y)-1]>=0):
    t=t[len(t)-1]+dt
    y.append(y[len(y)-1]+v*dt)

rmse = mean_squared_error(expe, y, squared=False)