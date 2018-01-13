import scipy.integrate as S
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import numpy as np
def chen(x,t):
    dx=[0.]*len(x)
    dx[0]=a*(x[1]-x[0])
    dx[1]=(c-a)*x[0]-x[0]*x[2]+c*x[1]
    dx[2]=x[0]*x[1]-b*x[2]
    return dx
#a=9;b=5;c=12
a=35;b=3;c=28

#a=40;b=3*0+1;c=26 #periodic ?
xt=np.arange(0,200,1e-3)
#x0=[14.0,8.1,45.0]
x0=[7,7,40]
#x0=[np.sqrt(abs(b*(2*c-a))),np.sqrt(abs(b*(2*c-a))),2*c-a]
#print(xf)
res=S.odeint(chen,x0,xt)
tx=res[:,0]
ty=res[:,1]
tz=res[:,2]
xPz = []
xPx = []
xPy = []
zth = 40
xth = 0
yth = 0
xy = []
theta = 45./180*np.pi
for i in range(len(tx)-1):
    if (tz[i]-zth)*(tz[i+1]-zth)<0:
        xPz.append([tx[i],ty[i]])
    if (tx[i]-xth)*(tx[i+1]-xth)<0:
        xPx.append([ty[i],tz[i]])
    if (ty[i]-yth)*(ty[i+1]-yth)<0:
        xPy.append([tx[i],tz[i]])
    # if (tx[i]-ty[i])*(tx[i+1]-ty[i+1])<0:
    #     xy.append([tx[i],ty[i],tz[i]])
    if (tx[i]*np.sin(theta)-ty[i]*np.cos(theta))*(tx[i+1]*np.sin(theta)-ty[i+1]*np.cos(theta))<0:
        xy.append([tx[i],ty[i],tz[i]])
xPx = np.asarray(xPx)
xPy = np.asarray(xPy)
xPz = np.asarray(xPz)
xy = np.asarray(xy)
f=figure()
ax=f.gca(projection='3d')
ax.plot(tx,ty,tz,linewidth=1)

# section de poincare
# ax.plot(xPz[:,0],xPz[:,1],zth*np.ones((len(xPz[:,1]))),'.')
# ax.plot(xth*np.ones((len(xPx[:,1]))),xPx[:,0],xPx[:,1],'.')
# ax.plot(xPy[:,0],yth*np.ones((len(xPy[:,1]))),xPy[:,1],'.')
# ax.plot(xy[:,0],xy[:,1],xy[:,2],'.')

# point fixes
# ax.scatter(np.sqrt(abs(b*(2*c-a))),np.sqrt(abs(b*(2*c-a))),2*c-a,color='red')
# ax.scatter(-np.sqrt(abs(b*(2*c-a))),-np.sqrt(abs(b*(2*c-a))),2*c-a,color='red')
# ax.scatter(0,0,0,color='red')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig = figure()
ax1 = fig.add_subplot(2,2,1)
ax1.set_xlabel('Y')
ax1.set_ylabel('Z')

ax2 = fig.add_subplot(2,2,2)
ax2.set_xlabel('X')
ax2.set_ylabel('Z')

ax3 = fig.add_subplot(2,2,3)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')

ax4 = fig.add_subplot(2,2,4)
ax4.set_xlabel('u')
ax4.set_ylabel('Z')

ax1.text(.1,.9,r'x=%4.1f' % xth,transform=ax1.transAxes,fontsize=14)
ax2.text(.1,.9,r'y=%4.1f' % yth,transform=ax2.transAxes,fontsize=14)
ax3.text(.1,.9,r'z=%4.1f' % zth,transform=ax3.transAxes,fontsize=14)
ax4.text(.1,.9,r'$\theta=$%4.1f' % (theta*180./np.pi),transform=ax4.transAxes,fontsize=14)

ax1.plot(xPx[:,0],xPx[:,1],'.',color='tab:green')
ax2.plot(xPy[:,0],xPy[:,1],'.',color='red')
ax3.plot(xPz[:,0],xPz[:,1],'.',color='tab:orange')
ax4.plot(xy[:,0]*np.cos(theta)+xy[:,1]*np.sin(theta),xy[:,2],'.',color='tab:purple')




show()
