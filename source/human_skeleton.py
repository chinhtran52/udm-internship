import numpy as np
from position import Position
import open3d as o3d
import utilities as uti

class HumanSkeleton:
    __slots__ = ['height','joints','__lines']
    def __init__(self):
        self.height = np.NaN
        self.joints = {
            'head' : Position(),
            'neck' : Position(),
            'left_shoulder' : Position(),
            'right_shoulder' : Position(),
            'left_elbow' : Position(),
            'right_elbow' : Position(),
            'left_wrist' : Position(),
            'right_wrist' : Position(),
            'middle_weist' : Position(),
            'left_weist' : Position(),
            'right_weist' : Position(),
            'left_knee' : Position(),
            'right_knee' : Position(),
            'left_ankle' : Position(),
            'right_ankle' : Position(),
        }
        self.__lines = np.array([[0,1],
                                [2,1],
                                [3,1],
                                [3,2],
                                [5,3],
                                [6,4],
                                [7,5],
                                [8,1],
                                [9,8],
                                [10,8],
                                [11,9],
                                [12,10],
                                [13,11],
                                [14,12]])

    def setPosition(self,joint,x,y,z):
        try:
            self.joints[joint] = Position(x=x,y=y,z=z)
        except:
            print('wrong format!')
    
    def display(self):
        temp = []
        for i in self.joints:
            coordinate = self.joints[i].getCoordinate()
            if not np.isnan(coordinate).any():
                temp.append(coordinate)
        if len(temp) > 1:
            pcl = uti.createPointCloud(temp)
            pcl.paint_uniform_color(np.array([0,0,1]))
            o3d.visualization.draw_geometries([pcl])
            print(temp,pcl)
        else:
            print('Empty skeleton')
    
    def getLines(self):
        print(self.__lines)
    
a = HumanSkeleton()
a.__lines = 0