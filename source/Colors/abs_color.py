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
    if curvature_value<0.2:
        return switcher[1]
    elif curvature_value<0.7:
        return switcher[2]
    elif curvature_value<1.2:
        return switcher[3]
    elif curvature_value<1.7:
        return switcher[4]
    elif curvature_value<2.2:
        return switcher[5]
    elif curvature_value<3.2:
        return switcher[6]
    elif curvature_value<4.2:
        return switcher[7]
    elif curvature_value<5.2:
        return switcher[8]
    else:
        return switcher[9]