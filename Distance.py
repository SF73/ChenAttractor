import numpy as np
from pylab import *
import scipy.integrate as S
import matplotlib.pyplot as plt
def deriv(x, t):
    """
    Derivees temporelles du systeme en fonction du temps t.
    """
    dx=[0.0]*len(x)
    dx[0]=x[1]
    dx[1]=-b*x[1]-np.sin(x[0])+F*np.cos(t)
    return dx
    
b=0.2
F=2

t=np.arange(0,2*np.pi*10000,2*np.pi/100)
x0s = [[0,0],[1e-10,0]]
res = [S.odeint(deriv,x,t) for x in x0s]
x1=res[0][:,0]%(2*np.pi) #theta
x2=res[1][:,0]%(2*np.pi)

y1=res[0][:,1] #thetaPoint
y2=res[1][:,1]

f, ax = plt.subplots()
ax.semilogx(t,np.sqrt((x2-x1)**2+(y2-y1)**2))
ax.set_xlabel('t',size=12)
ax.set_ylabel('distance',size=12)

# timest=[]
# thetast=[]
# thetaPst = []
# for i in range(len(t)):
#     if abs(t[i]%(2*np.pi))<1e-6:
#         timest.append(t[i])
#         thetast.append(theta[i])
#         thetaPst.append(thetaP[i])
# f2, ax2 = plt.subplots(figsize=(15, 10))
# ax2.scatter(thetast,thetaPst,s=2)
# ax2.set_xlabel('theta',size=12)
# ax2.set_ylabel(r'$\dot{\theta}$',size=12)
show()