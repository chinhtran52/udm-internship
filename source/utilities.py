import numpy as np
import open3d as o3d
import copy
import math
from plyfile import PlyData, PlyElement
from PIL import Image
from colour import Color

def createPointCloud(points_list):
    temp = o3d.geometry.PointCloud()
    temp.points = o3d.utility.Vector3dVector(np.asarray(points_list))
    return temp

def computeNormal(points,cam):
    ##search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)
    points.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.5, max_nn=9))
    points.orient_normals_towards_camera_location(camera_location=cam)

def mergeTwoClouds(fcloud,scloud):
    points = np.append(np.asarray(fcloud.points),np.asarray(scloud.points),axis=0)
    normals = np.append(np.asarray(fcloud.normals),np.asarray(scloud.normals),axis=0)
    result = createPointCloud(points)
    result.normals = o3d.utility.Vector3dVector(normals)
    return result

def removeBacksurface(mesh,cam):
    result = [[],[]]
    mesh.compute_triangle_normals()
    tri = np.asarray(mesh.triangles)
    tri_nor = np.asarray(mesh.triangle_normals)
    for i in range(len(tri_nor)):
        if tri_nor[i][2]<0:
            result[0].append(tri[i])
            result[1].append(tri_nor[i])
    mesh1 = copy.deepcopy(mesh)
    mesh1.triangles = o3d.utility.Vector3iVector(np.array(result[0]))
    mesh1.triangle_normals = o3d.utility.Vector3dVector(np.array(result[1]))
    return mesh1

def sortColumn(list_or_array,col_num):
    a = np.asarray(list_or_array)
    #sap xep theo chieu tang dan cua toa do y
    return a[a[:,col_num].argsort()]

def distance(numpy_point_1,numpy_point_2):
    x1 = numpy_point_1[0]
    y1 = numpy_point_1[1]
    z1 = numpy_point_1[2]
    x2 = numpy_point_2[0]
    y2 = numpy_point_2[1]
    z2 = numpy_point_2[2]
    return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

def checkNeighbor(numy_array_1,numy_array_2,radius):
    temp = distance(numy_array_1[0],numy_array_1[1],numy_array_1[2],numy_array_2[0],numy_array_2[1],numy_array_2[2])
    if temp<=radius:
        return True
    else:
        return False

def filterBack(directory=None):
    if directory:
        plydata = PlyData.read(directory)
        count = plydata['vertex'].count
        temp = np.zeros((count,5))
        temp[:,0] = plydata['vertex']['x']
        temp[:,1] = plydata['vertex']['y']
        temp[:,2] = plydata['vertex']['z']
        temp[:,3] = plydata['vertex']['nz']
        temp[:,4] = plydata['vertex']['quality']
        results = []
        for i in temp:
            if i[3] > 0:
                results.append([i[0],i[1],i[4]])
        results = np.asarray(results)
        return results[:,0:2],results[:,2]
    else:
        print('Cant find your files directory.')

def displayImage(points,height,width,background=np.array([255,255,255])):
    #init background
    frame = np.empty((height,width,3),dtype=np.int8)
    frame[:,:] = background
    #paint format x,y,r,g,b
    for i in points:
        frame[int(i[1])][int(i[0])] = i[2:5]
    #display
    img = Image.fromarray(frame,'RGB')
    img.show()

def multipleArray(cycle,values):
    if cycle <= 1:
        return values
    else:
        result = values.copy()
        for i in range(cycle -1):
            result = np.append(result,values)
        return result

def outlierRemoval(open3d_point_cloud,neighbors,ratio):
    #prepare input data
    ## downsample the point clouds with voxel = 0.02
    ## voxel_down_pcd = open3d_point_cloud.voxel_down_sample(voxel_size=0.02)
    cl, ind = open3d_point_cloud.remove_statistical_outlier(nb_neighbors=neighbors,std_ratio=ratio)
    return display_inlier_outlier(open3d_point_cloud, ind)

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_down_sample(ind)
    outlier_cloud = cloud.select_down_sample(ind, invert=True)

    return {
        'inlier' : inlier_cloud,
        'outlier' : outlier_cloud
    }