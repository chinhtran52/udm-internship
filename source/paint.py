import numpy as np
from PIL import Image
from bresenham import bresenham
from colour import Color

def lineColor(a,b):
    line = np.asarray(list(bresenham(a[0],a[1],b[0],b[1])))
    colorst = a[2:5]/255
    colornd = b[2:5]/255
    temp = []
    start_color = Color(red=colorst[0],green=colorst[1],blue=colorst[2])
    end_color = Color(red=colornd[0],green=colornd[1],blue=colornd[2])
    colors = list(start_color.range_to(end_color,len(line)))
    for i in range(len(line)):
        color = np.array(colors[i].rgb)*255
        temp.append([line[i][0],line[i][1],color[0],color[1],color[2]])
    return np.array(temp,dtype=np.int64)

def triColor(line,point):
    result = []
    for i in line:
        temp = lineColor(i,point)
        if len(result)<=0:
            result = temp
        else:
            result = np.append(result,temp,axis=0)
    return result

def colorTriangle(a,b,c,frame):
    lineAB = lineColor(a,b)
    lineBC = lineColor(b,c)
    lineCA = lineColor(c,a)
    tri1 = triColor(lineAB,c)
    tri2 = triColor(lineBC,a)
    tri3 = triColor(lineCA,b)
    tri = np.concatenate((tri1,tri2,tri3),axis=0)
    for i in tri:
        frame[i[1]][i[0]] = i[2:5]

# h = 200
# w = 100
# frame = np.zeros((h,w,3),dtype=np.uint8)
# frame += 255

# a = np.array([0,0,255,0,0])
# b = np.array([0,99,0,255,0])
# c = np.array([50,50,0,0,255])
# colorTriangle(a,b,c,frame)

# img = Image.fromarray(frame,'RGB')
# img.show()



