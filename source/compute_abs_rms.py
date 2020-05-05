import quadratic as qdr
import numpy as np
import plyfile as ply
from plyfile import PlyData, PlyElement
import math

def getPrincipalCurve(frames,gauss_dic_in,mean_dic_in,abs_dic_out,rms_dic_out):
    for i in range(1,frames+1):
        plydata_mean = PlyData.read(mean_dic_in+'jean_nm'+str(i)+'.ply')
        plydata_gauss = PlyData.read(gauss_dic_in+'jean_ng'+str(i)+'.ply')
        mean_data = np.asarray(plydata_mean['vertex'][:]['quality'])
        gauss_data = np.asarray(plydata_gauss['vertex'][:]['quality'])
        count = plydata_mean['vertex'].count
        for j in range(count):
            s = 2*mean_data[j]
            p = gauss_data[j]
            k = qdr.quadratic_revert_viete(s,p)
            plydata_mean['vertex'][j]['quality'] = abs(k[0]) + abs(k[1])
            plydata_gauss['vertex'][j]['quality'] = math.sqrt((k[0]*k[0]+k[1]*k[1])/2)
        plydata_mean.write(abs_dic_out+'jean_na'+str(i)+'.ply')
        plydata_gauss.write(rms_dic_out+'jean_nr'+str(i)+'.ply')