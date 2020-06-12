import numpy as np

class Position:
    x = np.nan
    y = np.nan
    z = np.nan

    def __init__(self,x='number',y='number',z='number'):
        if isinstance(x,int):
            self.x = x
        if isinstance(x,int):
            self.y = y
        if isinstance(x,int):
            self.z = z
    
    def getCoordinate(self):
        return np.array([self.x,self.y,self.z])
    
    def setCoordinate(self,coords):
        try:
            self.x = coords[0]
            self.y = coords[1]
            self.z = coords[2]
        except:
            print("Can't set joint position!")