switcher = {
    1: [255,0,0,255],
    2: [255,128,0,255],
    3: [255,255,0,255],
    4: [128,255,0,255],
    5: [0,255,0,255],
    6: [0,255,128,255],
    7: [0,255,255,255],
    8: [0,128,255,255],
    9: [0,0,255,255],
    'white': [255,255,255,255],
}

def getColor(curvature_value):
    if 0<=curvature_value:
        if curvature_value<20:
            return switcher[5]
        else:
            if curvature_value<60:
                return switcher[4]
            else:
                if curvature_value<90:
                    return switcher[3]
                else:
                    if curvature_value<100:
                        return switcher[2]
                    else:
                        return switcher[1]
    else:
        if curvature_value>-20:
            return switcher[5]
        else:
            if curvature_value>-60:
                return switcher[6]
            else:
                if curvature_value>-90:
                    return switcher[7]
                else:
                    if curvature_value>-100:
                        return switcher[8]
                    else:
                        return switcher[9]