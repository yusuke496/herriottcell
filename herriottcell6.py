import sys
import matplotlib
import matplotlib.animation as animation
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import re
from statistics import mean
def dmat(d):
    return np.matrix([[1,d,0,0],[0,1,0,0,],[0,0,1,d],[0,0,0,1]])
def R(Rx,Ry):
    return np.matrix([[1,0,0,0],[-2/Rx,1,0,0],[0,0,1,0],[0,0,-2/Ry,1]])
def T(theta):
    return np.matrix([[np.cos(theta),0,np.sin(theta),0],[0,np.cos(theta),0,np.sin(theta)],[-np.sin(theta),0,np.cos(theta),0],[0,-np.sin(theta),0,np.cos(theta)]])

d=200
dmir=200
N=182
Mx=80
My=76
tilt=0
theta=tilt*np.pi/180
Z0=np.matrix([[0],[0.06],[0],[0.06]])
phix=np.pi*Mx/N
phiy=np.pi*My/N
dRx=1
dRy=1
Rx=dRx*(dmir/(1-np.cos(phix)))
Ry=dRy*(dmir/(1-np.cos(phiy)))
#print(Rx,Ry)
x1=[]
y1=[]
x2=[]
y2=[]
#print(dmat(d))
#print(R(Rx,Ry))
#print(T(theta))
#C=R(Rx,Ry)@dmat(d)@T(-theta)@R(Rx,Ry)@T(theta)@dmat(d)
#C=T(-theta)@R(Rx,Ry)@T(theta)@dmat(d)@T(-theta)@R(Rx,Ry)@T(theta)@dmat(d)
#print(C)
#print(C@C@C@C@C)
Zn=Z0
x1.append(Zn[0])
y1.append(Zn[2])
i=1
for i in range(1,N+1):
    if i%2==0:
        C=np.dot(R(Rx,Ry),dmat(d))
        Zn=np.dot(C,Zn)
        x1.append(Zn[0])
        y1.append(Zn[2])
    else:
        C=np.dot(T(-theta),R(Rx,Ry))
        C=np.dot(C,T(theta))
        C=np.dot(C,dmat(d))
        Zn=np.dot(C,Zn)
        x2.append(Zn[0])
        y2.append(Zn[2])
        #print(Zn[0])
    i=i+1
print(Zn)
print(C)

#i=1
#ims = []
#fig=plt.figure()
#for i in range(1,N+1):
#    im = plt.scatter(x1[0:i],y1[0:i], marker='o', color='black', s=15)
#    ims.append([im])
#    plt.title('front mirror')
#ani = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=1000)
#plt.show()

fig=plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title("front mirror")
ax1.set_aspect('1.0')
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("back mirror")
ax2.set_aspect('1.0')
ax1.scatter(x1,y1, marker='o', color='black', s=15)
ax2.scatter(x2,y2, marker='o', color='red', s=15)
plt.show()

#Zn=C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@C@Z0
