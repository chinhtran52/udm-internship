import utilities as uti
import numpy as np
from plyfile import PlyData,PlyElement
from PIL import Image
from scipy import interpolate

height = 200
width = 100

#read data
dic = './Mesh/results/normal/gauss_pose_1.ply'
points,curvatures = uti.filterBack(directory=dic)


center = [np.average(points[:,0]),np.average(points[:,1])]
points[:,0] = (points[:,0] - center[0])*10 + width/2
points[:,1] = (points[:,1] - center[1])*10 + height/2 + 20
points[:,0] = np.around(width - points[:,0])
points[:,1] = np.around(height - points[:,1])

f = interpolate.NearestNDInterpolator(points[:,:2],curvatures)
print(f)


# #paint raw point (option)
# color = np.zeros((len(points),3))
# points = np.append(points,color,axis=1)
# uti.displayImage(points,height,width)