import numpy as np
import math

def distance(x1,y1,z1,x2,y2,z2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

def checkNeighbor(numy_array_1,numy_array_2,radius):
    temp = distance(numy_array_1[0],numy_array_1[1],numy_array_1[2],numy_array_2[0],numy_array_2[1],numy_array_2[2])
    if temp<=radius:
        return True
    else:
        return False