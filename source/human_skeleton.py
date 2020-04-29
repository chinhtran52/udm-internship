import numpy as np
from position import Position

class Skeleton:
    height = np.NaN
    joints = {
        'head' : Position(),
        'neck' : Position(),
        'middle_weist' : Position(),
        'left_weist' : Position(),
        'right_weist' : Position(),
        'left_shoulder' : Position(),
        'right_shoulder' : Position(),
        'left_elbow' : Position(),
        'right_elbow' : Position(),
        'left_wrist' : Position(),
        'right_wrist' : Position(),
        'left_knee' : Position(),
        'right_knee' : Position(),
        'left_ankle' : Position(),
        'right_ankle' : Position(),
    }
    
    def setPosition(self,joint,x,y,z):
        try:
            self.joints[joint] = Position(x=x,y=y,z=z)
        except:
            print('wrong format!')