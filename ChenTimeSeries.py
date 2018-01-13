import scipy.integrate as S
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import numpy as np
def lorenz(x,t):
    dx=[0.]*len(x)
    dx[0]=a*(x[1]-x[0])
    dx[1]=(c-a)*x[0]-x[0]*x[2]+c*x[1]
    dx[2]=x[0]*x[1]-b*x[2]
    return dx
#a=9;b=5;c=12
a=35;b=3;c=28

#a=40;b=3*0+1;c=26 #periodic ?
xt=np.arange(0,10,1e-6)
x0=[7,7,40]
res=S.odeint(lorenz,x0,xt)
tx=res[:,0]
ty=res[:,1]
tz=res[:,2]

fig = figure()
ax1 = fig.add_subplot(3,1,1)
ax1.set_xlabel('t')
ax1.set_ylabel('X')

ax2 = fig.add_subplot(3,1,2)
ax2.set_xlabel('t')
ax2.set_ylabel('Y')

ax3 = fig.add_subplot(3,1,3)
ax3.set_xlabel('t')
ax3.set_ylabel('Z')

ax1.plot(xt[0:len(xt)-28000],tx[28000:len(xt)]/np.max(tx),color='tab:blue')
ax1.plot(xt,ty/np.max(ty),color='tab:orange')
ax3.plot(xt[0:len(xt)-28000],(tx/np.max(tx))[28000:len(xt)]-(ty/np.max(ty))[0:len(xt)-28000],color='tab:green')

show()