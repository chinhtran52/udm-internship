import numpy as np
import math

def groupYAxis(front_points,delta):
    #sap xep theo chieu tang dan cua toa do y
    temp = sortColumn(front_points,1)
    #tao mang gop nhom
    group_count = math.ceil((temp[-1][1]-temp[0][1])/delta)
    group = []
    for i in range(group_count):
        group.append([])
    for i in range(len(temp)):
        num = int((temp[i][1]-temp[0][1])//delta)
        group[num].append(list(temp[i]))
    for i in range(group_count):
        group[i] = sortColumn(group[i],0)
    return group

def sortColumn(list_or_array,col_num):
    a = np.asarray(list_or_array)
    #sap xep theo chieu tang dan cua toa do y
    return a[a[:,col_num].argsort()]

#def getArea(list_or_array):
