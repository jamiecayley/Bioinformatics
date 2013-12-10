import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pylab import show

#define rates
k1=0.05	#ER exit rate constant (in min -1)
k2=.1	#Golgi to SG rate constant (in min -1)

#define system of eqns as dy/dt = f(y,t)
def f(y,t):
	f0=-k1*y[0]
	f1=k1*y[0]-k2*y[1]
	f2=k2*y[1]
	return [f0,f1,f2]
	
#set initial conditions
y0 = [100,0,0]

#define time interval to integrate
t=np.linspace(0,60,1000)
	
#solve the DEs
soln = odeint(f, y0, t)
E = soln[:,0]
G = soln[:,1]
S = soln[:,2]

#plot results
plt.figure()
plt.plot(t, E, label='ER')
plt.plot(t, G, label='Golgi')
plt.plot(t, S, label='SG')
plt.xlabel('time (min)')
plt.ylabel('% of total pulse')
plt.title('modeling transport ER -> Golgi -> SG')
plt.legend(loc=0)
show()
