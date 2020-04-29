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