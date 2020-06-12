import numpy as np
from position import Position
import open3d as o3d
import utilities as uti

class HumanSkeleton:
    __slots__ = ['height','joints','__lines']
    def __init__(self,height=None):
        self.height = height
        self.joints = {
            'head' : Position(),            #0
            'neck' : Position(),            #1
            'left_shoulder' : Position(),   #2
            'right_shoulder' : Position(),  #3
            'left_elbow' : Position(),      #4
            'right_elbow' : Position(),     #5
            'left_wrist' : Position(),      #6
            'right_wrist' : Position(),     #7
            'left_hand' : Position(),       #8
            'right_hand' : Position(),      #9
            'weist' : Position(),           #10
            'left_knee' : Position(),       #11
            'right_knee' : Position(),      #12
            'left_ankle' : Position(),      #13
            'right_ankle' : Position(),     #14
            'left_foot' : Position(),       #15
            'right_foot' : Position(),      #16
        }

        self.__lines = [
            [0,1],
            [2,1],
            [3,1],
            [4,2],
            [5,3],
            [6,4],
            [7,5],
            [8,6],
            [9,7],
            [10,1],
            [11,10],
            [12,10],
            [13,11],
            [14,12],
            [15,13],
            [16,14],
        ]
    
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
    
    def createSkeleton(self,list_coords):
        ## save data
        index = 0
        for i in self.joints:
            self.joints[i].setCoordinate(list_coords[index])
            index += 1
        
        ## return open3d object
        line_set = o3d.geometry.LineSet(
            points=o3d.utility.Vector3dVector(list_coords),
            lines=o3d.utility.Vector2iVector(self.__lines),
        )
        return line_set
