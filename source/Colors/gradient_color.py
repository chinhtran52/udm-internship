import numpy as np
from colour import Color


def getColor(value,range_color=32,highest=10,lowest=-10):
    if lowest<value<highest:
        temp = value
    elif value<=lowest:
        temp = lowest
    else:
        temp = highest
    red = Color("blue")
    colors = np.array(list(red.range_to(Color("red"),range_color)))
    ran = highest - lowest
    det = temp - lowest
    cur = int((det*(range_color-1))//ran)
    return np.around(np.array(colors[cur].rgb)*255)