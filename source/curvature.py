import numpy as np
from plyfile import PlyData

curtypes = {
    'sim' : {
        'gauss' : 1,
        'mean' : 1.5,
        'rms' : 2,
        'abs' : 2
    },
    'real' : {
        'gauss' : 50,
        'mean' : 10,
        'rms' : 14,
        'abs' : 15,
    }
}

def computeKneeAreaCurvature(data,data_type,curve_type,side=None):
    try:
        high_cure_limit = curtypes[data_type][curve_type]
        if len(data[0]) >= 4:
            min_h = np.amin(data[:,1])
            max_h = np.amax(data[:,1])
            h = max_h - min_h
            under = min_h + h*0.3
            above = min_h + h*0.35
            pknees = []
            avg_x = np.average(data[:,0])
            for i in range(len(data)):
                if under < data[i][1] < above and data[i][3] > high_cure_limit:
                    pknees.append(data[i])
            pknees = np.array(pknees)

            if side == 'left':
                pknees = pknees[np.where(pknees[:,0] > avg_x)]
            if side == 'right':
                pknees = pknees[np.where(pknees[:,0] < avg_x)]

            return pknees
        else:
            print('wrong data format, please set format (x,y,z,curvature value) as numpy array!')
    except:
        print('wrong data or curvature type! --- datatype = [real/sim] --- curve type = [gauss/mean/rms/abs]')