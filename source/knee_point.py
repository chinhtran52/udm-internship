import numpy as np
import plyfile as ply
from plyfile import PlyData, PlyElement
import utilities as uti

def getKneePoints(frames):
    results = []
    for i in range(1,frames+1):
        plydata = PlyData.read('./Mesh/results/8 frames/ng'+str(i)+'.ply')
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

def getNeighborPoints(center_point,radius,curve_type,pose_number):
    vertices_data = PlyData.read('./Mesh/results/8 frames/'+curve_type+pose_number+'.ply')['vertex']
    count = vertices_data.count
    vertices = np.empty((count,5))
    vertices[:,0] = vertices_data['x']
    vertices[:,1] = vertices_data['y']
    vertices[:,2] = vertices_data['z']
    vertices[:,3] = vertices_data['quality']
    vertices[:,4] = vertices_data['nz']
    try:
        ctr = vertices[center_point]
    except:
        print("center point's outside the data")
        return False
    temp = []
    index = []
    for i in range(count):
        if uti.distance(vertices[i][:3],ctr) <= radius and vertices[i][4] > 0:
            temp.append(vertices[i])
            index.append(i)
    return np.asarray(temp),index

def getListPoints(list_index,curve_type=None,pose_number=None):
    cur = curve_type or 'ng'
    pose = pose_number or '1'
    vertices_data = PlyData.read('./Mesh/results/8 frames/'+cur+pose+'.ply')['vertex']
    count = vertices_data.count
    vertices = np.empty((count,5))
    vertices[:,0] = vertices_data['x']
    vertices[:,1] = vertices_data['y']
    vertices[:,2] = vertices_data['z']
    vertices[:,3] = vertices_data['quality']
    vertices[:,4] = vertices_data['nz']
    temp = []
    for i in list_index:
        temp.append(vertices[i])
    return np.asarray(temp)