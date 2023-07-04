import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def dmat(d):
    return np.matrix([[1,d,0,0],[0,1,0,0,],[0,0,1,d],[0,0,0,1]])
def R(Rx,Ry):
    return np.matrix([[1,0,0,0],[-2/Rx,1,0,0],[0,0,1,0],[0,0,-2/Ry,1]])
def T(theta):
    return np.matrix([[np.cos(theta),0,np.sin(theta),0],[0,np.cos(theta),0,np.sin(theta)],[-np.sin(theta),0,np.cos(theta),0],[0,-np.sin(theta),0,np.cos(theta)]])

d=200
N=182
tilt=0
dmir=200
Nmir=182
Mx=80
My=76
theta=tilt*np.pi/180
phix=np.pi*Mx/Nmir
phiy=np.pi*My/Nmir
dRx=1.0
dRy=1.0
Rx=dRx*(dmir/(1-np.cos(phix)))
Ry=dRy*(dmir/(1-np.cos(phiy)))
#print(Rx,Ry)

Z0=np.matrix([[0],[0.065],[0],[0.065]])
x1=[]
y1=[]
x2=[]
y2=[]

Zn=Z0
x1.append(Zn[0])
y1.append(-Zn[2])
i=1
for i in range(1,N+1):
    if i%2==0:
        C=np.dot(R(Rx,Ry),dmat(d))
        Zn=np.dot(C,Zn)
        x1.append(Zn[0])
        y1.append(-Zn[2])
    else:
        C=np.dot(np.dot(np.dot(T(-theta),R(Rx,Ry)),T(theta)),dmat(d))
        Zn=np.dot(C,Zn)
        x2.append(Zn[0])
        y2.append(-Zn[2])
    i=i+1

#print(Zn)

#i=1
#ims = []
#fig = plt.figure(figsize=(7,7))
#plt.title('front mirror')
##plt.title('back mirror')
#for i in range(1,N+1):
#    im = plt.scatter(x1[0:i],y1[0:i], marker='o', color='black', s=25)
#    #im = plt.scatter(x2[0:i],y2[0:i], marker='o', color='red', s=25)
#    ims.append([im])
#ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=100)
#plt.show()

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title("front mirror")
ax1.set_aspect('1.0')
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("back mirror")
ax2.set_aspect('1.0')
ax1.scatter(x1,y1, marker='o', color='black', s=25)
ax2.scatter(x2,y2, marker='o', color='red', s=25)
plt.show()
