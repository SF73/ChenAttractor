import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.animation as animation
import scipy.integrate as S
def deriv(x, t):
    dx=[0.]*len(x)
    dx[0]=a*(x[1]-x[0])
    dx[1]=(c-a)*x[0]-x[0]*x[2]+c*x[1]
    dx[2]=x[0]*x[1]-b*x[2]
    return dx
    
a=35;b=3;c=28
t=np.arange(0,500,1e-3)
# x0s = [[0,0],[1e-4,0]]
# res = [S.odeint(deriv,x,t) for x in x0s]
x0=[7,7,40]
res=S.odeint(deriv,x0,t)
x=res[:,0] #theta
y=res[:,1]
z=res[:,2]

fig = figure()
ax = fig.gca(projection='3d')
ln, = plt.plot([], [],[], 'b.', animated=True)
ln2, = plt.plot([],[],[], 'g.',animated=True)
# ax.set_xlabel(r'$\theta$',size=12)
# ax.set_ylabel(r'$\dot{\theta}$',size=12)
fig.tight_layout()

# timest=[]
# thetast=[]
# thetaPst = []
# for i in range(len(t)):
#     if abs(t[i]%(2*np.pi))<1e-6:
#         timest.append(t[i])
#         thetast.append(theta[i])
#         thetaPst.append(thetaP[i])

def init():
    ax.set_xlim(-20, 20)
    ax.set_ylim(-30,30)
    ax.set_zlim(10,45)
    return ln,

def update(i):
    ln.set_data(x[:i], y[:i],z[:i])
    #ln.set_data(res[0][:,0][max(0,i-10):i]%(2*np.pi), res[0][:,1][max(0,i-10):i])
    #ln2.set_data(res[1][:,0][max(0,i-10):i]%(2*np.pi), res[1][:,1][max(0,i-10):i])
    return ln,#ln2

ani = animation.FuncAnimation(fig, update, frames=500, interval=10,
                    init_func=init, blit=True)

#ani.save('test.mp4',bitrate=1024)
plt.show()