import numpy as np
from pylab import *
import scipy.integrate as S
import matplotlib.pyplot as plt
def deriv(x, t):
    dx=[0.]*len(x)
    dx[0]=a*(x[1]-x[0])
    dx[1]=(c-a)*x[0]-x[0]*x[2]+c*x[1]
    dx[2]=x[0]*x[1]-b*x[2]
    return dx
a=35;b=3;c=28
t=np.arange(0,500,1e-2)
x0s = [[7,7,40],[7+1e-7,7,40]]
res = [S.odeint(deriv,x,t) for x in x0s]
x1=res[0][:,0]
x2=res[1][:,0]

y1=res[0][:,1]
y2=res[1][:,1]

z1=res[0][:,2]
z2=res[1][:,2]

f, ax = plt.subplots()
ax.semilogx(t,np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
ax.set_xlabel('t',size=12)
ax.set_ylabel('distance',size=12)
ax.text(.1,.9,'$\|\|\Delta x(0)\|\|=10^{-7}$',ha='center', va='center',transform=ax.transAxes,fontsize=14)

show()