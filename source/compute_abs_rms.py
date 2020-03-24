import quadratic as qdr
import numpy as np
import plyfile as ply
from plyfile import PlyData, PlyElement
import math

def getPrincipalCurve(frames,gauss_dic_in,mean_dic_in,abs_dic_out,rms_dic_out):
    for i in range(1,frames+1):
        file_name = 'pose_'+str(i)+'.ply'
        plydata_mean = PlyData.read(mean_dic_in+file_name)
        plydata_gauss = PlyData.read(gauss_dic_in+file_name)
        mean_data = np.asarray(plydata_mean['vertex'][:]['quality'])
        gauss_data = np.asarray(plydata_gauss['vertex'][:]['quality'])
        count = plydata_mean['vertex'].count
        for i in range(count):
            s = 2*mean_data[i]
            p = gauss_data[i]
            k = qdr.quadratic_revert_viete(s,p)
            plydata_mean['vertex'][i]['quality'] = abs(k[0]) + abs(k[1])
            plydata_gauss['vertex'][i]['quality'] = math.sqrt((k[0]*k[0]+k[1]*k[1])/2)
        plydata_mean.write(abs_dic_out+file_name)
        plydata_gauss.write(rms_dic_out+file_name)