#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:41:34 2019

@author: cadecorontzos


This program draws flowers, which consist of a certain diamonds alligned at a point. The screen fills with
 flowers, and these flowers rotate. By changing the number of diamonds, the distance between the flowers,
 and the angualar displacement of each flower with respect to the previous, all sorts of cool and trippy 
 designs can be created. Those three aspects are controled by buttons in the second window.
"""



from pgl import GPolygon,GWindow,GCompound,GOval,GLabel
from math import tan,radians,cos,sin

GW_WIDTH=600
GW_HEIGHT=600
THETA=[20,30,45,60,90]         # 360%THETA==0: 10 <= THETA <= 90
MIDX=GW_WIDTH//2
MIDY=GW_HEIGHT//2
TIME_STEP=10
colors=["Red","Orange","Yellow","Green","Blue","Indigo","aquamarine","hotpink","indianred","limegreen","cyan"
        ,"gold","mediumseagreen", "mediumaquamarine","lime","sienna","skyblue","peachpuff","peru",
        "white","plum","orchid","palevioletred", "snow","mediumvioletred","mediumorchid","lavenderblush",
        "lightseagreen","navajowhite","mediumslateblue","grey","midnightblue","gainsboro","lightslategrey"]

def Swirl():
    gw = GWindow(GW_WIDTH,GW_HEIGHT)
    allFlowers=[]
    theta=0
    steps=0
    angleNumber=4
    diamondAngle=THETA[3]
    limChanger=0
    stepChanger=10
    angularOffset=(.5*diamondAngle)
    aOchanger=0
    
    

    def setUp():#sets up scene
        nonlocal allFlowers,theta,diamondAngle,angularOffset
        lim=GW_WIDTH*2
        while(lim>=1):
            flower=drawFlowerz(lim,theta,diamondAngle)
            gw.add(flower,MIDX,MIDY)
            theta+= angularOffset
            lim= changeLim(lim)
            allFlowers.append(flower)
            
    def changeDiamondAngle():#changes the number of diamonds, or the number of colors
        nonlocal diamondAngle,angleNumber,angularOffset
        angleNumber+=1
        
        if angleNumber>len(THETA)-1:
            angleNumber=0
        diamondAngle=THETA[angleNumber]
        angularOffset=(.5*diamondAngle)
        
    def click(e):
        buttonPressed=gw2.getElementAt(e.getX(),e.getY())
        if buttonPressed==changeAngleButton:
            changeDiamondAngle()
        if buttonPressed==changeSpaceOffsetButton:
            changeSpace()
        if buttonPressed==changeAngularOffsetButton:
            changeAngularOff()
            
    
    def changeAngularOff():#changes angular offset of each flower with respect to the previous
        nonlocal diamondAngle,angularOffset,aOchanger
        aOchanger+=1
        if aOchanger>2:
            aOchanger=0
        if aOchanger==0:
            angularOffset=(.5*diamondAngle)
        if aOchanger==1:
            angularOffset=(.75*diamondAngle)
        if aOchanger==2:
            angularOffset=(2*diamondAngle)
        
    def step():
        nonlocal allFlowers,theta,steps,diamondAngle,stepChanger,angularOffset
        for i in allFlowers:
            gw.remove(i)
        allFlowers.clear()
        lim=GW_WIDTH*2
        steps+=stepChanger
        theta=0+(steps)
        
        while(lim>=1):
            flower=drawFlowerz(lim,theta,diamondAngle)
            gw.add(flower,MIDX,MIDY)
            theta+= angularOffset
            lim= changeLim(lim)
            allFlowers.append(flower)
        
    def changeSpace(): 
        nonlocal limChanger
        limChanger+=1
    
    def changeLim(lim): #changes space offset between each flower
        nonlocal limChanger,stepChanger
        if limChanger>=4:
            limChanger=0
        if limChanger==0:
            stepChanger=10
            return ((.5* lim)/cos((radians(.5*diamondAngle))))
        if limChanger==1:
            stepChanger=30
            return lim-60
        if limChanger==2:
            stepChanger=20
            return lim-100
        if limChanger==3:
            stepChanger=40
            return lim-40
    
    setUp()
    gw2=GWindow(GW_WIDTH,100)
    gw.setInterval(step,TIME_STEP)
    
   
    gw2.addEventListener("click",click)
    
    space=gw2.getWidth()//4
    changeAngleButton=createButton("Change Number of Colors") #changes the number of diamonds
    changeSpaceOffsetButton=createButton("Change Space Offset")#changes the space between each flower
    changeAngularOffsetButton=createButton("Change Angular Offset")#changes offset of each flower with respect to the previous
    gw2.add(changeAngleButton,space,gw2.getHeight()//2)
    gw2.add(changeSpaceOffsetButton,space*2,gw2.getHeight()//2)
    gw2.add(changeAngularOffsetButton,space*3,gw2.getHeight()//2)
    
def drawFlowerz(size,angle,diamondAngle): #draws flower, with size being the height of one diamond and angle  being the rotation of the flower
    f=GCompound()
    numDiamonds=360//diamondAngle
    theta=angle
    for i in range(numDiamonds):
        f.add(drawDiamond(size,theta,colors[i],diamondAngle))
        theta+=diamondAngle
    return f
        
def createButton(s):# makes a button with the string s
    button=GCompound()
    buttonSize=75
    label=GLabel(s)
    label.setColor("white")
    label.setFont("8px 'Sans-Serif'")
    c=GOval(-(label.getWidth()+20)//2,-buttonSize//2,label.getWidth()+20,buttonSize)
    c.setFillColor("black")
    c.setFilled(True)
    button.add(c)
    button.add(label,-label.getWidth()//2,0)
    return button
    
def drawDiamond(height,theta,color,diamondAngle):  #draws diamond of given height and color, with its' right edge on line with angle theta
    l=((.5*height)*cos((radians(.5*diamondAngle))))
    diamond=GPolygon()
    t=theta+diamondAngle
    diamond.addVertex(0,0)
    diamond.addPolarEdge(l,t)
    t=t-diamondAngle
    diamond.addPolarEdge(l,t)
    t=t-(180-diamondAngle)
    diamond.addPolarEdge(l,t)
    diamond.setFillColor(color)
    diamond.setFilled(True)
    return diamond 
             
if __name__=='__main__':
    Swirl()