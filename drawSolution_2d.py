#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pylab import *
"""
unit : ステップの大きさ
stopCriterion : 微分のnormがstopCriterion以下だと反復が止まる.停止条件
iteration : 反復回数
"""
myu=0
unit = 0.01
stopCriterion = 0.0000000001
iteration=2000

# ベクトルを拡大、縮小するメソッド
def stretchVector(list,n):
    list_ = [0]*len(list)
    for i in range(0,len(list)):
        list_[i] = list[i]*n
    return list_

def getDX2_1(x,y):
    return -x+x*x+y*y
def getDY2_1(x,y):
    return y+x*y

def getDX2_2(x,y):
    return 2*x-x*y-x*x
def getDY2_2(x,y):
    return y+x*y-y*y

def getDX3_1(x,y):
    return -y
def getDY3_1(x,y):
    return -x*x*x+y*y*y

def getDX3_3(x,y):
    return -myu*x*y+myu*y*y
def getDY3_3(x,y):
    return (1-myu)*x+x*y

def getPoints(x0,y0,fdx,fdy,direction):
    x=x0
    y=y0
    listx = [x]
    listy = [y]
    for i in range(iteration):
        dx = fdx(x,y)
        dy = fdy(x,y)
        norm = sqrt(dx*dx+dy*dy)
        if norm<stopCriterion:
            break
        dx = dx/norm
        dy = dy/norm
        x = x+dx*unit*direction
        y = y+dy*unit*direction
        listx.append(x)
        listy.append(y)
    return [listx,listy]

def drawGraph(listx0,listy0,fdx,fdy):
    for i in range(len(listx0)):
        result = getPoints(listx0[i],listy0[i],fdx,fdy,1)
        plot(result[0],result[1],"r-")
        result = getPoints(listx0[i],listy0[i],fdx,fdy,-1)
        plot(result[0],result[1],"b-")

def drawProblem2_1():
    xlim(-3,3)
    ylim(-3,3)
    listx0 = [-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3]
    listy0 = [0.1,0.6,1.1,1.6,2.1,2.6,-0.1,-0.6,-1.1,-1.6,-2.1,-2.6]
    drawGraph(listx0,listy0,getDX2_1,getDY2_1)

    listx0 = [0.1,0.35,0.6,0.85,1.1,1.35,1.6,1.85,2.1,2.35,2.6,2.85]
    listy0 =[0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
    drawGraph(listx0,listy0,getDX2_1,getDY2_1)

    listx0 = [0.1,0.35,0.6,0.85,1.1,1.35,1.6,1.85,2.1,2.35,2.6,2.85]
    listy0 =[-0.05,-0.05,-0.05,-0.05,-0.05,-0.05,-0.05,-0.05,-0.05,-0.05,-0.05,-0.05]
    drawGraph(listx0,listy0,getDX2_1,getDY2_1)

def drawProblem2_2():
    xlim(-3,3)
    ylim(-3,3)

    listx0 = [-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3]
    listy0 = [0.1,0.3,0.45,0.6,0.85,1.1,1.6,2.1,2.6,-0.1,-0.6,-1.1,-1.6,-2.1,-2.6]
    drawGraph(listx0,listy0,getDX2_2,getDY2_2)
    listx0 = [3,3,3,3,3,3,3,3,3,3,3,3]
    listy0 = [0.1,0.6,1.1,1.6,2.1,2.6,-0.1,-0.6,-1.1,-1.6,-2.1,-2.6]
    drawGraph(listx0,listy0,getDX2_2,getDY2_2)
    listy0 = [-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3]
    listx0 = [0.1,0.6,1.1,1.6,2.1,2.6,-0.1,-0.6,-1.1,-1.6,-2.1,-2.6]
    drawGraph(listx0,listy0,getDX2_2,getDY2_2)
    listy0 = [3,3,3,3,3,3,3]
    listx0 = [0.1,0.6,1.1,1.6,2.1,2.6,-0.1]
    drawGraph(listx0,listy0,getDX2_2,getDY2_2)
    listx0 = [0.2,0.15,0.1,0.05,0]
    listy0 = [0,0.05,0.1,0.15,0.2]
    drawGraph(listx0,listy0,getDX2_2,getDY2_2)

def drawProblem3_1():
    xlim(-1,1)
    ylim(-1,1)
    listx0 = [-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2]
    listy0 = [0,0.05,0.1,0.15,0.2,0.15,0.1,0.05,0]
    drawGraph(listx0,listy0,getDX3_1,getDY3_1)
    listx0 = [-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2]
    listy0 = [0,-0.05,-0.1,-0.15,-0.2,-0.15,-0.1,-0.05,0]
    drawGraph(listx0,listy0,getDX3_1,getDY3_1)
def drawProblem3_3(myu_):
    global myu
    myu = myu_
    xlim(-3,3)
    ylim(-3,3)

    # stretchUnit = 0.8
    # listx0 = [-3,-2,-1,0,1,2,3,-3,-2,-1,0,1,2,3,-3,-2,-1,0,1,2,3,-3,-2,-1,0,1,2,3]
    # listy0 = [0,1,2,3,2,1,0,0,1,2,3,2,1,0,0,-1,-2,-3,-2,-1,0,0,-1,-2,-3,-2,-1,0]
    # listx0_ = stretchVector(listx0,stretchUnit)
    # listy0_ = stretchVector(listy0,stretchUnit)
    # drawGraph(listx0_,listy0_,getDX3_3,getDY3_3)
    # for i in range(len(listx0)):
    #      listx0_[i] = listx0_[i]+myu-1
    #      listy0_[i] = listy0_[i]+myu-1
    # drawGraph(listx0_,listy0_,getDX3_3,getDY3_3)

    # stretchUnit = 0.8
    # listx0 = [-3,-2,-1,0,1,2,3,-3,-2,-1,0,1,2,3]
    # listy0 = [0,1,2,3,2,1,0,0,-1,-2,-3,-2,-1,0]
    # stretchVector(listx0,stretchUnit)
    # stretchVector(listy0,stretchUnit)
    # drawGraph(listx0,listy0,getDX3_3,getDY3_3)
    # stretchUnit=0.5
    # stretchVector(listx0,stretchUnit)
    # stretchVector(listy0,stretchUnit)
    # drawGraph(listx0,listy0,getDX3_3,getDY3_3)


    stretchUnit = 0.8
    listx0 = [-3,-3,-3,-3,-3,-3,-3,3,3,3,3,3,3,3]
    listy0 = [-3,-2,-1,0,1,2,3,-3,-2,-1,0,1,2,3]
    listx0_=stretchVector(listx0,stretchUnit)
    listy0_=stretchVector(listy0,stretchUnit)
    drawGraph(listx0_,listy0_,getDX3_3,getDY3_3)
    listx0 =[-3,-2,-1,0,1,2,3,-3,-2,-1,0,1,2,3]
    listy0 =[-3,-3,-3,-3,-3,-3,-3,3,3,3,3,3,3,3]
    listx0_=stretchVector(listx0,stretchUnit)
    listy0_=stretchVector(listy0,stretchUnit)
    drawGraph(listx0_,listy0_,getDX3_3,getDY3_3)

# drawProblem3_3は引数にmyuを持ちます

#drawProblem2_1()
#drawProblem2_2()
#drawProblem3_1()
drawProblem3_3(1.5)
show()
