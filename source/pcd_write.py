import open3d as o3d

def writePCD(data,path): 
    f = open(path,'w')   
    f.write("""# .PCD v.7 - Point Cloud Data file format
VERSION .7
FIELDS x y z
SIZE 4 4 4
TYPE F F F
COUNT 1 1 1
WIDTH 213
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS """+str(len(data))+"""
DATA ascii
""")
    for i in range (len(data)):
        f.writelines(str(data[i][0])+' '+str(data[i][1])+' '+str(data[i][2])+'\n')

def filterBodyPoints(data):
    results = []
    for i in data:
        if 2.8>i[2]>1.7 and -1<i[1]<1 and -0.5<i[0]<0.5:
            results.append(i)
    return results