import numpy as np
import open3d as o3d
import copy
import math

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

def distance(x1,y1,z1,x2,y2,z2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

def checkNeighbor(numy_array_1,numy_array_2,radius):
    temp = distance(numy_array_1[0],numy_array_1[1],numy_array_1[2],numy_array_2[0],numy_array_2[1],numy_array_2[2])
    if temp<=radius:
        return True
    else:
        return False