import quadratic as qdr
import numpy as np
import plyfile as ply
from plyfile import PlyData, PlyElement
import math

def getPrincipalCurve(mean_data,gauss_data):
    k = []
    absolute = np.zeros(vertices)
    rms = np.zeros(vertices)
    for i in range(vertices):
        s = 2*curvature_data_mean[i]
        p = curvature_data_gauss[i]
        k.append(qdr.quadratic_revert_viete(s,p))
        absolute[i] = abs(k[i][0]) + abs(k[i][1])
        rms[i] = math.sqrt((k[i][0]*k[i][0]+k[i][1]*k[i][1])/2)
    return {
        'k_principal' : k,
        'rms' : rms,
        'abs' : absolute
    }