import numpy as np
import plyfile as ply
from plyfile import PlyData, PlyElement

def getKneePoints(frames):
    results = []
    for i in range(1,frames+1):
        file_name='pose_'+str(i)+'.ply'
        plydata = PlyData.read('./Mesh/Gauss Curvature/normal/'+file_name)
        vertices = plydata['vertex'].count
        height = np.amax(plydata['vertex']['y'])-np.amin(plydata['vertex']['y'])
        curvature_data = np.asarray(plydata['vertex']['quality'])
        temp = []
        for i in range(vertices):
            if (0.2*height<plydata['vertex'][i]['y']<0.35*height) and curvature_data[i]>=2:
                temp.append(i)
        results.append(temp)
    return results

def getCenterKneePoint(list):
    len_list = []
    for i in range(len(list)):
        len_list.append(len(list[i]))
    index_min_len_list = np.argmin(np.amin(len_list))

    results = []
    for i in range(len(list[index_min_len_list])):
        temp = True
        for j in range(len(list)):
            if not (list[index_min_len_list][i] in list[j]):
                temp = False
        if temp:
            results.append(list[index_min_len_list][i])
    return results

def getCurveKnee(point,frames,folder):
    result = []
    for i in range(1,frames+1):
        file_name = 'pose_'+str(i)+'.ply'
        plydata = PlyData.read(folder+file_name)
        temp = plydata['vertex'][point]['quality']
        result.append(temp)
    return result

def getNeighborPoints(center_point,radius,curve_type=None,pose_number=None):
    cur = curve_type or 'ng'
    pose = pose_number or '1'
    plydata = PlyData.read('./Mesh/results/8 frames/'+cur+pose+'.ply')
    vertices = plydata['vertex'].count
    ymax = plydata['vertex'][center_point]['y']+radius
    ymin = plydata['vertex'][center_point]['y']-radius
    xmax = plydata['vertex'][center_point]['x']+radius
    xmin = plydata['vertex'][center_point]['x']-radius
    zmax = plydata['vertex'][center_point]['z']+radius
    zmin = plydata['vertex'][center_point]['z']-radius
    temp = []
    for i in range(vertices):
        if (ymin<plydata['vertex'][i]['y']<ymax) and (xmin<plydata['vertex'][i]['x']<xmax) and (zmin<plydata['vertex'][i]['z']<zmax):
            temp.append([i,plydata['vertex'][i]['quality']])
    return temp