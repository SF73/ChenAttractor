import scipy.integrate as S
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

def lorenz(x,t):
    dx=[0.]*len(x)
    dx[0]=a*(x[1]-x[0])
    dx[1]=(c-a)*x[0]-x[0]*x[2]+c*x[1]
    dx[2]=x[0]*x[1]-b*x[2]
    return dx

a=35;b=3;c=28
xt=np.arange(0,50,1e-3)

f=figure()
ax=f.gca(projection='3d')
sigma=10;beta=8.0/3;rho=28
x0=[7,7,40]
res=S.odeint(lorenz,x0,xt)
tx=res[:,0]
ty=res[:,1]
tz=res[:,2]
ax.plot(tx,ty,tz)
ax.scatter(tx[0],ty[0],tz[0])
ax.scatter(tx[-1],ty[-1],tz[-1],'*',color='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# FFT
f2=figure()
ax2=f2.add_subplot(111)
#tx=tx-mean(tx)
#ty=ty-mean(ty)
#tz=tz-mean(tz)
tfx=abs(rfft(tx))
tfy=abs(rfft(ty))
tfz=abs(rfft(tz))
tfx[0]=0
tfy[0]=0
tfz[0]=0
xtf=arange(len(tfx))
print (tfx[-30:-1])
#ax2.set_xlim(-100,len(xtf)+1)
ax2.loglog(xtf,tfx) #,'o',ms=5)
ax2.loglog(xtf,tfy) #,'o',ms=5)
ax2.loglog(xtf,tfz) #,'o',ms=5)
legend(['$fft_x$','$fft_y$','$fft_z$'])
# ax2.semilogy(xtf,tfx) #,'o',ms=5)
# ax2.semilogy(xtf,tfy) #,'o',ms=5)
# ax2.semilogy(xtf,tfz) #,'o',ms=5)
show()
