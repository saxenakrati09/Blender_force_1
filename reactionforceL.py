import bge, time
from mathutils import Vector
import os
import csv

controller = bge.logic.getCurrentController()
#controller.activate("right_servo")
obj = controller.owner

t = time.time()
v = Vector(obj.worldLinearVelocity)
m = obj.mass

def main():
    global t, v, m
 
    csvfile1 = "D:\Cloth simulations blender\cloth sphere sim\simulation4\\leftreactionforce.csv"
    obj.applyMovement([0,0,-0.0025], True)
    #compute change in time
    dt = time.time() - t
    t += dt

    #calculate change in velocity
    dv = Vector(obj.worldLinearVelocity) - v
    v += dv

    #force is change in momentum, which is velocity times mass, divided by time
    f = m * dv / dt
    #f = obj.getReactionForce()
    #f = obj.applyForce([0,0,-50],True)
    #obj.applyMovement([0,0,-2.5], True)
    
    with open(csvfile1, "a") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows([f])   
    print(f)
    
    #!!!!!!!!!!!!!!!!
    #CAUTION
    #PLEASE DELETE THE FILE ALREADY PRESENT IN THE FOLDER
    #OTHERWISE IT APPENDS
    #!!!!!!!!!!!!!!!!!!!!!!!!
     