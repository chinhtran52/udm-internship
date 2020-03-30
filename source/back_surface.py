import numpy as np
import math
import points_distance as ptd

def groupYAxis(front_points,delta,radius):
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
        getArea(group[i],radius)
    return group

def sortColumn(list_or_array,col_num):
    a = np.asarray(list_or_array)
    #sap xep theo chieu tang dan cua toa do y
    return a[a[:,col_num].argsort()]

def getArea(list_or_array,radius):
    result = []
    rule = True
    count = len(list_or_array)
    for i in range(count):
        if rule:
            result.append([])
            result[-1].append(list_or_array[i])
            if count != (i+1):
                if ptd.checkNeighbor(list_or_array[i],list_or_array[i+1],radius):
                    rule = False
        else:
            result[-1].append(list_or_array[i])
            if count != (i+1):
                if not ptd.checkNeighbor(list_or_array[i],list_or_array[i+1],radius):
                    rule = True
    print('The array are divided into '+str(len(result))+' area(s)')
    return np.asarray(result)

def reverseCurve(points):
    temp = points.copy()
    center_x = (temp[0][0]+temp[-1][0])/2
    center_z = (temp[0][2]+temp[-1][2])/2
    print(center_x,center_z)
    for i in temp:
        i[0] = 2*center_x - i[0]
        i[2] = 2*center_z - i[2]
    return np.asarray(temp)

test = [[-2,1,3],
        [-1,0,1],
        [1,6,1],
        [2,5,2]]

print(reverseCurve(test))

