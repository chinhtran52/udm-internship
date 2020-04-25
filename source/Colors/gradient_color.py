import numpy as np
from colour import Color

range_color = 32
red = Color("blue")
colors = np.array(list(red.range_to(Color("red"),range_color)))
def getColor(value,highest=2,lowest=-2):
    if lowest<value<highest:
        temp = value
    elif value<=lowest:
        temp = lowest
    else:
        temp = highest
    ran = highest - lowest
    det = temp - lowest
    cur = int((det*(range_color-1))//ran)
    return np.around(np.array(colors[cur].rgb)*255)