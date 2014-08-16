#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
"""
14M37173 曽根毅
プログラムに関する問い合わせは
henohenotsuyoshi@gmail.com
までよろしくお願いします.

このファイルでは問4の解曲線を描く

unit : ステップの大きさ
stopCriterion : 微分のnormがstopCriterion以下だと反復が止まる.停止条件
iteration : 反復回数
colors : 線の色の種類
"""

unit = 0.01
stopCriterion = 0.0000000001
iteration = 2000
colors = ["b","g","r","c","m","y","k"]

def stretchVector(list,n):
    list_ = [0]*len(list)
    for i in range(0,len(list)):
        list_[i] = list[i]*n
    return list_

def getDX(x,y,z):
    return -y+x*y-pow(z,4)
def getDY(x,y,z):
    return x+y*z+x*y*z
def getDZ(x,y,z):
    return -z-x*x-y*y+z*z+math.sin(pow(x,3))
def getPoints(x0,y0,z0,fdx,fdy,fdz,direction):
    x = x0
    y=y0
    z=z0
    listx = np.array([x])
    listy = np.array([y])
    listz = np.array([z])
    for i in range(iteration):
        dx = fdx(x,y,z)
        dy = fdy(x,y,z)
        dz = fdz(x,y,z)
        norm = math.sqrt(dx*dx+dy*dy+dz*dz)
        if norm<stopCriterion:
            break
        dx = dx/norm
        dy = dy/norm
        dz = dz/norm
        x = x+dx*unit*direction
        y = y+dy*unit*direction
        z = z+dz*unit*direction
        listx = np.append(listx,x)
        listy = np.append(listy,y)
        listz = np.append(listz,z)
    return [listx,listy,listz]

def drawGarph(listx0,listy0,listz0,fdx,fdy,fdz):
    for j in range(len(listx0)):
        result = getPoints(listx0[j],listy0[j],listz0[j],fdx,fdy,fdz,1)
        ax.plot(result[0],result[1],zs=result[2],c=colors[j%len(colors)])
        result = getPoints(listx0[j],listy0[j],listz0[j],fdx,fdy,fdz,-1)
        ax.plot(result[0],result[1],zs=result[2],c=colors[j%len(colors)])

fig = plt.figure()
ax = fig.gca(projection='3d')

# ax.set_xlim3d(-0.02, 0.02)
# ax.set_ylim3d(-0.02, 0.02)
# ax.set_zlim3d(-0.02, 0.02)
ax.set_xlim3d(-0.2, 0.2)
ax.set_ylim3d(-0.2, 0.2)
ax.set_zlim3d(-0.2, 0.2)
# ax.set_xlim3d(-2, 2)
# ax.set_ylim3d(-2, 2)
# ax.set_zlim3d(-2, 2)

unitStretch = 0.01

listx0=[-2,-1,0,1,2,1,0,-1]
listy0=[0,1,2,1,0,-1,-2,-1]
listz0=[0,0,0,0,0,0,0,0]

listx0_=stretchVector(listx0,unitStretch)
listy0_=stretchVector(listy0,unitStretch)
listz0_=stretchVector(listz0,unitStretch)
drawGarph(listx0_,listy0_,listz0_,getDX,getDY,getDZ)
listz0=[2,2,2,2,2,2,2,2]
listz0_=stretchVector(listz0,unitStretch)
drawGarph(listx0_,listy0_,listz0_,getDX,getDY,getDZ)
listz0=[-2,-2,-2,-2,-2,-2,-2,-2]
listz0_=stretchVector(listz0,unitStretch)
drawGarph(listx0_,listy0_,listz0_,getDX,getDY,getDZ)

plt.show()